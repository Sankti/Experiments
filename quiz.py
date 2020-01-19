name = "Victor Hugo"
date = "26.02.1802"
question = f"What is {name}\'s date of birth?"

print(question)
answer = input(question + " ")

print(bool(answer == date))