import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")

    option = ["rock", "paper", "scissors"]

    computer_choice = random.choice(option)

    choices = {"player": player_choice, "computer": computer_choice}

    return choices

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")

    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        return "Paper covers rock! You lose."

    elif player == "paper":
        if computer == "scissors":
            return "scissors cut paper! You lose."
        return "Paper covers rock! You win!"

    elif player == "scissors":
        if computer == "paper":
            return "scissors cut paper! You win!"
        return "Rock smashes scissors! You lose."


final_choices = get_choices()
RESULT = check_win(final_choices["player"], final_choices["computer"])
print(RESULT)
