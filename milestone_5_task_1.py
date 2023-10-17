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
     for indx, let in enumerate(self.word):
        if let == guess: 
         self.word_guessed[indx] = guess
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

# Step 1:Create a function called play_game that takes word_list as a parameter. Inside the function, write the code for the following steps
 def play_game(word_list):
        game = Hangman(word_list, num_lives=5)
        while game.num_lives > 0 and game.num_letters > 0:
              game.ask_for_input()
              if game.num_lives == 0: 
               print("You lost")
        else:
                print ('Congratulations. You won the game!')
        pass


# Create a variable called num_lives and assign it to 5
        # num_lives = 5
#  Create an instance of the Hangman class. Do this by calling the Hangman class and assign it to a variable called game
# Pass word_list and num_lives as arguments to the game object
        # game = Hangman(word_list, num_lives=5)

# Create a while loop and set the condition to True. In the body of the loop, do the following:
# Check if the num_lives is 0. If it is, that means the game has ended and the user lost. Print a message saying 'You lost!'
# Next, check if the num_letters is greater than 0. In this case, you would want to continue the game, so you need to call the ask_for_input method.
# If the num_lives is not 0 and the num_letters is not greater than 0, that means the user has won the game. Print a message saying 'Congratulations. You won the game!'
     
if __name__ == '__main__':
 word_list = ['Apple','Grape','Strawberry','Banana','Melon']
 play_game(word_list)

