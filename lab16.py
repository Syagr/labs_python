""" 1 """
""" import random
import string
import sqlite3

# Функція для генерації випадкових імен
def generate_random_name():
    name_length = random.randint(5, 10)
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(name_length))

# Функція для генерації випадкової електронної пошти
def generate_random_email():
    name = generate_random_name()
    domain = random.choice(['gmail.com', 'yahoo.com', 'hotmail.com'])
    return f'{name}@{domain}'

# Функція для генерації випадкової адреси
def generate_random_address():
    street = generate_random_name()
    number = random.randint(1, 100)
    city = generate_random_name()
    return f'{number} {street}, {city}'

# Функція для генерації випадкових товарів
def generate_random_products(num_products):
    products = []
    for _ in range(num_products):
        name_length = random.randint(5, 15)
        letters = string.ascii_letters + string.digits
        product_name = ''.join(random.choice(letters) for _ in range(name_length))
        price = round(random.uniform(10, 1000), 2)
        products.append((product_name, price))
    return products

# Параметри для генерації замовлень
num_customers = 10
num_orders = 20
num_products_per_order = 3

# Підключення до бази даних SQLite
conn = sqlite3.connect('orders.db')
cursor = conn.cursor()

# Створення таблиці клієнтів
cursor.execute('''CREATE TABLE IF NOT EXISTS customers
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT,
                   email TEXT,
                   address TEXT)''')

# Створення таблиці товарів
cursor.execute('''CREATE TABLE IF NOT EXISTS products
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT,
                   price REAL)''')

# Створення таблиці замовлень
cursor.execute('''CREATE TABLE IF NOT EXISTS orders
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   customer_id INTEGER,
                   product_id INTEGER,
                   quantity INTEGER,
                   FOREIGN KEY (customer_id) REFERENCES customers (id),
                   FOREIGN KEY (product_id) REFERENCES products (id))''')

# Згенерувати випадкові дані про клієнтів та вставити їх у базу даних
for _ in range(num_customers):
    name = generate_random_name()
    email = generate_random_email()
    address = generate_random_address()
    cursor.execute("INSERT INTO customers (name, email, address) VALUES (?, ?, ?)", (name, email, address))

# Згенерувати випадкові дані про товари та вставити їх у базу даних
products = generate_random_products(num_products_per_order)
for product in products:
    cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", product)

# Згенерувати випадкові замовлення клієнтів та вставити їх у базу даних
for _ in range(num_orders):
    customer_id = random.randint(1, num_customers)
    product_id = random.randint(1, num_products_per_order)
    quantity = random.randint(1, 10)
    cursor.execute("INSERT INTO orders (customer_id, product_id, quantity) VALUES (?, ?, ?)", (customer_id, product_id, quantity))

# Зберегти зміни у базі даних
conn.commit()

# Запит для отримання інформації про замовлення
cursor.execute('''SELECT customers.name, SUM(products.price * orders.quantity) AS total_cost
                  FROM orders
                  JOIN customers ON customers.id = orders.customer_id
                  JOIN products ON products.id = orders.product_id
                  GROUP BY customers.id''')

# Вивести результати запиту
results = cursor.fetchall()
for row in results:
    customer_name, total_cost = row
    print(f"Customer: {customer_name}, Total Cost: {total_cost}")

# Закрити підключення до бази даних
conn.close() """

""" 2 """
""" import random
import string
import sqlite3
import statistics

# Функція для генерації випадкових назв товарів
def generate_random_name():
    name_length = random.randint(5, 15)
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(name_length))

# Параметри для генерації товарів
num_products = 100

# Підключення до бази даних SQLite
conn = sqlite3.connect('products.db')
cursor = conn.cursor()

# Створення таблиці товарів
cursor.execute('''CREATE TABLE IF NOT EXISTS products
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT,
                   price REAL,
                   category TEXT,
                   quantity INTEGER)''')

# Згенерувати випадкові дані про товари та вставити їх у базу даних
for _ in range(num_products):
    name = generate_random_name()
    price = round(random.uniform(10, 1000), 2)
    category = random.choice(['Electronics', 'Clothing', 'Home', 'Books'])
    quantity = random.randint(1, 100)
    cursor.execute("INSERT INTO products (name, price, category, quantity) VALUES (?, ?, ?, ?)", (name, price, category, quantity))

# Зберегти зміни у базі даних
conn.commit()

# Виконати запит для отримання цін товарів
cursor.execute("SELECT price FROM products")
prices = cursor.fetchall()

# Перетворити ціни на числовий формат
prices = [price[0] for price in prices]

# Обчислити середню ціну
average_price = statistics.mean(prices)

# Обчислити загальну кількість товарів
total_quantity = sum(row[0] for row in cursor.execute("SELECT quantity FROM products"))

# Обчислити максимальну ціну
max_price = max(prices)

# Вивести статистичний опис
print("Statistical Summary:")
print(f"Average Price: {average_price}")
print(f"Total Quantity: {total_quantity}")
print(f"Maximum Price: {max_price}")

# Закрити підключення до бази даних
conn.close()
"""

""" 3 """
""" import json
import sqlite3

# Відкрити файл з даними погоди
with open('weather_data.json') as file:
    weather_data = json.load(file)

# Підключення до бази даних SQLite
conn = sqlite3.connect('weather.db')
cursor = conn.cursor()

# Створення таблиці погоди
cursor.execute('''CREATE TABLE IF NOT EXISTS weather
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   date TEXT,
                   temperature REAL,
                   humidity INTEGER,
                   wind_speed REAL)''')

# Вставка даних про погоду у таблицю
for data in weather_data:
    date = data['date']
    temperature = data['temperature']
    humidity = data['humidity']
    wind_speed = data.get('wind_speed')  # Використовуємо get() для отримання значення з можливим відсутнім ключем
    cursor.execute("INSERT INTO weather (date, temperature, humidity, wind_speed) VALUES (?, ?, ?, ?)", (date, temperature, humidity, wind_speed))

# Зберегти зміни у базі даних
conn.commit()

# Закрити підключення до бази даних
conn.close()
"""