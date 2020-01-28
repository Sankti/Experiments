from tkinter import *
import time

# GUI SETUP

root = Tk()
root.geometry("640x480")

# GUI ELEMENTS SETUP

left = Frame(root, borderwidth=2, relief="solid", background="gainsboro")
right = Frame(root, borderwidth=2, relief="solid", background="gainsboro")
left_con = Frame(left, borderwidth=2, relief="solid", background="azure")
right_con = Frame(right, borderwidth=2, relief="solid", background="azure")


title = Label(left_con, text="Kuchcik Adam", fg="black", font=("Times New Roman", 24), background="azure")


message_box = Text(right_con, width=24, height=8, wrap=WORD, fg="black", font=("Courier New", 10))
message_box.config(state=DISABLED)

# DEFINING FUNCTIONS

def write(string):
    message_box.config(state=NORMAL)
    message_box.insert("end", string)
    message_box.see("end")
    message_box.config(state=DISABLED)

# LAYOUT SETUP

left.pack(side="left", expand=True, fill="both")
right.pack(side="right", expand=True, fill="both")
left_con.pack(expand=True, fill="both", padx=5, pady=5)
right_con.pack(expand=True, fill="both", padx=5, pady=5)

title.pack(padx=10, pady=10)
message_box.pack(padx=10, pady=10)

# COMMENCING LOOP

root.mainloop()