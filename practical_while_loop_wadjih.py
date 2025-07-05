#Exercise2: Using a "while" Loop.
secret = 8
while True:
    guess = int(input("I heard you were good at guessing, if so, try guessing the secret number I'm currently thinking about: "))
    if guess > secret:
        print("Too high! Try again.")
    elif guess < secret:
        print("Too low! Try again.")
    else:
        print("Congratulations! You've guessed it.")
        break