def mad_libs():
    print("Welcome to the Mad Libs game!")
    print("Please provide the following words to complete the story.")

    # Collecting inputs from the user
    large_object = input("A large object: ")
    large_objects_plural = input("Large objects (plural): ")
    adjective = input("An adjective: ")
    body_part = input("A body part: ")
    restaurant = input("A restaurant: ")
    food_1 = input("A food: ")
    food_2 = input("Another food: ")

    # Creating the story
    story = f"""
    Once upon a time, in a land filled with {large_objects_plural}, there stood a giant {large_object}.
    This {large_object} was known for its {adjective} appearance, captivating everyone who passed by.
    One day, while enjoying a meal at {restaurant}, a curious traveler accidentally bumped their {body_part}
    into the {large_object}. The incident sent plates of {food_1} and {food_2} flying across the room!
    Laughter erupted as the patrons of {restaurant} witnessed the chaotic yet amusing scene.
    """

    # Outputting the completed story
    print("\nHere's your Mad Libs story:\n")
    print(story)

# Running the Mad Libs function
if __name__ == "__main__":
    mad_libs()
