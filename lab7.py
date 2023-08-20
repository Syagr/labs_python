""" 1 """
""" while True:
    try:
        age = int(input("Введіть ваш вік: "))
        break
    except ValueError:
        print("Помилка: введено некоректне значення. Вік повинен бути числом.")
print("Ваш вік:", age) """

""" 2 """
"""  while True:
    try:
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))
        break
    except ValueError:
        print("Помилка: введено некоректне значення. Числа повинні бути числами.")
product = num1 * num2
print("Добуток чисел:", product)
"""

""" 3 """
""" while True:
    try:
        string = input("Введіть рядок: ")
        if not string:
            raise ValueError("Помилка: рядок порожній.")
        break
    except ValueError as e:
        print(e)
length = len(string) """
