"""
Number Guessing Game
A simple interactive game where players guess a randomly generated number.
"""

import random
import os

def clear_screen():
    """Clear the console screen for better user experience."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_welcome():
    """Display welcome message and game rules."""
    print("=" * 50)
    print("     WELCOME TO THE NUMBER GUESSING GAME!")
    print("=" * 50)
    print("\nHow to play:")
    print("1. Choose a difficulty level")
    print("2. Guess the secret number within the range")
    print("3. Get hints after each guess")
    print("4. Try to guess in minimum attempts!\n")

def choose_difficulty():
    """Allow player to select game difficulty level."""
    print("Select Difficulty Level:")
    print("1. Easy (1-50, 10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard (1-200, 5 attempts)")
    
    while True:
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '1':
            return 50, 10, "Easy"
        elif choice == '2':
            return 100, 7, "Medium"
        elif choice == '3':
            return 200, 5, "Hard"
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

def get_player_guess(max_range):
    """Get and validate player's guess."""
    while True:
        try:
            guess = int(input(f"\nEnter your guess (1-{max_range}): "))
            if 1 <= guess <= max_range:
                return guess
            else:
                print(f"Please enter a number between 1 and {max_range}!")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def provide_hint(guess, secret_number, max_range):
    """Provide helpful hints based on the player's guess."""
    difference = abs(guess - secret_number)
    
    if difference == 0:
        return "correct"
    elif difference <= max_range * 0.05:
        return "🔥 Very Hot! You're extremely close!"
    elif difference <= max_range * 0.10:
        return "🌡️ Hot! Getting closer!"
    elif difference <= max_range * 0.20:
        return "☀️ Warm! You're on the right track!"
    elif difference <= max_range * 0.40:
        return "❄️ Cold! Still far away..."
    else:
        return "🧊 Very Cold! Way off!"

def play_game():
    """Main game logic."""
    display_welcome()
    
    # Get difficulty settings
    max_range, max_attempts, difficulty = choose_difficulty()
    secret_number = random.randint(1, max_range)
    
    print(f"\n{'='*50}")
    print(f"Difficulty: {difficulty}")
    print(f"Range: 1 to {max_range}")
    print(f"Maximum Attempts: {max_attempts}")
    print(f"{'='*50}\n")
    
    attempts = 0
    guess_history = []
    
    # Game loop
    while attempts < max_attempts:
        attempts += 1
        remaining = max_attempts - attempts + 1
        
        print(f"\nAttempt {attempts}/{max_attempts} (Remaining: {remaining})")
        guess = get_player_guess(max_range)
        guess_history.append(guess)
        
        # Check if guess is correct
        if guess == secret_number:
            print("\n" + "🎉" * 25)
            print(f"   CONGRATULATIONS! You guessed it right!")
            print(f"   The secret number was: {secret_number}")
            print(f"   You won in {attempts} attempt(s)!")
            print("🎉" * 25 + "\n")
            
            # Display guess history
            print(f"Your guesses: {guess_history}")
            return True
        
        # Provide directional hint
        if guess < secret_number:
            direction = "📈 Too Low!"
        else:
            direction = "📉 Too High!"
        
        # Provide temperature hint
        temperature = provide_hint(guess, secret_number, max_range)
        
        print(f"\n{direction}")
        print(temperature)
        
        # Show previous guesses
        if len(guess_history) > 1:
            print(f"Previous guesses: {guess_history[:-1]}")
    
    # Game over - out of attempts
    print("\n" + "💔" * 25)
    print(f"   GAME OVER! You've run out of attempts.")
    print(f"   The secret number was: {secret_number}")
    print(f"   Your guesses: {guess_history}")
    print("💔" * 25 + "\n")
    return False

def display_stats(games_played, games_won):
    """Display player statistics."""
    if games_played > 0:
        win_rate = (games_won / games_played) * 100
        print(f"\n{'='*50}")
        print("YOUR STATISTICS")
        print(f"{'='*50}")
        print(f"Games Played: {games_played}")
        print(f"Games Won: {games_won}")
        print(f"Win Rate: {win_rate:.1f}%")
        print(f"{'='*50}\n")

def main():
    """Main program entry point."""
    games_played = 0
    games_won = 0
    
    print("\n🎮 Starting Number Guessing Game... 🎮\n")
    
    while True:
        # Play one game
        won = play_game()
        games_played += 1
        
        if won:
            games_won += 1
        
        # Ask to play again
        play_again = input("\nWould you like to play again? (yes/no): ").lower()
        
        if play_again not in ['yes', 'y']:
            display_stats(games_played, games_won)
            print("\nThank you for playing! Goodbye! 👋\n")
            break
        
        clear_screen()

if __name__ == "__main__":
    main()
