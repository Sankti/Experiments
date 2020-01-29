s = 'azcbobobegghakl'

current_letter = 0
range_letters = 0
count = 0

for letter in s:
    current_letter += 1
    range_letters = current_letter + 2
    while letter == "b":
        if range(current_letter, range_letters) == "bob":
            count += 1

print("Number of times bob occurs is: " + str(count))
