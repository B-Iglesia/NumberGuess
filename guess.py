import random


guesses=0
def main():
    print("Hello and welcome to the number guessing game.")
    print("This game has three difficulties:")
    print("Easy: You get 5 tries to guess the correct number between 0 and 20")
    print("Medium: You get 3 tries to guess the right number")
    print("Hard: You only get 2 tries to guess the right number")
    diff = input("Would you like to play easy, medium, or hard mode? \n")
    if diff.lower() == "easy":
        guesses = 5
    elif diff.lower() == "medium":
        guesses = 3
    elif diff.lower() == "hard":
        guesses = 2
    else:
        print("defaulted to hard mode  ")
        guesses = 2
    number = random.randint(0,20)
    while guesses > 0:
        guess = input("Guess a number:")
        if int(guess) < number:
            print("Higher!")
        if int(guess) > number:
            print("Lower")
        if int(guess) == number:
            break
        guesses-=1
    if int(guess) == number:
        print("You've won congratulations!")
    else: 
        print("You've lost! It was", number)
    
if __name__=='__main__':
    main()