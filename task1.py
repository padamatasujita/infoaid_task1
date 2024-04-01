import random

def play_game():
    number = random.randint(1, 100)
    attempts = 0

    name=input("Enter your name to start the Game:")

    print(f"Welcome, {name}, to the Number Guessing Game!")
    
    print("Rules of the Game are:")
    print("I think of a number and you have to guess the number within 10 attempts")


    while attempts < 10:
        guess = int(input("Take a guess: "))
        attempts += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Congratulations! You found the number in {attempts} attempts.")
            break

    if attempts == 10:
          print(f"Sorry, {name}. You've reached the maximum number of attempts. The correct number was {number}.")
        
    play_again = input("Do you want to play again? (yes/no): ")

    if play_again.lower() == "yes":
        play_game()
    else:
        print("Thank you for playing!")

play_game()
