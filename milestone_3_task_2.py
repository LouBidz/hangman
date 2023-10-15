import random # import 

# Step 1:Create a list containing the names of your 5 favorite fruits
fruits = ['Apple','Grape','Strawberry','Banana','Melon'] 
# Step 2:Assign this list to a variable called word_list.
word_list = fruits 
# prints out the list of fruits
print(word_list)

# Step 3: Select a random word from the list 
def select_random_fruit(word_list):
       return random.choice(word_list)

word = select_random_fruit(word_list)
print(word)

# Step 4:Ask the user to guess a letter and assign this to a variable called guess.
guess = input ("Please guess a letter: ")

# Step 5:Create an if statement that checks if the guess is in the word.
if guess in word:
# Step 6:In the body of the if statement, print a message saying "Good guess! {guess} is in the word.". 
# Obviously, format the string to show the actual guess instead of {guess}.
   print (f"Good guess! {guess} is in the word")
# Step 7:Create an else block that prints a message saying "Sorry, {guess} is not in the word. Try again." 
# This block of code will run if the guess is not in the word.
else: 
   print (f"Sorry, {guess} is not in the word. Try again.")

# This creates an if statement that checks that the users guess is in the random word
