from tkinter import *
import json
import os
import time

window = Tk()
window.title("Dictionary Program")
window.geometry("400x400")

dictionary = {}
script_dir = os.path.dirname(os.path.abspath(__file__))

with open(script_dir + "./definitions.json", "r") as read_file:
    dictionary = json.load(read_file)
    read_file.close()

def reload_json():
    with open(script_dir + "./definitions.json", "r") as read_file:
        global dictionary
        dictionary = json.load(read_file)
        read_file.close()

def button_click():
    definition = ""
    done_entry = False
    entry_text = entry1.get()

    if not entry_text:
        change_error_label("You must enter a value!")
        done_entry = True

    entry1.delete(0, END)
    try:
        global dictionary
        definition = dictionary[entry_text.lower()]
    except KeyError:
        if not done_entry:
            change_error_label("This value is not in the dictionary!")
        done_entry = False
    global text
    text1.config(state="normal")
    text1.delete(0.0, END)
    text1.insert(END, definition)
    text1.config(state="disabled")

def change_error_label(error_text):
    search_error_label.config(text=error_text)
    search_error_label.after(4000, lambda: search_error_label.config(text=""))
        

def add_key_value():
    word_entry_text = word_entry.get().lower()
    def_entry_text = definition_entry.get()

    if not word_entry_text or not def_entry_text:
        print("noofhbdo")

    word_entry.delete(0, END)
    definition_entry.delete(0, END)

    print(f"{word_entry_text}:{def_entry_text}")
    temp_dict = {word_entry_text: def_entry_text}
    dictionary.update(temp_dict)

    with open(script_dir + "./definitions.json", "w") as write_file:
        json.dump(dictionary, write_file)
        write_file.close()

    print(dictionary)
    temp_dict = {}


#column 0, using the dictionary
label1 = Label(window, text="Enter your acronym here: ")
label1.grid(row=0, column=0)

entry1 = Entry(window)
entry1.grid(row=1, column=0, pady=5, padx=35, sticky=W)

button1 = Button(
    window, 
    text="Enter", 
    command=button_click, 
    highlightcolor="black", 
    highlightthickness=2)
button1.grid(row=1, column=0, pady=5, padx=35, sticky=E)

search_error_label = Label(window, text="", fg="red")
search_error_label.grid(row=2, column=0)

label2 = Label(window, text="Definition: ")
label2.grid(row=3, column=0, sticky=S, padx=20)

text1 = Text(window, width="25", height="8")
text1.grid(row=4, column=0, rowspan=2, pady=10, padx=20)

#column 1, adding to the dictionary
label3 = Label(window, text="Enter Word: ")
label3.grid(row=0, column=1)

word_entry = Entry(window)
word_entry.grid(row=1, column=1)

label3 = Label(window, text="Enter defintion: ")
label3.grid(row=2, column=1)

definition_entry = Entry(window)
definition_entry.grid(row=3, column=1)

add_button = Button(
    window, 
    text="Add Definition", 
    command=add_key_value, 
    highlightcolor="black", 
    highlightthickness=2
    )
add_button.grid(row=4, column=1, sticky=N, pady=5)

delete_label = Label(window, text="Enter word to delete: ")
delete_label.grid(row=4, column=1, sticky=S)

delete_entry = Entry(window)
delete_entry.grid(row=5, column=1, sticky=N)

delete_button = Entry

window.mainloop()
