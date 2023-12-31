# Step 1:Create a while loop and set the condition to True. Setting the condition to True` ensures that the code runs continuously.
# In the body of the loop, write the code required for the following steps.

while True:
# Step 2:Ask the user to guess a letter and assign this to a variable called guess.
      guess = input ("Please guess a letter: ")
# Step 3:Check that the guess is a single alphabetical character. 
# Hint: You can use Python's isalpha method to check if the guess is alphabetical.
      if len(guess) ==1 and guess.isalpha(): 
# Step 4:If the guess passes the checks, break out of the loop.
          break
# Step 5:If the guess does not pass the checks, then print a message saying "Invalid letter. 
# Please, enter a single alphabetical character."
      print("Invalid letter. Please, enter a single alphabetical character.")

# Step 5:If the guess does not pass the checks, then print a message saying "Invalid letter. 
# Please, enter a single alphabetical character."

# This is a while true loop that allows the user to guess a letter and prints an error if user enters more than one 
# character or a non-alphabetical character.