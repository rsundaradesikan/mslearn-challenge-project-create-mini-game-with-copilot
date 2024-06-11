# create a minigame of rock paper scissors using python 
# The winner of the game is determined by three simple rules:
# Rock beats scissors
# Scissors beat paper
# Paper beats rock
# Make the game multiplayer, where computer will be the opponent and can randomly choose one of the elements (rock, paper, or scissors) for each move, just like you. Your interaction in the game will be through the console
# The game should be played in rounds, where each round consists of both players making a move. The game ends when one of the players wins a certain number of rounds. The player who wins the most rounds is the winner of the game.
# The player can choose one of the three options rock, paper, or scissors and should be warned if an invalid option is chosen. The game should also warn the player if the round is a tie.
# At each round, the player must enter one of the options in the list and be informed if they won, lost or tied with the opponent
# By the end of each round, the player can choose whether to play again.
# Display the player's score at the end of the game.
# the minigame must handle user inputs, putting them in lowercase and informing the user if the input is invalid.
import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_player_choice():
    choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        choice = input("Invalid choice. Enter your choice (rock, paper, scissors): ").lower()
    return choice

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 'tie'
    if (player_choice == 'rock' and computer_choice == 'scissors') or \
       (player_choice == 'scissors' and computer_choice == 'paper') or \
       (player_choice == 'paper' and computer_choice == 'rock'):
        return 'player'
    return 'computer'

def play_game():
    player_score = 0
    computer_score = 0
    play_again = 'yes'
    while play_again == 'yes':
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(player_choice, computer_choice)
        if winner == 'player':
            player_score += 1
            print(f"You chose {player_choice}, computer chose {computer_choice}. You win this round!")
        elif winner == 'computer':
            computer_score += 1
            print(f"You chose {player_choice}, computer chose {computer_choice}. Computer wins this round!")
        else:
            print(f"Both you and the computer chose {player_choice}. It's a tie!")
        play_again = input("Do you want to play again? (yes/no): ").lower()
    print(f"Game over! Final score: You: {player_score}, Computer: {computer_score}")

play_game()
