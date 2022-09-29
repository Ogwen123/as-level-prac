from tkinter import *

window = Tk()
window.title("Dictionary Program")
window.geometry("200x300")

dictionary = {
    "ALU":"Arithmatic Logic Unit", 
    "CU":"Control Unit", 
    "CPU":"Central Processing Unit", 
    "RAM":"Random Access Memory", 
    "GPU":"Graphics Processing Unit", 
    "PSU":"Power Supply Unit"
    }

def button_click():
    entry_text = entry.get()
    entry.delete(0, END)
    try:
        definition = dictionary[entry_text.upper()]
    except KeyError:
        print("This is not in the dictionary.")

    text.config(state="normal")
    text.delete(0.0, END)
    text.insert(END, definition)
    text.config(state="disabled")


label = Label(window, text="Enter your acronym here: ")
label.grid(row=0, column=0)

entry = Entry(window)
entry.grid(row=1, column=0)

button = Button(window, text="Enter", command=button_click)
button.grid(row=2, column=0)

text = Text(window, width="20", height="8", padx=(10, 10))
text.grid(row=3, column=0)

window.mainloop()