s = 'azcbobobegghakl'

current_letter = 0
range_letters = 0
count = 0

for letter in s:
    range_letters = current_letter + 3
    print(s[current_letter:range_letters])
    if s[current_letter:range_letters] == "bob":
        count += 1
    current_letter += 1

print("Number of times bob occurs is: " + str(count))
