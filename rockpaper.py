import random

def play_game():
    options = ["rock", "paper", "scissors"]
    
    print("--- Welcome to Rock, Paper, Scissors! ---")
    
    # Get user choice
    user_choice = input("Enter rock, paper, or scissors: ")
    
    # Validate input
    if user_choice not in options:
        print("Invalid choice! Please restart and try again.")
        return

    # Computer choice
    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")

    # Determine winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")

# Run the game
while True:
    play_game()
