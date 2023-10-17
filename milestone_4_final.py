import random

class Hangman:

 def __init__(self, word_list, num_lives=5):
  self.word = random.choice(word_list)
  self.word_guessed = [" _ "] * len(self.word)
  self.num_letters = len(set(self.word))
  self.num_lives = num_lives
  self.list_of_guesses = []

 def check_guess(self, guess):
    guess = guess.lower()
    if guess in self.word:
      for index, letter in enumerate(self.word):
        if letter == guess: 
           self.word_guessed[index] = guess
           self.num_letters -= 1
        print(f"Good guess! {guess} is in the word")
        print(f' '.join(self.word_guessed))
    else:
        self.num_lives -= 1
        print(f"Sorry, {guess} is not in the word")
        print(f"You have {self.num_lives} lives left")
    pass
 
 def ask_for_input(self):
    while True:
        guess = input("Guess a letter: ").lower()
        if guess in self.word:
            for inx, letter in enumerate(self.word):
                if guess == letter:
                    self.word_guessed[inx] = guess
                    self.num_letters -=1
        elif guess in self.list_of_guesses:
            print("You already tried that letter!")
        elif not guess.isalpha() or len(guess) != 1:
            print("Invalid letter. Please, enter a single alphabetical character.")
        else:
            self.check_guess(guess)
            break
    self.list_of_guesses.append(guess)
    pass
 
word_list = ['Apple','Grape','Strawberry','Banana','Melon']
game = Hangman(word_list)
game.ask_for_input()

# This completes milestone 4
# It completes all tasks and runs a game of hangman 
