# 1. Простая распаковка кортежей
pairs = [(1, "Коля"), (2, "Маша"), (3, "Иван")]
for num, name in pairs:
    print(num, name)

# 2. Распаковка строк (строка = список символов)
for a, b in ["ab", "cd", "ef"]:
    print(a, b)

# 3. Распаковка со *
words = ["python", "java", "c++"]
for first, *rest in words:
    print(first, rest)

# 4. Распаковка в словарях
students = {"Коля": 85, "Маша": 92, "Иван": 73}
for key, value in students.items(): """!!! ОБЯЗАТЕЛЬНО ITEMS"""
    print(key, value)

# 5. enumerate + распаковка
for i, (key, value) in enumerate(students.items(), start=1):
    print(i, key, value)

# 6. Игнорирование значений с _
data = [(1, "apple", 10), (2, "banana", 20)]
for _, fruit, price in data:
    print(fruit, price)