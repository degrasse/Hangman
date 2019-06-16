import pickle
import random


def containLetter(string, char):
    # function to return true if string contains char
    for i in range(0, len(string)):  # loop through index of string
        #  string[i]
        if string[i] == char:
            return True
    return False




# print a title bar
def title_bar():
    print("--------------------------------------")
    print("--------------Hang Man----------------")
    print("--------------------------------------")



def city_list():

    words = []
    user_input = input ("Enter a city: ")
    while user_input != "N":
        # add user_input to words
        # update user_input
        words.append(user_input)
        user_input = input("Enter a city: ")
    try:
        file = open('cities.pydata', 'wb')
        pickle.dump(words, file)
        file.close()
    except:
        print("I can't find file.")
def country_list():

    words = []
    user_input = input ("Enter a country: ")
    while user_input != "N":
        # add user_input to words
        # update user_input
        words.append(user_input)
        user_input = input("Enter a country: ")
    try:
        file = open('countries.pydata', 'wb')
        pickle.dump(words, file)
        file.close()
    except:
        print("I can't find file.")
def animal_list():

    words = []
    user_input = input ("Enter an animal: ")
    while user_input != "N":
        # add user_input to words
        # update user_input
        words.append(user_input)
        user_input = input("Enter an animal: ")
    try:
        file = open('animals.pydata', 'wb')
        pickle.dump(words, file)
        file.close()
    except:
        print("I can't find file.")





def categories():
    user_input = input("Type the name of the category you would like to play: cities, countries, or animals")
    if user_input == "countries":
        try:
            file = open("countries.pydata", "rb")
            words = pickle.load(file)
            file.close()

            index = random.randint(0, len(words) - 1)
            return words[index]
        except:
            print("I can't open file.")

    elif user_input == "cities":
        try:
            file = open("cities.pydata", "rb")
            words = pickle.load(file)
            file.close()

            index = random.randint(0, len(words) - 1)
            return words[index]
        except:
            print("I can't open file.")

    elif user_input == "animals":
        try:
            file = open("animals.pydata", "rb")
            words = pickle.load(file)
            file.close()

            index = random.randint(0, len(words) - 1)
            return words[index]
        except:
            print("I can't open file.")

    else:
        return None




# def categories():
#     user_input = input("Type the name of the category you would like to play: cities, countries, or animals")
#     if user_input == "countries":
#         return countries
#     elif user_input == "cities":
#         return cities
#     elif user_input == "animals":
#         return animals
#     else:
#         return None

# def getWord():
#
#     words = categories()
#     index = random.randint(0, len(words) - 1)
#     return words[index]


def display_underscores(word):
    returnWord = ""
    for let in word:
        if let == " ":
            returnWord += " "
        else:
            returnWord += "_"

    return returnWord



#made my word list

# city_list()
# country_list()
# animal_list()

title_bar()
print()


secret_word = categories()


word_so_far = display_underscores(secret_word)

print()

print("The word so far is: ")
for letter in word_so_far:
    print(letter, end=" ")

print()
user_input = input("please guess a letter: ")
user_inputList = ""
badgeuss = []

for i in range(0, len(secret_word) + 7):
    user_inputList = user_inputList[0:i] + user_input + user_inputList[i + 1:]


turn = 6
replay = ""

while replay != "n":
    while turn >= 1:

        if user_input not in secret_word:
            print("The word does not contain the letter " + user_input)
            # check if already guessed letter
            if user_input in badgeuss:
                print("You already guessed that letter")

            else:
                turn = turn - 1
                badguess = badgeuss.append(user_input)
                print("you have " + str(turn) + " guesses left")
                print("The word you guessed so far is: ")

        elif containLetter(secret_word, user_input):
            print("The word contains the letter " + user_input)
            print()
            # find where the index of the letter in secret_word
            for i in range(0, len(secret_word)):
                if secret_word[i] == user_input:
                    word_so_far = word_so_far[0:i] + user_input + word_so_far[i + 1:]



        for letter in word_so_far:
            print( letter, end=" ")
        print()

        # end of game
        if turn == 0:
            print("You lose :(")
            break
        print()
        if (word_so_far == secret_word):
            print("You win!")
            break

        user_input = input("Please guess a letter")

        while len(user_input) > 1:
            user_input = input("Invalid input, enter a letter")

    # check if want to play again
    replay = input("Do you want to play again? enter y or n")
    if replay == "y":
        turn = 6

        secret_word = categories()
        # print(display_underscores(select_word()))
        word_so_far = display_underscores(secret_word)

        print()

        print("The word so far is: ")
        for letter in word_so_far:
            print(letter, end=" ")

        print()
        print()
        user_input = input("please guess a letter: ")

        user_inputList = ""




    elif replay == "n":
        print("Goodbye!")
        break
