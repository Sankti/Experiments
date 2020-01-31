s = 'zyxwvutsrqponmlkjihgfedcba'

current_index = 0
current_letter = s[current_index]
next_letter = s[current_index + 1]
avar = current_letter
string = ""
guesses = []
test = True

for letter in s:
    current_treble = str(letter) + str(next_letter)
    if next_letter >= letter:
        if test == False:
            avar = avar + str(letter) + str(next_letter)
        else:
            avar = avar + str(next_letter)
        test = str(len(avar) > len(string))
        if len(avar) > len(string):
            string = avar
    else:
        avar = next_letter
    current_index += 1
    if current_index < len(s) - 1:
        next_letter = s[current_index + 1]
    else:
        next_letter = ""
    if string == "":
        string = letter
print("Longest substring in alphabetical order is: " + string)
