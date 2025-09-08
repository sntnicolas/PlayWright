# обработка ошибок с файлом
try:
    with open("data.txt") as f:
        data = f.read()
except FileNotFoundError:
    print("Файл не найден!")
except PermissionError:
    print("Нет доступа к файлу!")
else:
    print("Файл прочитан успешно")
finally:
    print("Завершение работы с файлом")
# обработка ошибок с данными
try:
    x = int(input("Введите число: "))
    result = 10 / x
except ValueError:
    print("Это не число!")
except ZeroDivisionError:
    print("На ноль делить нельзя!")
else:
    print("Всё прошло успешно, результат:", result)
finally:
    print("Конец программы")
