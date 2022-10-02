from tkinter import *
from tkinter import scrolledtext as tkscrolled
import json
import os
import time

window = Tk()
window.title("Dictionary Program")
window.resizable(False, False)
#window.configure(bg="black")

dictionary = {}
script_dir = os.path.dirname(os.path.abspath(__file__))#gets the current directory of the script
current_word = ""

with open(script_dir + "./definitions.json", "r") as read_file:
    dictionary = json.load(read_file)
    read_file.close()


#this functions is run when the button is pressed
def search_dict():
    definition = ""
    entry_text = search_entry.get()
    global current_word

    if defintion_textbox["state"] == "normal":
        change_search_status_label("Save your definition changes before searching!", "red")
        return

    current_word = entry_text

    if not entry_text:
        change_search_status_label("You must enter a value!", "red")
        return

    search_entry.delete(0, END)
    try:
        global dictionary
        definition = dictionary[entry_text.lower()]
    except KeyError:
        change_search_status_label("This value is not in the dictionary!", "red")
        return

    definition_label.config(text=f"Defintion of {entry_text}: ")

    defintion_textbox.config(state="normal")
    defintion_textbox.delete(0.0, END)
    defintion_textbox.insert(END, definition)
    defintion_textbox.config(state="disabled")



def add_key_value():
    def clear_add_entry():
        word_entry.delete(0, END)
        definition_entry.delete(0.0, END)

    word_entry_text = word_entry.get().lower().strip()
    def_entry_text = definition_entry.get(0.0, END).strip()

    if not word_entry_text or not def_entry_text:
        change_add_status_label("You cannot leave the boxes empty!", "red")
        clear_add_entry()
        return

    if word_entry_text in dictionary:
        change_add_status_label("This word is already in the dictionary!", "red")
        clear_add_entry()
        return

    clear_add_entry()

    temp_dict = {word_entry_text: def_entry_text}
    dictionary.update(temp_dict)

    with open(script_dir + "./definitions.json", "w") as write_file:
        json.dump(dictionary, write_file)
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
        write_file.close()
    
    change_delete_status_label("Deleted Word", "green")



def save_textbox():
    dictionary[current_word] = defintion_textbox.get(0.0, END)
        
    with open(script_dir + "./definitions.json", "w") as write_file:
        json.dump(dictionary, write_file)
        write_file.close()
    
    change_edit_definition_status_label("Saved new definition!", "green")



def edit_definition():
    if not current_word:
        change_edit_definition_status_label("You must have a definition to edit!", "red")
        return

    if defintion_textbox["state"] == "disabled":#making the box editable
        defintion_textbox.config(state="normal")
        edit_button.config(text="Save")
        edit_button.config(bg="light yellow")

    elif defintion_textbox["state"] == "normal":#making the box uneditable and saving the new defintion
        defintion_textbox.config(state="disabled")
        edit_button.config(text="Edit")
        edit_button.config(bg="light blue")

        save_textbox()



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

def change_edit_definition_status_label(error_text, colour):
    edit_definition_status_label.config(fg=colour)
    edit_definition_status_label.config(text=error_text)
    edit_definition_status_label.after(4000, lambda: edit_definition_status_label.config(text=""))


#use the dictionary
definition_label = Label(window, text="Search: ")
definition_label.grid(row=0, column=0)

search_entry = Entry(window)
search_entry.grid(row=1, column=0, pady=5, padx=(78, 0), sticky=W, ipady=3)

enter_button = Button(window, text="Enter", command=search_dict, bg="light blue")
enter_button.grid(row=1, column=0, pady=5, padx=(0, 78), sticky=E)

search_status_label = Label(window, text="")
search_status_label.grid(row=2, column=0)

definition_label = Label(window, text="Definition: ")
definition_label.grid(row=2, column=0, sticky=S, padx=20)

defintion_textbox = Text(window, width="35", height="21", wrap=WORD, state="disabled")
defintion_textbox.grid(row=3, column=0, rowspan=3, pady=3, padx=20)

edit_button = Button(window, text="Edit", bg="light blue",command=edit_definition)
edit_button.grid(row=6, column=0, sticky=W, padx=20, pady=(3, 10))

edit_definition_status_label = Label(window, text="")
edit_definition_status_label.grid(row=6, column=0, sticky=E, padx=20)

#add key/value to the dict
add_word_label = Label(window, text="Enter Word: ")
add_word_label.grid(row=0, column=1)

word_entry = Entry(window, width=23)
word_entry.grid(row=1, column=1, padx=40)

add_definition_label = Label(window, text="Enter Defintion: ")
add_definition_label.grid(row=2, column=1, sticky=S)

definition_entry = tkscrolled.ScrolledText(window, width=15, height=6, wrap=WORD)
definition_entry.grid(row=3, column=1, sticky=N, pady=3)

add_button = Button(window, text="Add Definition", command=add_key_value, bg="#87AE73")
add_button.grid(row=3, column=1, sticky=S, pady=1)

add_status_label = Label(window, text="")
add_status_label.grid(row=4, column=1, sticky=S)

#delete key/value from dict
delete_label = Label(window, text="Enter Word:")
delete_label.grid(row=5, column=1, pady=(0, 60))

delete_entry = Entry(window, width=23)
delete_entry.grid(row=5, column=1)

delete_button = Button(window, text="Delete Word", bg="#FF6961", command=delete_key_value)
delete_button.grid(row=5, column=1, pady=(40, 0), sticky=S)

delete_status_label = Label(window, text="")
delete_status_label.grid(row=6, column=1)

window.mainloop()