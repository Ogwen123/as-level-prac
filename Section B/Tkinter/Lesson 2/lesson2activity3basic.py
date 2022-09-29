from tkinter import *

window = Tk()
window.title("Dictionary Program")

dictionary = {
    "ALU": "Arithmatic Logic Unit",
    "CU": "Control Unit",
    "CPU": "Central Processing Unit",
    "RAM": "Random Access Memory",
    "GPU": "Graphics Processing Unit",
    "PSU": "Power Supply Unit"
}


def button_click():
    definition = ""
    entry_text = entry1.get()
    entry1.delete(0, END)
    try:
        global dictionary
        definition = dictionary[entry_text.upper()]
    except KeyError:
        print("This is not in the dictionary.")
    global text
    text1.config(state="normal")
    text1.delete(0.0, END)
    text1.insert(END, definition)
    text1.config(state="disabled")


def add_key_value():
    word_entry_text = word_entry.get()
    def_entry_text = definition_entry.get()

    word_entry.delete(0, END)
    definition_entry.delete(0, END)

    print(f"{word_entry_text}:{def_entry_text}")
    temp_dict = {word_entry_text.upper(): def_entry_text}
    dictionary.update(temp_dict)
    print(dictionary)
    temp_dict = {}


#column 0, using the dictionary
label1 = Label(window, text="Enter your acronym here: ")
label1.grid(row=0, column=0)

entry1 = Entry(window)
entry1.grid(row=1, column=0)

button1 = Button(window, text="Enter", command=button_click)
button1.grid(row=2, column=0)

text1 = Text(window, width="20", height="4")
text1.grid(row=3, column=0)

#column 1, adding to the dictionary
label2 = Label(window, text="Enter Word: ")
label2.grid(row=0, column=1)

word_entry = Entry(window)
word_entry.grid(row=1, column=1)

label3 = Label(window, text="Enter defintion: ")
label3.grid(row=2, column=1)

definition_entry = Entry(window)
definition_entry.grid(row=3, column=1)

add_button = Button(window, text="Add Definition", command=add_key_value)
add_button.grid(row=4, column=1)

window.mainloop()
