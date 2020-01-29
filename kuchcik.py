from tkinter import *
from random import randint
import time

# GUI SETUP

root = Tk()
root.geometry("640x480")

# GUI ELEMENTS SETUP

left = Frame(root, borderwidth=2, relief="solid", background="gainsboro")
right = Frame(root, borderwidth=2, relief="solid", background="gainsboro")
left_con = Frame(left, borderwidth=2, relief="solid", background="azure")
right_con = Frame(right, borderwidth=2, relief="solid", background="azure")

title = Label(left_con, text="Kuchcik Adam", fg="black", font=("Book Antiqua", 24), background="azure")
undertitle = Label(left_con, text="Twój Asystent Kuchenny", fg="black", font=("Verdana", 10), background="azure")

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
undertitle.pack()
message_box.pack(padx=10, pady=10)

greet1 = "To wspaniały dzień na gotowanie!"
greet2 = "Wyglądasz dziś fenomenalnie!"
greet3 = "To jest twój dzień i twój obiad!"
greet4 = "Wyglądasz na kogoś, kto chciałby dziś dobrze zjeść!"
greet5 = "Podoba mi się twoja fryzura!"
greet6 = "Naczynia umyte? Zaraz sie przydadzą!"
greet7 = "Czas trochę pohałasować w kuchni!"
greet8 = "Czas poobijać nieco garnki!"
greet9 = "Czas poćwiatrować kilka połci mięsa!"



write("Witaj!")

# COMMENCING LOOP

root.mainloop()
