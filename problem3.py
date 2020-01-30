s = 'azcbobobegghakl'

alphabet = 'abcdefghijklmnopqrstuvwxyz'

current_index = 0
last_letter = None
current_letter = s[current_index]
next_letter = s[current_index + 1]
avar = current_letter
string = ""
guesses = []

for letter in s:
    if current_index > 0:
        last_letter = s[current_index - 1]
    print("cur:" + str(current_index) + str(last_letter) + str(current_letter) + str(next_letter))

    if next_letter >= current_letter:
        avar = avar + next_letter
        if len(avar) > len(string):
            string = avar
    elif next_letter < current_letter:
        string = ""
        avar = current_letter

    current_index += 1
    if current_index < len(s):
        current_letter = s[current_index]
    if current_index < len(s) - 1:
        next_letter = s[current_index + 1]
    else:
        next_letter = ""
    print("String: " + string)
    print("Avarse: " + avar)
