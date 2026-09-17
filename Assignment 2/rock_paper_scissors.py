import random

computer_score = 0
user_score = 0

x = random.randint(1, 3)

if x == 1:
   computer_choice = "rock"
elif x == 2:
   computer_choice = "paper"
elif x == 3:
   computer_choice = "scissors"
   
user_choice = input("enter your choise: ")


print("computer choice: ", computer_choice)


if computer_choice == "rock" and user_choice == "paper":
   user_choice = user_score + 1

elif computer_choice == "rock" and user_choice == "scissors":
   computer_choice = computer_score + 1

elif computer_choice == "rock" and user_choice == "rock":
   computer_score = user_score

elif computer_choice == "paper" and user_choice == "rock":
   computer_choice = computer_score + 1

elif computer_choice == "paper" and user_choice == "scissors":
   computer_choice = computer_score + 1

elif computer_choice == "paper" and user_choice == "paper":
   computer_score = user_score

elif computer_choice == "scissors" and user_choice == "rock":
   user_choice = user_score + 1

elif computer_choice == "scissors" and user_choice == "paper":
   computer_choice = computer_score + 1

elif computer_choice == "scissors" and user_choice == "scissors":
   computer_score = user_score


if user_choice == computer_choice:
   print("equal")
elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
   print("winner: user")
else:
   print("winner: computer")