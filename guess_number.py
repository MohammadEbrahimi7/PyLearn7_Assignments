import random

computer_number = random.randint(10, 30)
for i in range(10):
    user_number = int(input("enter your number: "))

    if computer_number == user_number:
        print("you win")
        print("🎉")
        print("guesses:", i + 1)
        break

    elif computer_number > user_number:
        print("go up")

    elif computer_number < user_number:
        print("g down")