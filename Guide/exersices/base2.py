books = [
    "Война и мир;Толстой;500",
    "Преступление и наказание;Достоевский;400",
    "Мастер и Маргарита;Булгаков;350",
    "Анна Каренина;Толстой;450",
    "Идиот;Достоевский;380"
]


def book_sorter(menu):
    names = [b.split(";")[0] for b in books]
    authors = [b.split(";")[1] for b in books]
    cost = [int(b.split(";")[2]) for b in books]

    if menu == 1:
        for i in range(len(books)):
            print(f"{names[i]} - {authors[i]} ({cost[i]} руб.)")

    elif menu == 2:
        author_input = input("Введите фамилию автора:")
        print(f"Книги автора {author_input}:")
        # author_books = []
        # for i in range(len(books)):
        #     if author_input == authors[i]:
        #         author_books.append(f"{names[i]} ({cost[i]} руб.)")
        author_books = [f"{names[i]} ({costs[i]} руб.)"
                        for i in range(len(books)) if authors[i] == author_input]

        # if len(author_books) == 0:
        #     print("Книг этого автора нет.")
        # else:
        #     for i in range(len(author_books)):
        #         print(author_books[i])
        if author_books:
            for book in author_books:
                print(book)
        else:
            print("Книг этого автора нет.")


    elif menu == 3:
        average_cost = sum(cost) / len(cost)
        print(f"{average_cost:.2f}")

    elif menu == 4:
        # max_index = 0
        # min_index = 0
        # for i in range(len(cost)):
        #     if cost[i] > cost[max_index]:
        #         max_index = i
        #     if cost[i] < cost[min_index]:
        #         min_index = i
        max_index = cost.index(max(cost))
        min_index = cost.index(min(cost))
        print(f"Самая дорогая книга: {names[max_index]} ({cost[max_index]} руб.)")
        print(f"Самая дешёвая книга: {names[min_index]} ({cost[min_index]} руб.)")
    else:
        print(f"Введено неверное значение, попробуйте другое")

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


