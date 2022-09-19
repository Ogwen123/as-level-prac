
from tkinter import *
import json
import os

window = Tk()
window.title("Flash Card Program - CPU Components")
window.geometry("550x400")
window.configure(bg="white")

text_data = [
    "The ALU is the Arithmetic Logic Unit. It is the part of the cpu that handles mathematic and logical operations. It is the part that does the execute stage of the fetch-decode-execute cycle.", 
    "Cache is extremely fast memory in the CPU that acts as an intermediary to stop bottlenecking from the slow, reletive to the CPU's speed, speed of the RAM. It stores recent and frequently used instructions.", 
    "There are 5 Registers in the CPU. They are the Program Counter, Accumulator, Memory Address Register, Memory Data Register and Current Instruction Register. Registers hold important information during the fetch-decode-execute cycle.", 
    "The control unit controls the rest of the PC components and does the decode stage of the fetch-decode-execute cycle."
    ]

name_data = [
    "ALU",
    "Cache",
    "Registers",
    "CU"
]

def button_click(type):
    text1.config(state="normal")#allows the text bow to be changed
    text1.delete(0.0, END)
    text1.insert(END, text_data[type])
    text1.config(state="disabled")#makes the text box read only so it cannot be edited in the GUI

#dynamically load the buttons
for i in range(len(text_data)):
    button_card = Button(
        window,
        width=8,
        text=name_data[i],
        bg="white",
        highlightcolor="black", 
        highlightthickness=2,
        command=lambda i=i: button_click(i)
    )
    button_card.grid(row=i, column=0, sticky=NW, padx=(5, 0))

text1 = Text(
    window, 
    bg="white", 
    width=50,
    highlightcolor="black", 
    wrap=WORD,
    highlightthickness=1)
text1.grid(row=0, column=1, rowspan=4, sticky=E, padx=(55, 10))

button_click(0)

window.mainloop()

# The ALU is the Arithmetic Logic Unit. It is the part of the cpu that handles mathematic and logical operations. It is the part that does the execute stage of the fetch-decode-execute cycle.
# Cache is extremely fast memory in the CPU that acts as an intermediary to stop bottlenecking from the slow, reletive to the CPU's speed, speed of the RAM. It stores recent and frequently used instructions.
# There are 5 Registers in the CPU. They are the Program Counter, Accumulator, Memory Address Register, Memory Data Register and Current Instruction Register. Registers hold important information during the fetch-decode-execute cycle.
# The control unit controls the rest of the PC components and does the decode stage of the fetch-decode-execute cycle.