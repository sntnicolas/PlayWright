# 1. Сортировка по нескольким критериям
students = [
    ("Коля", 85),
    ("Маша", 92),
    ("Иван", 92),
    ("Света", 59),
]
# Сначала по оценке (убывание), потом по имени (возрастание)
sorted_students = sorted(students, key=lambda x: (-x[1], x[0]))
print(sorted_students)

# 2. Сортировка словаря
grades = {"Коля": 85, "Маша": 92, "Иван": 73}
sorted_grades = dict(sorted(grades.items(), key=lambda item: item[1], reverse=True))
print(sorted_grades)

# 3. Сортировка с operator.itemgetter
from operator import itemgetter
pairs = [(1, "b"), (3, "a"), (2, "c")]
print(sorted(pairs, key=itemgetter(1)))  # сортировка по второму элементу

# 4. Сортировка со сложной функцией
words = ["banana", "apple", "pear", "grape"]
# сортировка по последней букве
print(sorted(words, key=lambda w: w[-1]))

# 5. Стабильная сортировка - при одинаковом значении порядок сохраняется
data = [("Иван", 2), ("Маша", 2), ("Коля", 1)]
# сначала по имени
data = sorted(data, key=lambda x: x[0])
# потом по числу
data = sorted(data, key=lambda x: x[1])
print(data)
# Иван и Маша сохранят порядок"
