import random


print("ROCK PAPER SCISSSOR GAME")
def play_round():
    options = ['rock', 'paper', 'scissors']
    user_choice = input("Enter your choice : rock, paper, or scissors: ").lower()
    if user_choice not in options:
        return "Invalid choice"
    
    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "Yeah, You Won"
    else:
        return "Ohh No, Computer Won"

print(play_round())
