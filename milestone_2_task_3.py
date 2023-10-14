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

# Step 1:Using the input function, ask the user to enter a single letter
letter = input("Please enter a single letter: ")
# Step 2:Assign the input to a variable called guess.
guess = "You entered: " + str(letter)

# This creates a list of fruits,chooses a random fruit and prints it.
# Then it asks the user to choose a single letter from the alphabet and assigns it to a variable called guess.