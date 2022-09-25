total = 0
sen = input("enter sen: ")
for i in range(len(sen)):
    if sen[i] in ["a", "e", "i", "o", "u"]:
        total += 1
print(total)