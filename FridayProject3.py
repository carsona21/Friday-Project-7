import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    # Ask if the user wants to play
    play = input("Do you want to play? (yes/no): ").strip().lower()
    
    if play == 'no':
        print("Maybe next time!")
        return  # Exit the function if the user doesn't want to play
    
    while play == 'yes':
        secret_number = random.randint(1, 10)  # Generate a random number between 1 and 10
        guess = None  # Initialize guess
        
        print("I have chosen a number between 1 and 10. Try to guess it!")
        
        # Continue prompting the user to guess until they guess correctly
        while guess != secret_number:
            guess = int(input("Enter your guess: "))  # Get the user's guess
            
            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print("Congratulations! You've guessed the number!")
        
        # Ask if the user wants to play again
        play = input("Do you want to play again? (yes/no): ").strip().lower()
    
    print("Thank you for playing! Goodbye!")

# Run the game
if __name__ == "__main__":
    number_guessing_game()
