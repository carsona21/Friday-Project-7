import random

def generate_powerball_numbers():
    # Generate five unique white ball numbers
    white_balls = random.sample(range(1, 70), 5)
    # Generate one red ball number
    red_ball = random.randint(1, 26)

    # Sort the white balls for better readability
    white_balls.sort()

    return white_balls, red_ball

def main():
    print("Welcome to the PowerBall Number Generator!")
    
    # Generate PowerBall numbers
    white_balls, red_ball = generate_powerball_numbers()

    # Display the results
    print("Your PowerBall ticket numbers are:")
    print("White Balls:", white_balls)
    print("Red Ball:", red_ball)

if __name__ == "__main__":
    main()
