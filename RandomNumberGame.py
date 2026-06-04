import random 

secret_number = random.randint(1, 10)

print("Welcome to the Number Guessing Game!")
print("I have chosen one secret number between 1 and 10. Can you guess it?")

while True:
    guess = input("Enter your guess: ")
    
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue
    
    guess = int(guess)
    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the secret number!")
        break