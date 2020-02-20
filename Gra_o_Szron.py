from tkinter import *

# GUI SETUP

root = Tk()
root.geometry("480x480")

# DEFINING FUNCTIONS 1

count = 0
score = 0

def answer(arg):
    global count
    global score
    if count == 0:
        write("\n")
        write("\n    ----- Przypadek 1 -----")
        write("\nTemperatura o godz. 16:00:    10 °C")
        write("\nTemperatura punktu rosy:      -6 °C")
        write("\nZachmurzenie:                 brak")
        write("\nWiatr:                        lekki")
        write("\n")
        write("\n")
        write("\n")
        write("\n")
        write("\n")
        write("Jakie jest prawdopodobieństwo wystąpienia szronu?")
        count += 1

    elif count == 1:
        if arg == "h":
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\nDobra odpowiedź!")
            write("\nOtrzymujesz 1 punkt.")
            write("\nKliknij jakikolwiek przycisk, aby kontynuować.")
            score += 1
        else:
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\nZła odpowiedź!")
            write("\nKliknij jakikolwiek przycisk, aby kontynuować.")
        count += 1

    elif count == 2:
        write("\n")
        write("\n    ----- Przypadek 2 -----")
        write("\nTemperatura o godz. 16:00:    10 °C")
        write("\nTemperatura punktu rosy:      8 °C")
        write("\nZachmurzenie:                 ???")
        write("\nWiatr:                        ???")
        write("\n")
        write("\n")
        write("\n")
        write("\n")
        write("\n")
        write("Jakie jest prawdopodobieństwo wystąpienia szronu?")
        count += 1

    elif count == 3:
        if arg == "l":
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\nDobra odpowiedź!")
            write("\nOtrzymujesz 1 punkt.")
            write("\nKliknij jakikolwiek przycisk, aby kontynuować.")
            score += 1
        else:
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\nZła odpowiedź!")
            write("\nKliknij jakikolwiek przycisk, aby kontynuować.")
        count += 1

    elif count == 4:
        write("\n")
        write("\n    ----- Przypadek 3 -----")
        write("\nTemperatura o godz. 16:00:    10 °C")
        write("\nTemperatura punktu rosy:      1,5 °C")
        write("\nZachmurzenie:                 brak")
        write("\nWiatr:                        silny")
        write("\n")
        write("\n")
        write("\n")
        write("\n")
        write("\n")
        write("Jakie jest prawdopodobieństwo wystąpienia szronu?")
        count += 1

    elif count == 5:
        if arg == "h":
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\nDobra odpowiedź!")
            write("\nOtrzymujesz 1 punkt.")
            write("\nKliknij jakikolwiek przycisk, aby kontynuować.")
            score += 1
        else:
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\nZła odpowiedź!")
            write("\nKliknij jakikolwiek przycisk, aby kontynuować.")
        count += 1

    elif count == 6:
        write("\n")
        write("\n    ----- Przypadek 4 -----")
        write("\nTemperatura o godz. 16:00:    10 °C")
        write("\nTemperatura punktu rosy:      1 °C")
        write("\nZachmurzenie:                 ???")
        write("\nWiatr:                        brak")
        write("\n")
        write("\n")
        write("\n")
        write("\n")
        write("\n")
        write("Jakie jest prawdopodobieństwo wystąpienia szronu?")
        count += 1

    elif count == 7:
        if arg == "d":
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\nDobra odpowiedź!")
            write("\nOtrzymujesz 1 punkt.")
            write("\nKliknij jakikolwiek przycisk, aby kontynuować.")
            score += 1
        else:
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\nZła odpowiedź!")
            write("\nKliknij jakikolwiek przycisk, aby kontynuować.")
        count += 1

    elif count == 8:
        write("\n")
        write("\n    ----- Przypadek 5 -----")
        write("\nTemperatura o godz. 16:00:    8 °C")
        write("\nTemperatura punktu rosy:      4 °C")
        write("\nZachmurzenie:                 duże")
        write("\nWiatr:                        brak")
        write("\n")
        write("\n")
        write("\n")
        write("\n")
        write("\n")
        write("Jakie jest prawdopodobieństwo wystąpienia szronu?")
        count += 1

    elif count == 9:
        if arg == "l":
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\nDobra odpowiedź!")
            write("\nOtrzymujesz 1 punkt.")
            write("\nKliknij jakikolwiek przycisk, aby kontynuować.")
            score += 1
        else:
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\nZła odpowiedź!")
            write("\nKliknij jakikolwiek przycisk, aby kontynuować.")
        count += 1

    elif count == 10:
        if score < 2:
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n    ----- Końcowa Ocena -----")
            write("\nZdobyłeś " + str(score) + " z 5 możliwych punktów.")
            write("\nKiepski z ciebie meteorolog. Następnym razem zadzwonimy do kogoś innego.")
            write("\n")
            write("\nKliknij jakikolwiek przycisk, aby spróbować jeszcze raz!")
        elif 2 <= score <= 4:
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n    ----- Końcowa Ocena -----")
            write("\nZdobyłeś " + str(score) + " z 5 możliwych punktów.")
            write("\nRównie dobrze moglibyśmy wróżyć z fusów. Następnym razem zadzwonimy do kogoś innego.")
            write("\n")
            write("\nKliknij jakikolwiek przycisk, aby spróbować jeszcze raz!")
        else:
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n")
            write("\n    ----- Końcowa Ocena -----")
            write("\nZdobyłeś " + str(score) + " z 5 możliwych punktów.")
            write("\nWspaniała robota! Świetny z ciebie meteorolog. Na pewno odezwiemy się ponownie!")
            write("\n")
            write("\nKliknij jakikolwiek przycisk, aby zagrać jeszcze raz!")
        count = 0
        score = 0
        

