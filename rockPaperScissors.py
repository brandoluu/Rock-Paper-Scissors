import random 

options = ["rock", "paper", "scissors"]
computer_win = 0
user_win = 0

while True:
    user_input = input("please enter Rock/Paper/Scissors or Q to quit: ").lower()

    if user_input == "q":
        break

    if user_input not in options:
        print("Error: please select rock/paper/scissors or q to exit")
        continue

    randomNumber = random.randint(0,2)
    computerChoice = options[randomNumber]
    print("computer picked " + computerChoice)

    if user_input == "rock" and computerChoice == "scissors":
        print("you win!")
        user_win += 1

    elif user_input == "paper" and computerChoice == "rock":
        print("you win!")
        user_win += 1

    elif user_input == "scissors" and computerChoice == "paper":
        print("you win!")
        user_win += 1
    
    elif user_input == "rock" and computerChoice == "rock":
        print("Tie!")
        user_win += 1

    elif user_input == "paper" and computerChoice == "paper":
        print("Tie!")
        user_win += 1

    elif user_input == "scissors" and computerChoice == "scissors":
        print("Tie!")
        user_win += 1

    else:
        print("you lose!")
        computer_win += 1



print("you won " + str(user_win) + " times")
print("the computer won " + str(computer_win) + " times")
