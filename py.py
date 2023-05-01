import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    pc_choice = random.choice(options)
    choice = {"Player": player_choice, "Pc": pc_choice}
    return choice

def check_win(player, pc):
    print(f"You chose {player}, computer chose {pc}")
    
    if player == pc:
        return "It's a tie!"
    elif player == "rock":
        if pc == "scissors":
            return "Rock smashes scissors! You win"
        elif pc == "paper":
            return "Paper covers rock! You lose"
    elif player == "paper":
        if pc == "rock":
            return "Paper covers rock! You win"
        elif pc == "scissors":
            return "Scissors cuts paper! You lose"
    elif player == "scissors":
        if pc == "paper":
            return "Scissors cuts paper! You win"
        elif pc == "rock":
            return "Rock smashes scissors! You lose"

choice = get_choices()
result = check_win(choice["Player"], choice["Pc"])
print(result)
