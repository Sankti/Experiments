print("Please think of a number between 0 and 100!")

low = 0
high = 100
guess = int((low + high) / 2)

print("Is your secret number " + str(guess) + "?")
ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

while ans != "c":
    if ans == "h":
        high = int(guess + guess / 2)
    elif ans == "l":
        low = int(guess / 2)
    else:
        print("Sorry, I did not understand your input.")

    guess = int((low + high) / 2)
    print("Is your secret number " + str(guess) + "?")
    ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

print("Game over. Your secret number was: " + str(guess))
