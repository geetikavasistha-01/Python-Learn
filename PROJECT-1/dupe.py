import random

def game_result(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'snake' and computer_choice == 'water') or \
         (user_choice == 'water' and computer_choice == 'gun') or \
         (user_choice == 'gun' and computer_choice == 'snake'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    choices = ['snake', 'water', 'gun']
    computer_choice = random.choice(choices)

    print("Welcome to Snake Water Gun Game!")
    print("Choices: snake, water, gun")
    
    user_choice = input("Enter your choice: ").lower()

    if user_choice not in choices:
        print("Invalid choice! Please choose from snake, water, or gun.")
        return

    print(f"Computer chose: {computer_choice}")
    result = game_result(user_choice, computer_choice)
    print(result)

# Running the game
play_game()
