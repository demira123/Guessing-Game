import random
number = random.randint(1,9)

chances = 0

print("Guess a number in between 1 to 9")

while chances < 5:

    guess = int(input("Enter the number : "))
    
    if guess == number:
        print("Congratulations! You Won!")
        break

    elif guess < number :
        print("Your guess is too low!!")

    elif guess > number :
        print("Your guess is too high!!")

    chances += 1

    
if not chances < 5:
    print("You Lose! The number is", number)
