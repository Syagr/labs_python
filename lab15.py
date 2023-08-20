""" 1 """
""" import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pickle
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
    ]
    print("Choose a user agent:")
    for i, agent in enumerate(user_agents):
        print(f"{i + 1}. {agent}")
    choice = input("Enter the number of the selected user agent: ")
    index = int(choice) - 1
    if 0 <= index < len(user_agents):
        return user_agents[index]
    else:
        print("Invalid choice. Using the first user agent.")
        return user_agents[0]


def save_credentials(filename, username, password):
    data = {
        "username": username,
        "password": password
    }
    with open(filename, "wb") as file:
        pickle.dump(data, file)


def load_credentials(filename):
    if os.path.exists(filename):
        choice = input("A credentials file already exists. Do you want to use the existing credentials? (y/n): ")
        if choice.lower() == "y":
            with open(filename, "rb") as file:
                return pickle.load(file)
    print("Enter new login credentials:")
    username = input("Username: ")
    password = input("Password: ")
    save_credentials(filename, username, password)
    return {"username": username, "password": password}


def main():
    filename = "credentials.pkl"
    credentials = load_credentials(filename)

    user_agent = get_user_agent()

    chrome_options = Options()
    chrome_options.add_argument(f"--user-agent={user_agent}")

    # Use ChromeDriverManager to automatically download and install the latest Chromedriver
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver.get('https://www.instagram.com/')

    # Wait for the username input element to be visible
    wait = WebDriverWait(driver, 10)
    username = wait.until(EC.visibility_of_element_located((By.NAME, 'username')))
    username.send_keys(credentials["username"])

    password = driver.find_element(By.NAME, 'password')
    password.send_keys(credentials["password"])

    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()

    success = False
    if "login" in driver.current_url:
        print("Invalid login credentials")
    else:
        success = True

    if success:
        cookies = driver.get_cookies()
        with open("login_cookie.pkl", "wb") as file:
            pickle.dump(cookies, file)

    driver.quit()


if __name__ == "__main__":
    main() """

""" 2 """
""" from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json


driver = webdriver.Chrome("C:\\Users\\pasha\\.wdm\\drivers\\chromedriver\\win32\\113.0.5672.63\\chromedriver.exe")  # Укажите путь к вашему Chrome WebDriver


driver.get("https://www.instagram.com/pasha_siahrovskiy/")


driver.add_cookie({'name': 'C:\IT\lab\credentials.pkl', 'value': '<C:\IT\lab\login_cookie.pkl>'})


driver.refresh()

я
search_input = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Search"]')
search_input.click()


search_input.send_keys("5icq1")


time.sleep(2)

profile_link = driver.find_element(By.XPATH, '//div[@class="fuqBx"]/a')
profile_link.click()


time.sleep(2)


follow_button = driver.find_element(By.XPATH, '//button[text()="Follow"]')
follow_button.click()


time.sleep(2)


posts = driver.find_elements(By.XPATH, '//div[@class="v1Nh3 kIKUG  _bz0w"]/a')[:2]

for post in posts:
    post.click()
    time.sleep(2)

    
    like_button = driver.find_element(By.XPATH, '//span[@aria-label="Like"]')
    like_button.click()

    
    time.sleep(1)

    
    close_button = driver.find_element(By.XPATH, '//button[@class="ckWGn"]')
    close_button.click()


comments = []

for i in range(2):
    # Открытие поста
    posts[i].click()
    time.sleep(2)

    post_comments = driver.find_elements(By.XPATH, '//div[@class="C4VMK"]/span')

    for comment in post_comments:
        username = comment.find_element(By.XPATH, './/a').text
        text = comment.find_element(By.XPATH, './/span').text
        comments.append(f"{username} : {text}")

   
    close_button = driver.find_element(By.XPATH, '//button[@class="ckWGn"]')
    close_button.click()


with open('comments.json', 'w') as f:
    json.dump(comments, f)


first_post = driver.find_element(By.XPATH, '//div[@class="v1Nh3 kIKUG  _bz0w"]/a')
first_post.click()
time.sleep(2)

comment_input = driver.find_element(By.XPATH, '//textarea[@placeholder="Add a comment…"]')
comment_text = str(time.time())
comment_input.send_keys(comment_text)

post_comment_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
post_comment_button.click()

time.sleep(2)


driver.save_screenshot("screenshot.png")


message_button = driver.find_element(By.XPATH, '//button[text()="Message"]')
message_button.click()


time.sleep(2)


message_text = "Lastname_Firstname_Group_groupNumber task"
message_input = driver.find_element(By.XPATH, '//textarea[@placeholder="Message..."]')
message_input.send_keys(message_text)


photo_button = driver.find_element(By.XPATH, '//input[@accept="image/*"]')
photo_button.send_keys("путь_к_фото_1") 

send_button = driver.find_element(By.XPATH, '//button[text()="Send"]')
send_button.click()


time.sleep(2)


driver.quit()
"""