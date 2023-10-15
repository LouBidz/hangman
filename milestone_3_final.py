import random

from milestone_3_task_3 import check_guess # import

fruits = ['Apple','Grape','Strawberry','Banana','Melon'] 
word_list = fruits 
print(word_list)


def select_random_fruit(word_list):
       return random.choice(word_list)

word = select_random_fruit(word_list)
print(word)

def check_guess(guess):
      guess = input ("Please guess a letter: ")
      guess = guess.lower()
      if guess in word:
       print (f"Good guess! {guess} is in the word")
      else: 
       print (f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
 while True:
      guess = input ("Please guess a letter: ")
      check_guess(guess)
      if len(guess) ==1 and guess.isalpha(): 
          break
      print("Invalid letter. Please, enter a single alphabetical character.")


ask_for_input()

# This is the final code to milestone 3 
# It completes all tasks, with functions used to make the code more readable and accessible.