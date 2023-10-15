import random


class Hangman:

 def __init__(self, word_list, num_lives=5):
  self.word = random.choice(word_list)
  self.word_guessed = [" _ " for _ in self.word]
  self.num_letters = len(set(self.word))
  self.num_lives = num_lives
  self.list_of_guesses = []

 def check_guess(self, guess):
    guess = guess.lower()
    if guess in self.word:
        print(f"Good guess! {guess} is in the word")
        for index, letter in enumerate(self.word):
            if letter == guess:
                self.word_guessed[index] = guess
                self.num_letters -= 1

# Step 1:In the check_guess method, Create an else statement.
# Step 2:Within the else block:
    else:
        # Reduce `num_lives' by 1
        self.num_lives -= 1
        # Print a message saying "Sorry, {letter} is not in the word."
        print(f"Sorry, {guess} is not in the word")
        # Print another message saying "You have {num_lives} lives left."
        print(f"You have {self.num_lives} lives left")

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
