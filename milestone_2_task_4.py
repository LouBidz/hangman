import random # import 

fruits = ['Apple','Grape','Strawberry','Banana','Melon'] #Step 1:Create a list containing the names of your 5 favorite fruits.
word_list = fruits #Step 2:Assign this list to a variable called word_list.
print(word_list)#prints out the list of fruits
word = random.choice(word_list)#variable to hold the object random.choice
print(word)#Print out the newly created list to the standard output (screen).

letter = input("Please enter a single letter: ")#Step 1:Using the input function, ask the user to enter a single letter
guess = "You entered: " + str(letter)#Step 2:Assign the input to a variable called guess.


if len(letter) ==1 or not letter.isalpha(): 
    print("Good guess")
else:
    print("Ooops!That is not a valid input")