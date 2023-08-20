""" 1 """
""" import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

base_url = 'https://www.yakaboo.ua/ua/bestseleri-komplekt-iz-7-knig.html'
chrome_driver_path = 'path/to/chromedriver.exe'
num_books_to_scrape = 7

def scrape_books():
    args = {"info": []}

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run Chrome in headless mode (without GUI)

    with webdriver.Chrome(service=Service(chrome_driver_path), options=options) as driver:
        driver.get(base_url)
        time.sleep(2)

        book_elements = driver.find_elements(By.CSS_SELECTOR, '.description__content p a')
        urls = [element.get_attribute('href') for element in book_elements[:num_books_to_scrape]]

        for url in urls:
            driver.get(url)
            time.sleep(2)
            try:
                year_element = driver.find_element(By.XPATH, '//*[@id="product"]/div[1]/div/div/div/section/div[2]/section/div[4]/div[2]/button')
                year = year_element.text
            except:
                year = ""

            try:
                author_element = driver.find_element(By.XPATH, '//*[@id="product"]/div[1]/div/div/div/section/div[5]/div/div[2]/div[1]/div[2]/a/span')
                author = author_element.text
            except:
                author = ""

            try:
                name_element = driver.find_element(By.XPATH, '//*[@id="product"]/div[1]/div/div/section[1]/div[2]/div[1]/h1')
                name = name_element.text
            except:
                name = ""

            book_info = {'author': author, 'year': year, 'name': name}
            args['info'].append(book_info)

    json_data = json.dumps(args, indent=4, ensure_ascii=False)
    with open("my.json", "w", encoding="utf-8") as file:
        file.write(json_data)

scrape_books()
"""

""" 2 """
""" import requests
import json
from bs4 import BeautifulSoup

link_url = 'https://rozetka.com.ua/ua/mobile-phones/c80003/sort=rank/'
num_products_to_scrape = 50

def scrape_products():
    response = requests.get(link_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    products = []
    for item in soup.select('ul.catalog-grid li')[:num_products_to_scrape]:
        colors = {}

        color_items = item.select('ul.goods-tile__colors-list li')
        if not color_items:
            continue

        for color_item in color_items:
            url = color_item.find('a')['href']
            color = color_item.text.strip().split()[-2] if len(color_item.text.strip().split()) >= 2 else None
            status = "Out of stock" if "not-available" in color_item.get('class', []) else "Available"
            if color:
                colors[color] = status

            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            name = soup.find('h1', class_="product__title").text.strip()
            brand = name.split()[3]

            price_element = soup.find('p', class_='product-price__big')
            price = price_element.text.strip().replace('₴', '').replace('\xa0', '').replace(' ', '') if price_element else None

            discount_element = soup.find('p', class_='product-price__small ng-star-inserted')
            discount = abs(round(100.0 * (int(price) - int(discount_element.text.strip().replace('₴', '').replace('\xa0', '').replace(' ', ''))) / int(discount_element.text.strip().replace('₴', '').replace('\xa0', '').replace(' ', '')))) if discount_element and price else None

            product = {'name': name, 'brand': brand, 'colors': colors}
            if price:
                product['price'] = price
            if discount:
                product['discount'] = f'{discount}%'

            products.append(product)

    data = {'info': products[:num_products_to_scrape]}
    json_data = json.dumps(data, indent=4, ensure_ascii=False)
    with open('my1.json', 'w', encoding='utf-8') as file:
        file.write(json_data)

scrape_products()
"""

""" 3 """
""" import json
import re
import matplotlib.pyplot as plt


def load_data(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        json_data = file.read()
    product_data = json.loads(json_data)
    return product_data


def process_data(product_data):
    models = [product["name"] for product in product_data['info']]
    prices = []
    for product in product_data['info']:
        price_str = re.sub(r'[^\d.]', '', product["price"])
        price_float = float(price_str) if price_str else 0.0
        prices.append(price_float)
    return models, prices


def plot_prices_vs_models(models, prices):
    plt.figure(figsize=(12, 6))
    plt.scatter(models, prices)
    plt.xticks(rotation=90)
    plt.xlabel("Model")
    plt.ylabel("Price")
    plt.title("Price vs. Model")
    plt.tight_layout()
    plt.show()


def Runner():
    file_path = "my1.json"
    product_data = load_data(file_path)
    models, prices = process_data(product_data)
    plot_prices_vs_models(models, prices)


Runner()
"""