from tkinter import *

window = Tk()
window.title("Plumbers")
window.geometry("250x200")
#window.resizable(False, False)

header_label = Label(window, text="Plumbers", font="16")
header_label.grid(row=0, column=0, columnspan=3)

id_entry_label = Label(window, text="Plumber ID")
id_entry_label.grid(row=1, column=0, sticky=W)

id_entry = Entry(window)
id_entry.grid(row=1, column=1, sticky=W, columnspan=2)

firstname_entry_label = Label(window, text="Firstname")
firstname_entry_label.grid(row=2, column=0, sticky=W)

firstname_entry = Entry(window)
firstname_entry.grid(row=2, column=1, sticky=W, columnspan=2)

surname_entry_label = Label(window, text="Surname")
surname_entry_label.grid(row=3, column=0, sticky=W)

surname_entry = Entry(window)
surname_entry.grid(row=3, column=1, sticky=W, columnspan=2)

gas_safe_label = Label(window, text="Gas Safe?")
gas_safe_label.grid(row=4, column=0, sticky=W)

gas_safe_select = IntVar()
gas_safe_radio = Radiobutton(window, text="Yes", variable=gas_safe_select, value=1)
gas_safe_radio.grid(row=4, column=1, sticky=W)
gas_safe_radio = Radiobutton(window, text="No", variable=gas_safe_select, value=2)
gas_safe_radio.grid(row=4, column=2, sticky=W)

window.mainloop()