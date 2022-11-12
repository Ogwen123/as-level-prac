from tkinter import *
from tkinter import scrolledtext as tkscrolled
import json
from datetime import datetime
import os
from tkinter import ttk

window = Tk()
window.title("Questionnaire")
window.resizable(False, False)

current_info_tracker = 0

script_dir = os.path.dirname(os.path.abspath(__file__))
lang_list = [#before the first comma is the coding langauge name, between the commas is the row, after the last comma is the column
        "Python,8,1", 
        "Javascript,9,1", 
        "Typescript,10,1",
        "C,11,1", 
        "C#,12,1", 
        "C++,8,2", 
        "Java,9,2",  
        "Flutter,10,2", 
        "Rust,11,2",
        ]

def get_info():#a single function to get all of the data from the inputs and return it as a list
    title = title_cb.get()#get data from title combobox
    name = name_entry.get().title().strip()#get data from name entry

    name = title + " " + name

    age = age_spin.get()#get data from age spinbox
    gender_var = gender_select.get()#get data from gender radio boxes
    if gender_var == 1: gender = "Male"
    if gender_var == 2: gender = "Female"
    if gender_var == 3: gender = "Other" 

    #reset all of the inputs
    name_entry.delete(0, END)
    age_spin.delete(0, END)
    age_spin.insert(0, 1)
    gender_select.set(0)
    title_cb.set("Pick Your Title")

    lang_choice_list = []

    for i in lang_value_list:
        lang_choice_list.append(i.get())
        i.set(0)#reset the language options

    #validation checks
    if title == "Pick Your Title":#check that a title has been selected
        change_status_label("Please pick a title!", "red")
        return "validation failed"

    if not name:#check that a name has been entered
        change_status_label("All of the fields must be filled!", "red")
        return "validation failed"
    
    if len(name) > 50:#check that name is the write length due to the way the data is stored in the file
        max_name_len = 50 - len(title + " ")
        change_status_label(f"Name cannot be more that {str(max_name_len)} characters", "red")
        return "validation failed"

    try:
        age = int(age)#make sure the age in not a string, otherwise there will be alot of issues
    except ValueError:
        change_status_label("Age must be an integer!", "red")
        return

    if gender_var not in [1, 2, 3]:#check that a gender has been entered
        change_status_label("You must select a gender", "red")
        return  "validation failed"

    if 1 not in lang_choice_list:#check that either a coding language has been selected or the none box has been selected
        change_status_label("You must select a coding language!", "red")
        return "validation failed"

    if lang_choice_list[-1] == 1 and 1 in lang_choice_list[0:9]:#make sure that if the none box has been selected no other box has been selected
        change_status_label("You can't select other boxes if you select None!", "red")
        return "validation failed"

    for i in range(len(lang_choice_list)):#replace all the 1s in the choice list with the actual name of the language
        #print(lang_choice_list[i])
        if lang_choice_list[i] == 1:
            try:
                lang_choice_list[i] = lang_list[i].split(",")[0]
            except IndexError:
                lang_choice_list[i] = "None"
    
    #print(lang_choice_list)
    choices = []
    choices.append(name)
    choices.append(age)
    choices.append(gender)
    
    lang_choice_list = [value for value in lang_choice_list if value != 0]#wtf is this, absolutely digusting, it loops through the last and only adds ones that are not 0, therefore have to be 1

    choices.append(lang_choice_list)
    return choices#list format: name with title, age , gender, list of programming languages

def submit_func(choices):

    if choices == "validation failed":
        return

    option_order = ["Name: ", "Age: ", "Gender: "]

    display_info.config(state="normal")
    display_info.delete(0.0, END)
    for i in range(3):
        display_info.insert(END, f"{option_order[i]}{choices[i]}\n")

    display_info.insert(END, "Coding Languages: \n")

    for i in choices[-1]:
        display_info.insert(END, f"\u2022 {i}\n")

    display_info.config(state="disabled")
    change_status_label("Submission Succesful", "green")

def save_button():
    choices = get_info()

    submit_func(choices)

    if choices == "validation failed":
        return

    formatted_name = choices[0].ljust(50)
    formatted_age = choices[1].ljust(50)
    formatted_gender = choices[2].ljust(50)

    str_lang_list = str(choices[-1])
    str_lang_list = str_lang_list.replace("[", "")
    str_lang_list = str_lang_list.replace("]", "")
    str_lang_list = str_lang_list.replace("'", "")
    formatted_langs = str_lang_list

    write_list = formatted_name + formatted_age + formatted_gender + formatted_langs + "\n"

    print(write_list)

    with open(script_dir + "/submissions.txt", "a") as read_file:
        read_file.write(write_list)

    change_status_label("Saved To File", "green")

