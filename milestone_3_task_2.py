import random # import 

# Step 1:Create a list containing the names of your 5 favorite fruits
fruits = ['Apple','Grape','Strawberry','Banana','Melon'] 
# Step 2:Assign this list to a variable called word_list.
word_list = fruits 
# prints out the list of fruits
print(word_list)
# Step 3:Create the random.choice method and pass the word_list variable into the choice method
# Step 4:Assign the randomly generated word to a variable called word.
word = random.choice(word_list)
# Step 5: Print out word to the standard output. Run the code several times and observe the words printed out after each run.
print(word)

# Step 2:Ask the user to guess a letter and assign this to a variable called guess.
guess = input ("Please guess a letter: ")

# Step 1:Create an if statement that checks if the guess is in the word.
if guess in word:
# Step 2:In the body of the if statement, print a message saying "Good guess! {guess} is in the word.". 
# Obviously, format the string to show the actual guess instead of {guess}.
   print (f"Good guess! {guess} is in the word")
# Step 3:Create an else block that prints a message saying "Sorry, {guess} is not in the word. Try again." 
# This block of code will run if the guess is not in the word.
else: 
   print (f"Sorry, {guess} is not in the word. Try again.")

# This creates an if statement that checks that the users guess is in the random word
