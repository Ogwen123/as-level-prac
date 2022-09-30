from tkinter import *
import json
import os
import time

window = Tk()
window.title("Dictionary Program")

dictionary = {}
script_dir = os.path.dirname(os.path.abspath(__file__))#gets the current directory of the script

with open(script_dir + "./definitions.json", "r") as read_file:
    dictionary = json.load(read_file)
    read_file.close()

#this functions is run when the button is pressed
def button_click():
    definition = ""
    entry_text = entry1.get()

    if not entry_text:
        change_search_status_label("You must enter a value!", "red")
        return

    entry1.delete(0, END)
    try:
        global dictionary
        definition = dictionary[entry_text.lower()]
    except KeyError:
        change_search_status_label("This value is not in the dictionary!", "red")
        return
    global text
    text1.config(state="normal")
    text1.delete(0.0, END)
    text1.insert(END, definition)
    text1.config(state="disabled")

def add_key_value():
    def clear_add_entry():
        word_entry.delete(0, END)
        definition_entry.delete(0, END)

    word_entry_text = word_entry.get().lower().strip()
    def_entry_text = definition_entry.get().strip()

    if not word_entry_text or not def_entry_text:
        change_add_status_label("You cannot leave the boxes empty!", "red")
        clear_add_entry()
        return

    if word_entry_text in dictionary:
        change_add_status_label("This word is already in the dictionary!", "red")
        clear_add_entry()
        return

    clear_add_entry()

    #print(f"{word_entry_text}:{def_entry_text}")
    temp_dict = {word_entry_text: def_entry_text}
    dictionary.update(temp_dict)

    with open(script_dir + "./definitions.json", "w") as write_file:
        json.dump(dictionary, write_file)
        #reload_json()
        write_file.close()
    temp_dict = {}

    change_add_status_label("Added Word", "green")

def delete_key_value():
    def clear_delete_entry():
        delete_entry.delete(0, END)

    delete_entry_text = delete_entry.get().lower()

    if not delete_entry_text:
        change_delete_status_label("You must enter a value to delete!", "red")
        clear_delete_entry()
        return

    if delete_entry_text not in dictionary:
        change_delete_status_label("This word is not in the dictionary!", "red")
        clear_delete_entry()
        return

    clear_delete_entry()

    del dictionary[delete_entry_text]

    with open(script_dir + "./definitions.json", "w") as write_file:
        json.dump(dictionary, write_file)
        #reload_json()
        write_file.close()
    
    change_delete_status_label("Deleted Word", "green")

#change error labels
def change_search_status_label(error_text, colour):
    search_status_label.config(fg=colour)#changes the text colour of the label
    search_status_label.config(text=error_text)#sets the text in the label
    search_status_label.after(4000, lambda: search_status_label.config(text=""))#makes the label disapear after 4 seconds
        
def change_add_status_label(error_text, colour):
    add_status_label.config(fg=colour)
    add_status_label.config(text=error_text)
    add_status_label.after(4000, lambda: add_status_label.config(text=""))

def change_delete_status_label(error_text, colour):
    delete_status_label.config(fg=colour)
    delete_status_label.config(text=error_text)
    delete_status_label.after(4000, lambda: delete_status_label.config(text=""))


#use the dictionary
label1 = Label(window, text="Enter your word here: ")
label1.grid(row=0, column=0)

entry1 = Entry(window)
entry1.grid(row=1, column=0, pady=5, padx=35, sticky=W)

button1 = Button(window, text="Enter", command=button_click, bg="#A2E9FF")
button1.grid(row=1, column=0, pady=5, padx=35, sticky=E)

search_status_label = Label(window, text="", fg="red")
search_status_label.grid(row=2, column=0)

label2 = Label(window, text="Definition: ")
label2.grid(row=3, column=0, sticky=S, padx=20)

text1 = Text(window, width="25", height="9", wrap=WORD)
text1.grid(row=4, column=0, rowspan=2, pady=10, padx=20)

#add key/value to the dict
label3 = Label(window, text="Enter Word: ")
label3.grid(row=0, column=1)

word_entry = Entry(window)
word_entry.grid(row=1, column=1, padx=40)

label3 = Label(window, text="Enter defintion: ")
label3.grid(row=2, column=1)

definition_entry = Entry(window)
definition_entry.grid(row=3, column=1)

add_button = Button(window, text="Add Definition", command=add_key_value, bg="#87AE73")
add_button.grid(row=4, column=1, sticky=N, pady=5)

add_status_label = Label(window, text="", fg="red")
add_status_label.grid(row=4, column=1)

#delete key/value from dict
delete_label = Label(window, text="Enter word to delete: ")
delete_label.grid(row=4, column=1, sticky=S)

delete_entry = Entry(window)
delete_entry.grid(row=5, column=1, sticky=N)

delete_button = Button(window, text="Delete Word", bg="#FF6961", command=delete_key_value)
delete_button.grid(row=5, column=1, pady=3)

delete_status_label = Label(window, text="", fg="red")
delete_status_label.grid(row=5, column=1, sticky=S)

window.mainloop()
