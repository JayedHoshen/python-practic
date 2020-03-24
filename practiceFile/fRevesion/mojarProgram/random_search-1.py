import random

number = random.randint(1,1000)
attempts = 0

while True:
    input_number = input("Guess the number (between 1 and 1000):")
    input_number = int(input_number)
    attempts +=1

    if input_number == number:
        print("Yes, your guess is correct!")
        break
    if input_number > number:
        print("Incorrect! Please try to guess a smaller number.")
    else:
        print("Incorrect! Please try to guess a larger number.")
print("You tried",attempts,"times to find the correct number.")
