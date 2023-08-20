""" 1 """
""" from PIL import ImageGrab
import time

interval = int(input("Введіть інтервал для скриншотів (в секундах): "))
num_screenshots = int(input("Введіть число скриншотів при дії програми: "))
folder_path = input("Введіть папку для запису екрана: ")

for i in range(num_screenshots):
    file_name = folder_path + "/screenshot" + str(i + 1) + ".png"

    im = ImageGrab.grab()
    im.save(file_name)

    time.sleep(interval)
"""

""" 2 """
""" import pyautogui
import time

form_data = {
    'name': 'Pasha Siahrovskyi',
    'email': 'pasha.syagro@gmail.com',
    'phone': '+380986034232',
    'message': 'Hello!',
    'gender': 'male',
    'newsletter': True,
    'category': 'cat1'
}

field_selectors = {
    'name': '//*[@id="name"]',
    'email': '//*[@id="email"]',
    'phone': '//*[@id="phone"]',
    'message': '//*[@id="message"]',
    'gender': {
        'male': '//*[@id="gender-male"]',
        'female': '//*[@id="gender-female"]'
    },
    'newsletter': '//*[@id="newsletter"]',
    'category': {
        'cat1': '//*[@id="category-cat1"]',
        'cat2': '//*[@id="category-cat2"]'
    }
}

url = 'https://example.com/contact'

pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(2)
pyautogui.write(url)
pyautogui.press('enter')
time.sleep(5)

for field, value in form_data.items():
    selector = field_selectors[field]
    if isinstance(selector, dict):
        selector = selector[value]
    pyautogui.click(selector)
    pyautogui.write(value)

submit_selector = '//*[@id="submit"]'
pyautogui.click(submit_selector) """

""" 3 """
""" import pyautogui
import keyring
def login(username, password):
    pyautogui.click(100, 100) 
    pyautogui.typewrite(username)
    pyautogui.typewrite(password)
    pyautogui.click(200, 200) 

keyring.set_password("my_app", "username", "my_username")
keyring.set_password("my_app", "password", "my_password")

username = keyring.get_password("my_app", "username")
password = keyring.get_password("my_app", "password")

login_method = input("Enter login method (email/password, social media, two-factor authentication): ")
if login_method == "email/password":
    login(username, password)
elif login_method == "social media":
    pyautogui.click(300, 300)  
    pyautogui.typewrite(username)
    pyautogui.typewrite(password)
    pyautogui.click(400, 400)  
elif login_method == "two-factor authentication":
    pyautogui.click(500, 500) 
    pyautogui.typewrite(username)
    pyautogui.typewrite(password)
    code = input("Enter two-factor authentication code: ")
    pyautogui.typewrite(code)
    pyautogui.click(600, 600) 
else:
    print("Invalid login method.")
"""

""" 4 """
""" import pyautogui
import time

def create_new_file(file_type, file_name):
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.typewrite(file_type)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(5) 
    pyautogui.hotkey('ctrl', 'o')
    time.sleep(1)
    pyautogui.press('down')
    pyautogui.press('enter')
    time.sleep(1)
    if file_type == "Word":
        pyautogui.hotkey('alt', 'w', 'n')
    elif file_type == "Excel":
        pyautogui.hotkey('alt', 'f', 'n')
    elif file_type == "PowerPoint":
        pyautogui.hotkey('alt', 'f', 'n')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
    pyautogui.typewrite(file_name)
    pyautogui.press('enter')

create_new_file("Word", "my_file.docx")
"""

""" 5 """
""" import pyautogui
import time

download_button = (100, 100)
file_selection = (200, 200)

for file in file_list:
    try:
        pyautogui.moveTo(download_button[0], download_button[1], duration=1)
        pyautogui.click()

        pyautogui.moveTo(file_selection[0], file_selection[1], duration=1)
        pyautogui.click()

        pyautogui.hotkey('ctrl', 's')
        time.sleep(2)
        pyautogui.press('enter')

        time.sleep(10)

    except Exception as e:
        print(f"Error occurred while downloading {file}: {e}")
"""

""" 6 """
""" import os

def traverse_dir(path):
    for root, dirs, files in os.walk(path):
        print(f"Directory: {root}")

        for file in files:
            print(f"File: {os.path.join(root, file)}")

        for dir in dirs:
            print(f"Subdirectory: {os.path.join(root, dir)}")

traverse_dir('/path/to/directory')
"""

""" 7 """
""" import os
import shutil

def move_files_with_extension(source_path, dest_path, extension):
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)

    for file in os.listdir(source_path):
        if file.endswith(extension):
            shutil.move(os.path.join(source_path, file), os.path.join(dest_path, file))

move_files_with_extension('/path/to/source/directory', '/path/to/destination/directory', '.py') """

""" 8 """
""" import os
import shutil

def delete_file_or_directory(path):
    if os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
        print(f"{path} and its contents have been deleted.")
    else:
        print(f"{path} does not exist.")

delete_file_or_directory('/path/to/file_or_directory')
"""

""" 9 """
""" import psutil

processes = psutil.process_iter()

for process in processes:
	print(f"Name: {process.name()} | PID: {process.pid}")
"""

""" 10 """
""" import os

def change_owner_and_group(path, user, group):
    uid = pwd.getpwnam(user).pw_uid
    gid = grp.getgrnam(group).gr_gid

    os.chown(path, uid, gid)
    print(f"Owner and group of {path} have been changed to {user}:{group}.")

change_owner_and_group('/path/to/file_or_directory', 'new_user', 'new_group') """