def redText(text):
    return f"\033[91m{text}\033[0m"

def blueText(text):
    return f"\033[94m{text}\033[0m"

def greenText(text):
    return f"\033[92m{text}\033[0m"

def yellowText(text):
    return f"\033[93m{text}\033[0m"

def brownText(text):
    return f"\033[33m{text}\033[0m"  # ANSI code for brown is often represented as yellow

def main():
    # Call each function and print the text in the corresponding color
    print(redText("This text is red!"))
    print(blueText("This text is blue!"))
    print(greenText("This text is green!"))
    print(yellowText("This text is yellow!"))
    print(brownText("This text is brown!"))

    # User input for custom color choice
    color_choice = input("Choose a color (red, blue, green, yellow, brown): ").strip().lower()
    user_text = input("Enter the text you want to display: ")

    # Display the user's text in the chosen color
    if color_choice == "red":
        print(redText(user_text))
    elif color_choice == "blue":
        print(blueText(user_text))
    elif color_choice == "green":
        print(greenText(user_text))
    elif color_choice == "yellow":
        print(yellowText(user_text))
    elif color_choice == "brown":
        print(brownText(user_text))
    else:
        print("Invalid color choice!")

# Run the main program
if __name__ == "__main__":
    main()