def display_previous_results(direction):
    global current_info_tracker    

    #get info from file
    past_results = ""
    with open(script_dir + "/submissions.txt", "r") as read_file:
        past_results = read_file.read()

        past_results = past_results.split("\n")
    
    
    if direction == "left":
        if current_info_tracker == len(past_results)-1:
            change_status_label("No more results to display!", "red")
            return
        current_info_tracker += 1
    elif direction == "right":
        if current_info_tracker-1 <= 0:
            change_status_label("No more results to display!", "red")
            display_info.delete(0.0, END)
            if current_info_tracker == 1: change_tracker_label(f"Current Result: {current_info_tracker-1}")
            current_info_tracker = 0
            return
        
        current_info_tracker -= 1

    change_tracker_label(f"Current Result: {current_info_tracker}")


    del past_results[-1]#remove last item which is always empty

    #load info into list
    results = []

    list_index = current_info_tracker-1
    past_results.reverse()#reverse list so most recent results are first
    results.append(past_results[list_index][0:50])
    results.append(past_results[list_index][50:100])
    results.append(past_results[list_index][100:150])
    langs = past_results[list_index][150:]
    langs_list = langs.split(",")
    langs_list[-1] = langs_list[-1].strip()
    results.append(langs_list)

    print(results)

    display_info.config(state="normal")
    display_info.delete(0.0, END)

    for i in range(3):
        display_info.insert(END, results[i])
    
    display_info.insert(END, "Coding Languages: \n")

    for i in results[-1]:
        display_info.insert(END, f"\u2022 {i}\n")


def change_status_label(text, colour):
    status_label.config(fg=colour)
    status_label.config(text=text)
    status_label.after(4000, lambda: status_label.config(text=""))

def change_tracker_label(text, colour="black"):
    tracker_label.config(fg=colour)
    tracker_label.config(text=text)

header_label = Label(window, text="Questionnaire", font="Calibri 16")
header_label.grid(row=0, column=0, columnspan=3)

title_label = Label(window, text="Title: ", font="Calibri 12")
title_label.grid(row=1, column=0, sticky=W, padx=5, pady=5)

title_select = StringVar()
title_cb = ttk.Combobox(window, textvariable=title_select)
title_cb["values"] = ("Mr", "Mrs", "Ms", "Master", "Dr", "Sir", "Madame")
title_cb.grid(row=1, column=1, sticky=E, padx=3)
title_cb.config(state="readonly")
title_cb.set("Pick Your Title")

name_label = Label(window, text="Full Name: ", font="Calibri 12")
name_label.grid(row=2, column=0, sticky=W, padx=5, pady=5)

name_entry = Entry(window, width=23)
name_entry.grid(row=2, column=1, sticky=E, padx=5)

age_label = Label(window, text="Age: ", font="Calibri 12")
age_label.grid(row=3, column=0, sticky=W, padx=5, pady=5)

max_age = (datetime.today().year) - (1903)

age_range = IntVar()
age_spin = Spinbox(window, textvariable=age_range, from_=1, to=max_age, width=21)
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
lang_value_list = []
column_one_highest = 0
column_two_highest = 0
for i, j in enumerate(lang_list):
    column = int(j.split(",")[-1])
    row = int(j.split(",")[-2])
    
    if column == 1 and row > column_one_highest:
        column_one_highest = row
    if column == 2 and row > column_two_highest:
        column_two_highest = row


    lang_value_list.append(IntVar())
    lang_checkbox = Checkbutton(window, text=j.split(",")[0], variable=lang_value_list[i])
    lang_checkbox.grid(row=row, column=column, sticky=W, padx=(0, 20))

n = 0#variable for tracking the highest row value
for i in lang_list:
    try:
        row = int(i.split(",")[-2])
    except ValueError:
        print("the row wasn't a number")
    
    if row > n:
        n=row

none_column = 0
none_row = 0
if column_one_highest > column_two_highest:
    none_column = 2
    none_row = n
    n += 1
elif column_one_highest == column_two_highest:
    none_column = 1
    none_row = n+1
    n +=1
elif column_two_highest > column_one_highest:
    none_column = 1
    none_row = n
    n += 1

lang_value_list.append(IntVar())
none_checkbox = Checkbutton(window, text="None", variable=lang_value_list[-1])
none_checkbox.grid(row=none_row, column=none_column, sticky=W)


submit_button = Button(window, text="Submit", command=lambda: submit_func(get_info()), bg="#87AE73")
submit_button.grid(row=n+1, column=0, sticky=W, padx=10, pady=10)

save_button = Button(window, text="Save To File", command=save_button, bg="#87AE73")
save_button.grid(row=n+1, column=1, sticky=W, )

left_button = Button(window, text="❰", command=lambda: display_previous_results("left"), bg="#FDFD96")
left_button.grid(row=n+2, column=0, sticky=W, padx=(10, 0))

right_button = Button(window, text="❱", command=lambda: display_previous_results("right"), bg="#FDFD96")
right_button.grid(row=n+2, column=0, padx=25, sticky=W)

tracker_label = Label(window, text="Current Result: 0")
tracker_label.grid(row=n+2, column=1)

status_label = Label(window, text="")
status_label.grid(row=n+3, column=0, columnspan=3)

display_info = tkscrolled.ScrolledText(window, width=20, height=10, wrap=WORD, state="disabled")
display_info.grid(row=n+4, column=0, columnspan=2, pady=(0, 10), sticky=W, padx=10)

window.mainloop()