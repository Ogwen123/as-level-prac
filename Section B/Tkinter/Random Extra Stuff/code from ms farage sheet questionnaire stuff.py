from tkinter import *

window = Tk()
window.title("Survey")
window.geometry("300x600")

def submitclick():
    name = nameEntry.get()
    age1 = spinVar.get()
    gender = radioVar.get()

    box1 = check1.get()
    box2 = check2.get()
    box3 = check3.get()
    box4 = check4.get()
    box5 = check5.get()

    displayBox.delete(0.0, END)
    displayBox.insert(END, name)
    displayBox.insert(END, "\n")

    displayBox.insert(END, age1)
    displayBox.insert("\n")

    if gender == 1: displayBox.insert(END, "Male")
    if gender == 2: displayBox.insert(END, "Female")
    if gender == 3: displayBox.insert(END, "Other")

    displayBox.insert("\n")

    if box1 == 1: displayBox.insert(END, "Stamp Collecting")
    if box1 == 2: displayBox.insert(END, "Chess")
    if box1 == 3: displayBox.insert(END, "Reading")
    if box1 == 4: displayBox.insert(END, "Sports")
    if box1 == 5: displayBox.insert(END, "Walking")

    displayBox.insert(END, "\n")

check1 = IntVar()
check2 = IntVar()
check3 = IntVar()
check4 = IntVar()
check5 = IntVar()
radioVar = IntVar()
spinVar = IntVar()

titleLabel = Label(width=10, text="Questionnaire")
titleLabel.grid(row=0, column=0)

nameLabel = Label(window, text="Name: ")
nameLabel.grid(row=2, column=0, sticky=W)

nameEntry = Entry(window, width=10)
nameEntry.grid(row=2, column=1, sticky=W)

ageLabel = Label(window, text="Age: ", width=5)
ageLabel.grid(row=3, column=0, sticky=W)

ageSpin = Spinbox(window, textvariable=spinVar, from_=1, to=100)
ageSpin.grid(row=3, column=1, sticky=W)

genderLabel = Label(window, width=5, text="Gender: ")
genderLabel.grid(row=4, column=0, sticky=W)

rb = Radiobutton(window, text="Male", variable=radioVar, value=1)
rb.grid(row=5, column=1, sticky=W)

rb = Radiobutton(window, text="Female", variable=radioVar, value=2)
rb.grid(row=6, column=1, sticky=W)

rb = Radiobutton(window, text="Other", variable=radioVar, value=3)
rb.grid(row=7, column=1, sticky=W)

hobbiesLabel = Label(window, width=5, text="Hobbies: ")
hobbiesLabel.grid(row=8, column=0, sticky=W)

cb1 = Checkbutton(window, text="Stamp Collecting", variable=check1)
cb1.grid(row=9, column=1, sticky=W)

cb2 = Checkbutton(window, text="Reading", variable=check2)
cb2.grid(row=10, column=1, sticky=W)

cb3 = Checkbutton(window, text="Sports", variable=check3)
cb3.grid(row=11, column=1, sticky=W)

cb4 = Checkbutton(window, text="Chess", variable=check4)
cb4.grid(row=12, column=1, sticky=W)

cb5 = Checkbutton(window, text="Walking", variable=check5)
cb5.grid(row=13, column=1, sticky=W)

displayBox = Text(window, width=20, height=10)
displayBox.grid(row=14, column=0, columnspan=2, sticky=W)

submitButton = Button(window, text="Submit", command=submitclick, colour="green")
submitButton.grid(row=15, column=0, sticky=W)

window.mainloop()