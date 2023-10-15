import random

class Hangman:

 def __init__(self, word_list, num_lives=5):
  self.word = random.choice(word_list)
  self.word_guessed = [" _ " for _ in self.word]
  self.num_letters = len(set(self.word))
  self.num_lives = num_lives
  self.list_of_guesses = []

 def check_guess(self,guess):
     guess = guess.lower()
     if guess in self.word:
      print(f"Good guess! {guess} is in the word")

 def ask_for_input(self):
    while True:
        guess = input("Guess a letter: ").lower()
        if not guess.isalpha() or len(guess) != 1:
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in self.list_of_guesses:
            print("You already tried that letter!")
        else:
            self.check_guess(guess)
            self.list_of_guesses.append(guess)
        break
 ask_for_input()
word_list = ['Apple','Grape','Strawberry','Banana','Melon'] 

# The above code is broken down into each step below :

# Step 1:Define a method called check_guess. Pass the guess to the method as a parameter. In the body of the method, write the code for the following steps:
# Convert the guessed letter to lower case
# Create an if statement that checks if the guess is in the word
# In the body of the if statement, print a message saying "Good guess! {guess} is in the word."
# You will continue with the logic of the check_guess method in the next task. For now, let's create the ask_for_input method.
# Step 2:Define a method called ask_for_input. In the body of the method, do the following:
# Create a while loop and set the condition to True
# Ask the user to guess a letter and assign this to a variable called guess
# Create an if statement that runs if the guess is NOT a single alphabetical character
# In the body of the if statement, print a message saying "Invalid letter. Please, enter a single alphabetical character."
# Create an elif statement that checks if the guess is already in the list_of_guesses
# In the body of the elif statement, print a message saying "You already tried that letter!"
# If the guess is a single alphabetical character and it's not already in the list_of_guesses, create an else block and call the check_guess method. Remember to pass the guess as an argument to this method.
# Finally, append the guess to the list_of_guesses.
# Ensure you do this in the else block of this function, rather than inside the check_guess method, so that the letter can be appended to the list_of_guesses in both conditions.
# Step 3:Call the ask_for_input method to test your code.