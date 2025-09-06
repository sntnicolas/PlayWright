
# def printwords (words):
#     newlist = []
#     for i in words:
#         if len(i) <= 5:
#             newlist.append(i.lower())
#     for i in newlist:
#         a = len(i)
#         while a > 0:
#             print(i)
#             a = a - 1

row = "Python is fun and very powerful"
def printwords2(row):
    words = row.split(" ")
    short_words = 0
    long_words = 0
    for word in words:
        if len(word) < 4:
            short_words += 1
        else:
            long_words += 1

    print("long_words: " + str(long_words))
    print("short_words: " + str(short_words))

    print("Long words: ")
    for word in words:
        if len(word) >= 4:
            print(word.upper())

    print("Short words: ")
    for word in words:
        if len(word) < 4:
            print(word.lower())



if __name__ == '__main__':
    printwords2(row)