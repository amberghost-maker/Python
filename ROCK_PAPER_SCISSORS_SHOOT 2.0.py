import random
from collections import Counter

def get_player_move():
    """Prompt player for input and validate it."""
    while True:
        move = input("\nEnter your move (Rock/Paper/Scissors) or 'quit' to exit: ").strip().capitalize()
        if move in ['Rock', 'Paper', 'Scissors']:
            return move
        elif move == 'Quit':
            return None
        else:
            print("Invalid move! Please enter Rock, Paper, or Scissors.")

def get_ai_move_basic():
    """Basic AI: chooses randomly."""
    return random.choice(['Rock', 'Paper', 'Scissors'])

def get_ai_move_smart(player_history):
    """Enhanced AI: uses frequency analysis + simple pattern recognition."""
    if not player_history:
        return random.choice(['Rock', 'Paper', 'Scissors'])

    
    most_common = Counter(player_history).most_common(1)[0][0]

    counters = {'Rock': 'Paper', 'Paper': 'Scissors', 'Scissors': 'Rock'}
    return counters[most_common]

def determine_winner(player_move, ai_move):
    """Determine winner based on standard RPS rules."""
    if player_move == ai_move:
        return "Tie"

    winning_moves = {
        'Rock': 'Scissors',
        'Paper': 'Rock',
        'Scissors': 'Paper'
    }

    if winning_moves[player_move] == ai_move:
        return "Player"
    else:
        return "AI"

def play_game():
    print(" ~~~ Welcome to Rock Paper Scissors! ~~~ \n")

    player_score = 0
    ai_score = 0
    player_history = []

    while True:

        player_move = get_player_move()
        if player_move is None:
            print("\nThanks for playing! ")
            break
        ai_move = get_ai_move_smart(player_history)

        player_history.append(player_move)

        result = determine_winner(player_move, ai_move)

        print(f"\nYou played: {player_move}")
        print(f"AI played: {ai_move}")

        if result == "Tie":
            print(" It's a tie!")
        elif result == "Player":
            print(" You win this round!")
            player_score += 1
        else:
            print(" AI wins this round!")
            ai_score += 1

        print(f"Score - You: {player_score} | AI: {ai_score}")

if __name__ == "__main__":
    play_game()
    