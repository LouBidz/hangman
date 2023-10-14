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

# Step 1:Create an if statement that checks if the length of the input is equal to 1 and the input is alphabetical.
if len(letter) ==1 and letter.isalpha(): 
# Step 2:In the body of the if statement, print a message that says "Good guess!".
    print("Good guess")
# Step 3:Create an else block that prints "Oops! That is not a valid input." if the preceding conditions are not met.
else:
    print("Ooops!That is not a valid input")

# This creates a list of fruits,chooses a random fruit and prints it.
# Then it asks the user to choose a single letter from the alphabet and assigns it to a variable called guess.
# Lastly, it checks if the letter is in the alphabet and is a single letter,if it's true print "Good guess",
# if false print "Ooops!That is not a valid input"