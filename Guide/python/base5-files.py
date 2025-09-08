students = [
    ("Коля", 85),
    ("Маша", 92),
    ("Иван", 73),
    ("Света", 59),
    ("Петя", 100),
]


with open("data.txt", "w") as f:
    for name, score in students:
        f.write(f"{name} {score} \n")

with open("data.txt", "r") as f:
    lines = f.readlines()
    for student in lines:
        character = (student.split())
        if int(character[1]) >= 90:
            # print(character[0], character[1])
            print(student.strip())
    # high_scores = [line.split() for line in lines if int(line.split()[1]) >= 90]
    # for name, score in high_scores:
    #     print(name, score)




