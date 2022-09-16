from tkinter import *
from turtle import st

window = Tk()

def button_click():
    typed_text = entry1.get()
    text1.delete(0.0, END)
    typed_text = "You typed " + typed_text
    text1.insert(END, typed_text)


entry1 = Entry(window, width=20, bg="light blue")
entry1.grid(row=1, column=0, sticky=E)

button1 = Button(window, text="press me", width=10, command=button_click)
button1.grid(row=2, column=0, sticky=W)

text1 = Text(window, width=30, height=10, wrap=WORD, background="blue")
text1.grid(row=3, column=0, columnspan=2, sticky=W)

window.mainloop()