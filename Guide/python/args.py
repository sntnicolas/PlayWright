def print_info1(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")


def print_info2(**kwargs):
    print(*[f"{key} = {value}" for key, value in kwargs.items()], sep='\n')


print_info2(name="Коля", age=25, city="Москва")


def demo(a, b=10, *args, **kwargs):
    print("a:", a)
    print("b:", b)
    print("args:", args)
    print("kwargs:", kwargs)


demo(1, 2, 3, 4, x=5, y=6)
demo(7)
demo(1, 2, 3, 4, mort=2)


def process_data(*args, **kwargs):
    squared_sum = sum(map(lambda x: x ** 2, args))
    print(f"Сумма аргументов: {squared_sum}")
    print(*[f"{key} = {value}" for key, value in kwargs.items()], sep="\n")

process_data(1, 2, 3, a=10, b=20)

def analyze_data(*args, **kwargs):
    list_squares = [x ** 2 for x in args]
    # list_squares = list(map(lambda x: x ** 2, args))
    print(list_squares)
    print(f"Сумма квадратов : {sum(list_squares)}")
    print(f"Макс число : {max(args)}")

    for key, value in kwargs.items():
        print(f"{key} = {value}" + (f" (квадрат: {value ** 2})" if isinstance(value, int) else ""))

analyze_data(1, 2, 3, a=5, b="hello", c=10)

""" тренируем ламбду"""
students = [
    ("Коля", 85),
    ("Маша", 92),
    ("Иван", 73),
    ("Света", 59),
    ("Петя", 100),
]
def sorter(data):
    best = sorted(data, key= lambda x: x[1])

sorter(students)