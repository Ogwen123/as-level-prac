#cpu components
#alu, registers, cache, control unit

from tkinter import *
import json
import os

window = Tk()
window.title("Flash Card Program - CPU Components")
window.geometry("600x450")
window.configure(bg="white")

# The ALU is the Arithmetic Logic Unit. It is the part of the cpu that handles mathematic and logical operations. It is the part that does the execute stage of the fetch-decode-execute cycle.
# Cache is extremely fast memory in the CPU that acts as an intermediary to stop bottlenecking from the slow, reletive to the CPU's speed, speed of the RAM. It stores recent and frequently used instructions.
# There are 5 Registers in the CPU. They are the Program Counter, Accumulator, Memory Address Register, Memory Data Register and Current Instruction Register. Registers hold important information during the fetch-decode-execute cycle.
# The control unit controls the rest of the PC components and does the decode stage of the fetch-decode-execute cycle.

current_text = ""
script_dir = os.path.dirname(os.path.abspath(__file__))

with open(script_dir + "/flashcards.json", "r") as flashcard_data:
        text_data = json.load(flashcard_data)


def reload_json():
    with open(script_dir + "/flashcards.json", "r") as flashcard_data:
        global text_data
        text_data = json.load(flashcard_data)

    
def edit_button():
    if text1["state"] == "normal":#locking the card
        text1.config(state="disabled")
        button_edit.config(text="Edit Card")
        update_json()
    elif text1["state"] == "disabled":#making the card editable
        text1.config(state="normal")
        button_edit.config(text="Lock Card")


def lock_edit():
    text1.config(state="disabled")
    button_edit.config(text="Edit Card")


def update_json():
    with open(script_dir + "/flashcards.json", "r") as json_file:
        temp_text_data = json.load(json_file)
        temp_text_data[current_text]["text"] = text1.get(0.0, END)
        json.dump(temp_text_data, open(script_dir + "/flashcards.json", "w"), indent=4)
    reload_json()


def change_text(type):
    text1.config(state="normal")#allows the text bow to be changed
    text1.delete(0.0, END)
    text1.insert(END, text_data[type]["text"])
    text1.config(state="disabled")#makes the text box read only so it cannot be edited in the GUI


def button_click(type):
    global current_text
    #print(text1.get(0.0, END))
    #print(text_data[type]["text"])
    #print(type)
    if text1.get(0.0, END).strip() == text_data[current_text]["text"].strip():
        current_text = type
        print("same")
        change_text(type)
    else:
        print("diff")
        update_json()
        current_text = type
        change_text(type)
        if text1["state"] == "disabled":
            lock_edit()

    

text1 = Text(
    window, 
    bg="white", 
    width=50,
    highlightcolor="black", 
    wrap=WORD,
    highlightthickness=1)
text1.grid(row=0, column=1, rowspan=3, sticky=E, padx=(100, 10))

#dynamically load the buttons
for i in range(len(text_data)):
    button_card = Button(
        window,
        width=8,
        text=text_data[i]["name"],
        bg="white",
        highlightcolor="black", 
        highlightthickness=2,
        command=lambda i=i: button_click(i)
    )
    button_card.grid(row=i, column=0, sticky=NW)

button_edit = Button(
    window,
    width = 10,
    text = "Edit Card",
    bg="white",
    highlightcolor="black", 
    highlightthickness=2,
    command=lambda: edit_button()
)
button_edit.grid(row=3, column=1)

text1.insert(END, text_data[0]["text"])
text1.config(state="disabled")
current_text=0

window.mainloop()