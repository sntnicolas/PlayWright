books = [
    "Война и мир;Толстой;500",
    "Преступление и наказание;Достоевский;400",
    "Мастер и Маргарита;Булгаков;350",
    "Анна Каренина;Толстой;450",
    "Идиот;Достоевский;380"
]

while True:
    print("Выберите действие:")
    print("1 - список всех книг")
    print("2 - поиск по автору")
    print("3 - средняя цена")
    print("4 - самая дорогая/дешёвая книга")
    print("0 - выход")

    menu = int(input("Выберите действие:"))
    if menu == 0:
        print("Работа завершена.")
        break
    else:
        book_sorter(menu)

    def book_sorter():
        names = [b.split(";")[0] for b in books]


    author = [b.split(";")[1] for b in books]
    cost = [b.split(";")[2] for b in books]

    if menu == 1:
        for i in range(len(books)):
            print(f"{names[i]} - {author[i]} ({cost[i]} руб.)")

    elif menu == 2:
        author_input = input("Введите фамилию автора:")
        print(f"Книги автора Толстой:")
        author_books = []
        for i in range(len(books)):
            if author_input == author[i]:
                author_books.append({books[i]})
        if len(author_books) == 0:
            print("Книг этого автора нет.")
        else:
            for i in range(len(author_books)):
                print(author_books[i])

    elif menu == 3:
        average_cost = sum(cost) / len(cost)
        print(f"{average_cost}")

    elif menu == 4:
        max_index = 0
        min_index = 0
        for i in range(len(cost)):
            if cost[i] > cost[max_index]:
                max_index = i
            if cost[i] < cost[min_index]:
                min_index = i
        print(f"Самая дорогая книга: {names[max_index]} ({cost[max_index]} руб.)")
        print(f"Самая дешёвая книга: {names[min_index]} ({cost[min_index]} руб.)")



