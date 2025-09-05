data = [
    "Коля 85",
    "Маша 92",
    "Иван 73",
    "Света 59",
    "Петя 100",
    "Оля 40"
]

print("Выберите действие: ")
print("1 - статистика")
print("2 - лучшие студенты")
print("3 - худшие студенты")
print("0 - выход")

choise = int(input())

def programma(choise):
    names: list[str] = []
    scores: list[int] = []

    number_good = 0
    number_bad = 0
    total = 0
    best_students: list[str] = []
    worst_students: list[str] = []

    for student in data:
        name_score = student.split(" ")
        name: str = str(name_score[0])
        score: int = int(name_score[1])

        names.append(name)
        scores.append(score)
        if score >= 60:
            number_good +=1
            if score >= 90:
                best_students.append(name)
        elif score < 60:
            number_bad += 1
            worst_students.append(name)
        total += score

    total_average = total / len(scores)

    if choise == 1:
        print("Сдали: " + str(number_good))
        print("Провалили: " + str(number_bad))
        print("Средний балл: " + str(total_average))

    elif choise == 2:
        print("Лучшие студенты: ")
        for everyone in best_students:
            print(everyone.upper())

    elif choise == 3:
        print("Худшие студенты: ")
        for everyone in worst_students:
            print(everyone.lower())

    elif choise == 0:
        print("Работа завершена.")

programma(choise)