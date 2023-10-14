
import random


fruits = ['Apple','Grape','Strawberry','Banana','Melon']
word_list = fruits
print(word_list)
word = random.choice(word_list)
print(word)

while True:
    try:
        # Try to get a single letter from the user
        letter = input("Please enter a single letter: ")
        if len(letter) == 1 and letter.isalpha():
            raise ValueError("Good guess")
        print("Ooops! That is not a valid input: " + letter)
        break  # If the input is valid, break the loop
    except ValueError as exception:
        # If a ValueError is raised, print an error message and continue the loop
        print(exception)

