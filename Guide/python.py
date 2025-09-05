# Переменные и типы данных
# Python автоматически определяет тип переменной:
x = 10         # int
y = 3.14       # float
name = "Коля"  # str
is_active = True  # bool

# Ввод и вывод
name = input("Введите имя: ")
print("Привет,", name)

# Это однострочный комментарий
"""
Это многострочный
комментарий
"""

# Условные операторы
age = 20
if age >= 18:
    print("Взрослый")
elif age >= 13:
    print("Подросток")
else:
    print("Ребенок")

# Циклы
for i in range(5):  # 0,1,2,3,4
    print(i)
x = 0
while x < 5:
    print(x)
    x += 1

# Прерывания
for i in range(10):
    if i == 5:
        break  # выходит из цикла
    if i % 2 == 0:
        continue  # пропускает итерацию
    print(i)

# Работа со строками
text = "Hello, Python"
print(text.lower())    # hello, python
print(text.upper())    # HELLO, PYTHON
print(text.split(",")) # ['Hello', ' Python']
print(text[0:5])       # Hello
print("Python" in text)  # True

# Работа со списками
fruits = ["apple", "banana", "cherry"]
print(fruits[0])   # apple
fruits.append("orange")  # добавление
fruits.remove("banana")  # удаление
print(len(fruits))        # длина списка

# Простые функции
def greet(name):
    return f"Привет, {name}!"
print(greet("Коля"))
# С аргументами по умолчанию:
def power(x, n=2):
    return x ** n
print(power(3))   # 9
print(power(2, 3)) # 8
