import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]


def print_score():
    print("Your wins:", user_wins)
    print("Computer wins:", computer_wins)


while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        input("Invalid input. Please try again.")
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("Computer chose", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You win!")
        user_wins += 1
        print_score()
    elif user_input == "paper" and computer_pick == "rock":
        print("You win!")
        user_wins += 1
        print_score()
    elif user_input == "scissors" and computer_pick == "paper":
        print("You win!")
        user_wins += 1
        print_score()
    elif user_input == computer_pick:
        print("It's a tie!")
        print_score()
    else:
        print("You lose!")
        computer_wins += 1
        print_score()

print("Thanks for playing!")
