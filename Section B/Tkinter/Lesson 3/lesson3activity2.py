from tkinter import *
from tkinter import scrolledtext as tkscrolled
import json
from datetime import datetime
import os
from tkinter import ttk

WRITE_TO_FILE = False

window = Tk()
window.title("Questionnaire")
#window.resizable(False, False)
window.geometry("350x550")

script_dir = os.path.dirname(os.path.abspath(__file__))
lang_list = [
        "Python", 
        "Javascript", 
        "Typescript", 
        "C", 
        "C#", 
        "C++", 
        "Java",  
        "Flutter", 
        "Rust",
        "None"]

def submit_button():
    title = title_cb.get()
    name = name_entry.get().title().strip()

    name = title + " " + name

    age = str(age_spin.get())
    gender_num = gender_select.get()
    if gender_num == 1: gender = "Male"
    if gender_num == 2: gender = "Female"
    if gender_num == 3: gender = "Other" 
    #print(name)
    #print(age)
    #print(gender)

    name_entry.delete(0, END)
    age_spin.delete(0, END)
    age_spin.insert(0, 1)
    gender_select.set(0)
    title_cb.set("Pick Your Title")

    #validation checks
    if title == "Pick Your Title":
        change_status_label("Please pick a title!", "red")
        return

    if not name: 
        change_status_label("All of the fields must be filled!", "red")
        return
    
    if gender_num not in [1, 2, 3]:
        change_status_label("You must select a gender", "red")

    lang_choice_list = []

    for i in lang_value_list:
        lang_choice_list.append(i.get())
    #print(lang_choice_list)

    #more validation checks
    if 1 not in lang_choice_list:
        change_status_label("You must select a coding language!", "red")
        return

    if lang_choice_list[-1] == 1 and 1 in lang_choice_list[0:9]:
        change_status_label("You can't select other boxes if you select None!", "red")
        return

    for i in range(len(lang_choice_list)):
        #print(lang_choice_list[i])
        if lang_choice_list[i] == 1:
            lang_choice_list[i] = lang_list[i]
    
    #print(lang_choice_list)
    choices = []
    choices.append(name)
    choices.append(age)
    choices.append(gender)
    
    lang_choice_list = [value for value in lang_choice_list if value != 0]
    choices.append(lang_choice_list)

    #print(choices)

    option_order = ["Name: ", "Age: ", "Gender: "]

    display_info.config(state="normal")
    display_info.delete(0.0, END)
    for i in range(3):
        display_info.insert(END, f"{option_order[i]}{choices[i]}\n")

    display_info.insert(END, "Coding Languages: \n")

    for i in choices[-1]:
        display_info.insert(END, f"\u2022 {i}\n")

    display_info.config(state="disabled")
    if not WRITE_TO_FILE:
        change_status_label("Submition Successful", "green")

    if WRITE_TO_FILE:
        change_status_label("Recorded Result!", "green")

        json_path = script_dir + "\questionnaire_history.json"
        #print(json_path)

        #add to external file
        with open(json_path, "r") as read_file:
            loaded_file = json.load(read_file)
            read_file.close()

        now = datetime.now()
        temp_dict = {str(now):choices}
        loaded_file.update(temp_dict)
        #print(loaded_file)

        with open(json_path, "w") as write_file:
            json.dump(loaded_file, write_file)
            write_file.close()

def change_status_label(text, colour):
    status_label.config(fg=colour)
    status_label.config(text=text)
    status_label.after(4000, lambda: status_label.config(text=""))

header_label = Label(window, text="Questionnaire", font="Calibri 16")
header_label.grid(row=0, column=0, columnspan=2)

title_label = Label(window, text="Title: ", font="Calibri 12")
title_label.grid(row=1, column=0, sticky=W, padx=5, pady=5)

title_select = StringVar()
title_cb = ttk.Combobox(window, textvariable=title_select)
title_cb["values"] = ("Mr", "Mrs", "Ms", "Master", "Dr")
title_cb.grid(row=1, column=1, sticky=E, padx=3)
title_cb.config(state="readonly")
title_cb.set("Pick Your Title")

name_label = Label(window, text="Name: ", font="Calibri 12")
name_label.grid(row=2, column=0, sticky=W, padx=5, pady=5)

name_entry = Entry(window, width=23)
name_entry.grid(row=2, column=1, sticky=E, padx=5)

age_label = Label(window, text="Age: ", font="Calibri 12")
age_label.grid(row=3, column=0, sticky=W, padx=5, pady=5)

age_range = IntVar()
age_spin = Spinbox(window, textvariable=age_range, from_=1, to=100, width=21)
age_spin.grid(row=3, column=1, sticky=E, padx=5)

gender_label = Label(window, text="Gender: ", font="Calibri 12")
gender_label.grid(row=4, column=0, sticky=W, padx=5)

gender_select = IntVar()

gender_radio_button = Radiobutton(window, text="Male", variable=gender_select, value=1) 
gender_radio_button.grid(row=4, column=1, sticky=W)
gender_radio_button = Radiobutton(window, text="Female", variable=gender_select, value=2)
gender_radio_button.grid(row=5, column=1, sticky=W)
gender_radio_button = Radiobutton(window, text="Other", variable=gender_select, value=3)
gender_radio_button.grid(row=6, column=1, sticky=W)

lang_label_1 = Label(window, text="Coding", font="Calibri 12")
lang_label_1.grid(row=8, column=0)

lang_label_2 = Label(window, text="Language: ", font="Calibri 12")
lang_label_2.grid(row=9, column=0)

#dynamically render the checkboxes
grid_values = ["81", "91", "101", "111", "121", "82", "92", "102", "112", "122"]
lang_value_list = []
for i, j in enumerate(lang_list):
    column = grid_values[i][-1]
    row = grid_values[i][0:-1]

    lang_value_list.append(IntVar())
    lang_checkbox = Checkbutton(window, text=j, variable=lang_value_list[i])
    lang_checkbox.grid(row=row, column=column, sticky=W)

submit_button = Button(window, text="Submit", command=submit_button)
submit_button.grid(row=13, column=0, sticky=W, padx=10, pady=10)

status_label = Label(window, text="")
status_label.grid(row=13, column=1, columnspan=2)

display_info = tkscrolled.ScrolledText(window, width=20, height=10, wrap=WORD, state="disabled")
display_info.grid(row=14, column=0, columnspan=2)

window.mainloop()