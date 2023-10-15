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
# Step 1:Create a for-loop that will loop through each letter in the word
     for index, letter in enumerate(self.word):
# Step 2:Within the for-loop, do the following:
# Create an if statement that checks if the letter is equal to the guess
# In the if block, replace the corresponding "_" in the word_guessed with the guess. HINT: You can index the word_guessed at the position of the letter and assign it to the letter  
            if letter.lower() == guess:
               self.word_guessed[index] = guess
# Outside the for-loop, reduce the variable num_letters by 1  
            self.num_letters -= 1

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

