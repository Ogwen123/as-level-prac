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

def submit_button():
    title = title_cb.get()
    name = name_entry.get().title().strip()

    name = title + " " + name

    age = str(age_spin.get())
    gender = gender_select.get()
    if gender == 0: gender = "Male"
    if gender == 1: gender = "Female"
    if gender == 2: gender = "Other" 
    #print(name)
    #print(age)
    #print(gender)

    name_entry.delete(0, END)
    age_spin.delete(0, END)
    age_spin.insert(0, 1)
    gender_select.set(0)
    title_cb.set("Pick Your Title")

    #validation checks
    if not name: 
        change_status_label("All of the fields must be filled!", "red")
        return
    
    if title == "Pick Your Title":
        change_status_label("Please pick a title!", "red")
        return

    lang_choice_list = []
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

    choice1 = var1.get()
    lang_1.deselect()
    lang_choice_list.append(choice1)

    choice2 = var2.get()
    lang_choice_list.append(choice2)
    lang_2.deselect()

    choice3 = var3.get()
    lang_choice_list.append(choice3)
    lang_3.deselect()

    choice4 = var4.get()
    lang_choice_list.append(choice4)
    lang_4.deselect()

    choice5 = var5.get()
    lang_choice_list.append(choice5)
    lang_5.deselect()

    choice6 = var6.get()
    lang_choice_list.append(choice6)
    lang_6.deselect()

    choice7 = var7.get()
    lang_choice_list.append(choice7)
    lang_7.deselect()

    choice8 = var8.get()
    lang_choice_list.append(choice8)
    lang_8.deselect()

    choice9 = var9.get()
    lang_choice_list.append(choice9)
    lang_9.deselect()

    choice10 = var10.get()
    lang_choice_list.append(choice10)
    lang_10.deselect()


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

gender_radio_button = Radiobutton(window, text="Male", variable=gender_select, value=0) 
gender_radio_button.grid(row=4, column=1, sticky=W)
gender_radio_button = Radiobutton(window, text="Female", variable=gender_select, value=1)
gender_radio_button.grid(row=5, column=1, sticky=W)
gender_radio_button = Radiobutton(window, text="Other", variable=gender_select, value=2)
gender_radio_button.grid(row=6, column=1, sticky=W)

lang_label_1 = Label(window, text="Coding", font="Calibri 12")
lang_label_1.grid(row=8, column=0)

lang_label_2 = Label(window, text="Language: ", font="Calibri 12")
lang_label_2.grid(row=9, column=0)

var1 = IntVar()
lang_1 = Checkbutton(window, text="Python", variable=var1)
lang_1.grid(row=8, column=1, sticky=W)

var2 = IntVar()
lang_2 = Checkbutton(window, text="Javascript", variable=var2)
lang_2.grid(row=9, column=1, sticky=W)

var3 = IntVar()
lang_3 = Checkbutton(window, text="Typescript", variable=var3)
lang_3.grid(row=10, column=1, sticky=W)

var4 = IntVar()
lang_4 = Checkbutton(window, text="C", variable=var4)
lang_4.grid(row=11, column=1, sticky=W)

var5 = IntVar()
lang_5 = Checkbutton(window, text="C#", variable=var5)
lang_5.grid(row=12, column=1, sticky=W)

var6 = IntVar()
lang_6 = Checkbutton(window, text="C++", variable=var6)
lang_6.grid(row=8, column=2, sticky=W)

var7 = IntVar()
lang_7 = Checkbutton(window, text="Java", variable=var7)
lang_7.grid(row=9, column=2, sticky=W)

var8 = IntVar()
lang_8 = Checkbutton(window, text="Flutter", variable=var8)
lang_8.grid(row=10, column=2, sticky=W)

var9 = IntVar()
lang_9 = Checkbutton(window, text="Rust", variable=var9)
lang_9.grid(row=11, column=2, sticky=W)

var10 = IntVar()
lang_10 = Checkbutton(window, text="None", variable=var10)
lang_10.grid(row=12, column=2, sticky=W)

submit_button = Button(window, text="Submit", command=submit_button)
submit_button.grid(row=13, column=0, sticky=W, padx=10, pady=10)

status_label = Label(window, text="")
status_label.grid(row=13, column=1, columnspan=2)

display_info = tkscrolled.ScrolledText(window, width=20, height=10, wrap=WORD, state="disabled")
display_info.grid(row=14, column=0, columnspan=2)

window.mainloop()