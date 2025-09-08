data1 = [(1, "Коля"), (2, "Маша"), (3, "Иван")]
"""
1. Коля
2. Маша
3. Иван
"""
for num, name in data1:
    print(f"{num}. {name}")

data2 = ["ab", "cd", "ef"]
"""
a b
c d
e f
"""
for a, b in data2:
    print(a, b)

data3 = ["python", "java", "c++"]
"""
p ['y','t','h','o','n']
j ['a','v','a']
c ['+','+']
"""
for sym, *bols in data3:
    print(sym, bols)

data4 = {"Коля": 85, "Маша": 92, "Иван": 73}
"""
Коля — 85
Маша — 92
Иван — 73
"""
for name, score in data4.items():
    print(f"{name} — {score}")

data5 = [(1, "apple", 10), (2, "banana", 20), (3, "cherry", 30)]
"""
apple 10
banana 20
cherry 30
"""
for _, fruit, num in data5:
    print(fruit, num)
