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
    # squares = (lambda x: x ** 2, args)
    # print(squares)
    # print(lambda x: x ** 2, args)

    list_squares: [x ** 2 for x in args]
    print(list_squares)
    print(f"Сумма квадратов : {sum(list_squares)}")
    print(f"Макс число : {max(args)}")


    list_squares2 = {key: key ** 2 for key in kwargs if n == int else n:}
    print(f"{key} = {value} {string}" if arg != int else  2 if arg ")


analyze_data(1, 2, 3, a=5, b="hello", c=10)
