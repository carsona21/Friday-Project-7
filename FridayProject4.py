def trivia_quiz():
    # Define a dictionary with trivia questions and answers
    questions = {
        "What is the capital of France?": "Paris",
        "What is 2 + 2?": "4",
        "What is the largest planet in our solar system?": "Jupiter",
        "Who wrote 'Romeo and Juliet'?": "Shakespeare",
        "What is the chemical symbol for water?": "H2O"
    }

    print("Welcome to the Trivia Quiz!")
    
    # Loop through the questions in the dictionary
    for question, answer in questions.items():
        # Display the question
        print(question)
        # Prompt the user to input their answer
        user_answer = input("Your answer: ").strip()
        
        # Check if the user's answer matches the correct answer
        if user_answer.lower() == answer.lower():  # Case insensitive comparison
            print("Correct!")
        else:
            print(f"Incorrect! The correct answer is: {answer}")
        
        print()  # Print a blank line for better readability

    print("Thank you for playing the Trivia Quiz!")

# Run the trivia quiz
if __name__ == "__main__":
    trivia_quiz()
