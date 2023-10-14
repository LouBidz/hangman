import random # imports random 

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

# This looks in the list of fruits(word_list) and choses a random fruit each time its run 