# GUI ELEMENTS SETUP

left = Frame(root, borderwidth=2, relief="solid", background="gainsboro")
right = Frame(root, borderwidth=2, relief="solid", background="gainsboro")
left_con = Frame(left, borderwidth=2, relief="solid", background="azure")
right_con = Frame(right, borderwidth=2, relief="solid", background="azure")

title = Label(left_con, text="Gra o Szron", fg="black", font=("Book Antiqua", 24), background="azure")
undertitle = Label(left_con, text="Nadchodzi okres przymrozkowy...", fg="black", font=("Verdana", 10), background="azure")

message_box = Text(left_con, width=48, height=12, wrap=WORD, fg="black", font=("Courier New", 10))
message_box.config(state=DISABLED)

button_high = Button(right_con, text="Wysokie", background="gray", fg="white", font=("Courier New", 12, "bold"), command=lambda: answer("h"))
button_low = Button(right_con, text="Niskie", background="gray", fg="white", font=("Courier New", 12, "bold"), command=lambda: answer("l"))
button_data = Button(right_con, text="Za mało danych", background="gray", fg="white", font=("Courier New", 12, "bold"), command=lambda: answer("d"))

# DEFINING FUNCTIONS 2

def write(string):
    message_box.config(state=NORMAL)
    message_box.insert("end", string)
    message_box.see("end")
    message_box.config(state=DISABLED)

# LAYOUT SETUP

left.pack(side="top", expand=True, fill="both")
right.pack(side="bottom", expand=True, fill="both")
left_con.pack(expand=True, fill="both", padx=5, pady=5)
right_con.pack(expand=True, fill="both", padx=5, pady=5)

title.pack(padx=10, pady=10)
undertitle.pack()
message_box.pack(padx=10, pady=10)

button_high.grid(column=0, row=0, padx=10, pady=10)
button_low.grid(column=1, row=0, padx=10, pady=10)
button_data.grid(column=2, row=0, padx=10, pady=10)

write("    Witaj!")
write("\n    Rada Meteorologiczna zawezwała najlepszych meteorologów, aby sporządzić predykcję wystąpienia szronu w prowincji!")
write("\n    Jesteś jedyną osobą, która zgodziła się pomóc!")
write("\n    Twoim zadaniem jest określenie prawdopodobieństwa wystąpienia szronu na podstawie dostarczonych ci danych!")
write("\n    Kliknij jakikolwiek przycisk, aby rozpocząć.")

# COMMENCING LOOP

root.mainloop()
