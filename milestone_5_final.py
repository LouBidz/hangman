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
         print(f"Good guess! {guess} is in the word")
        for index, letter in enumerate(self.word):
            if letter == guess:
             self.word_guessed[index] = guess
             self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word")
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

    def play_game(words_list):
     num_lives = 5
     game = Hangman(word_list, num_lives=5)
     while game.num_lives > 0 and game.num_letters > 0:
              game.ask_for_input()
              if game.num_lives == 0: 
               print("You lost")
     else:
                print ('Congratulations. You won the game!')
        




word_list = ['Apple','Grape','Strawberry','Banana','Melon']
game = Hangman(word_list)
game.ask_for_input()

# This completes milestone 5 task 2.