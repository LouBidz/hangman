import random
fruits = ['Apple','Grape','Strawberry','Banana','Melon'] 
word_list = fruits 

def select_random_fruit(word_list):
    """
    This function selects a random fruit from a list.

    Parameters:
    fruits (word_list): A list of fruits

    Returns:
    str: A random fruit from the list
    """
    return random.choice(word_list)

word = select_random_fruit(word_list)
print(word)

letter = input("Please enter a single letter: ")
guess = "You entered: " + str(letter)

if len(letter) ==1 and letter.isalpha(): 
    print("Good guess")
else:
    print("Ooops!That is not a valid input")

# This is the final code to milestone_2 tasks. 

# It completes all the tasks and has an added function completed for task 2 that does the same as this: 
# fruits = ['Apple','Grape','Strawberry','Banana','Melon']                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          fruits = ['Apple','Grape','Strawberry','Banana','Melon'] #Step 1:Create a list containing the names of your 5 favorite fruits.
# word_list = fruits 
# print(word_list)
# word = random.choice(word_list)
# print(word)