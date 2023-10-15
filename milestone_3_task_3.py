import random # import 

from milestone_3_task_3 import check_guess # import

# Step 1:Create a list containing the names of your 5 favorite fruits
fruits = ['Apple','Grape','Strawberry','Banana','Melon'] 
# Step 2:Assign this list to a variable called word_list.
word_list = fruits 
# prints out the list of fruits
print(word_list)


def ask_for_input():
# Step 3:Move the code that you wrote in the Iteratively check if the input is a valid guess task into this function block.
 while True:
# Step 4:Ask the user to guess a letter and assign this to a variable called guess.
      guess = input ("Please guess a letter: ")
      check_guess(guess)
# Step 5:Check that the guess is a single alphabetical character. 
# Hint: You can use Python's isalpha method to check if the guess is alphabetical.
      if len(guess) ==1 and guess.isalpha(): 
# Step 6:If the guess passes the checks, break out of the loop.
          break
# Step 7:If the guess does not pass the checks, then print a message saying "Invalid letter. 
# Please, enter a single alphabetical character."
      print("Invalid letter. Please, enter a single alphabetical character.")

# Step 8:Outside the while loop, but within this function, call the check_guess function to check if the guess is in the word. 
# Don't forget to pass in the guess as an argument to the method.
# Step 9:Outside the function, call the ask_for_input function to test your code.
ask_for_input()

# This creates the function that asks the user to guess a letter and checks the input.