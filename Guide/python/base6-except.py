try:
    with open("data.txt", "r") as f:
        students = []
        for line in f:
            pair = line.split()
            try:
                name = str(pair[0])
                score = int(pair[1])
            except ValueError:
                print(f"Неверный формат в строке: {line}")
            students.append((name, score))


            # print(line.split())
            # students.append(line.split())
        print(students)
        # dic = {f"{f.readline}"}

except FileNotFoundError:
    print("File not found")
