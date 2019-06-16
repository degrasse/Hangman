import pickle
import random

def containLetter(string, char):

    #function to return true if string contains char
    for  i in range (0, len(string)): #loop through index of string
      #  string[i]
        if string[i] == char:
            return True
    return False
# print(containLetter("Hello", "o"))

#print a title bar
def title_bar():
    print("--------------------------------------")
    print("--------------Hang Man----------------")
    print("--------------------------------------")

# title_bar()

def make_word_list():
    # define a function
    # that asks the user to enter a word
    # until the user typed N
    # save into a .pydata file

    words = []
    user_input = input ("Enter a word: ")
    while user_input != "N":
        # add user_input to words
        # update user_input
        words.append(user_input)
        user_input = input("Enter a word: ")
    try:
        file = open('hangman.pydata', 'wb')
        pickle.dump(words, file)
        file.close()
    except:
        print("I can't find file.")


def select_word():
    try:
        file = open("hangman.pydata", "rb")
        words = pickle.load(file)
        file.close()

        index = random.randint(0, len(words)-1)
        return words [index]
    except:
        print("I can't open file.")

# secret_word = select_word()
# print(secret_word)


def display_underscores(word):
    # strawberry
    # _ _ _ _ _ _ _ _ _ _
    # summer break
    #  _ _ _ _ _ _    _ _ _ _ _
    # take the given word
    # return with appropriate number of underscores and spaces

    returnWord = ""
    for letter in word:
        if letter == " ":
            returnWord += " "
        else:
            returnWord += "_"

    return returnWord


# print(display_underscores(secret_word))

# Main game

title_bar()
print()
secret_word = select_word()
#print(display_underscores(select_word()))
word_so_far = display_underscores(secret_word)



print()

print("The word so far is: ")
for letter in word_so_far:
    print(letter, end = " ")

print()
print()
user_input = input("please guess a letter: ")

user_inputList = ""



# for each word, user has 6 guesses
# while guess < 6
    # if the user has guessed the same letter before
    # print you have already guess this letter
    # else:
    # if the word contains the letter
    # print the letter its position
    # else
    # print word doesn't contain the letter

    # round = round +3 1

for i in range(0, len(secret_word) + 7):
 user_inputList = user_inputList[0:i] + user_input + user_inputList[i + 1:]
    # if user_input not in word_so_far and user_inputList.__contains__(user_input):
    #         print("You already guessed that letter!")

# ask the user if they want to play again


turn = 6
replay = ""

while replay != "n":
    while turn >= 1:
      #  user_inputList = user_inputList + user_input



        if containLetter(secret_word, user_input.upper()):
            print("The word contains the letter " + user_input)
            print()
            # find where the index of the letter in secret_word
            for i in range(0,len(secret_word)):
                if secret_word[i] == user_input:
                    word_so_far = word_so_far[0:i] + user_input + word_so_far[i+1:]


            # replace the _ in word_so_far with the letter
            #         if word_so_far.__contains__(user_input):
            #          print("You already guessed that letter!")



        else:



                 print("The word does not contain the letter " + user_input)

                 turn = turn - 1



        print("The word you guessed so far is: ")
        for letter in word_so_far:
            print(letter, end = " ")
        print()
        print("you have " + str(turn) + " guesses left")

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
        # if user_inputList.__contains__(user_input):
        #     print("You already guessed that letter!")


    replay = input("Do you want to play again? enter y or n")
    if replay == "y":
        turn = 6

        secret_word = select_word()
        # print(display_underscores(select_word()))
        word_so_far = display_underscores(secret_word)

        print()

        print("The word so far is: ")
        for letter in word_so_far:
            print(letter, end=" ")

        print()
        print()
        user_input = input("please guess a letter: ")

        while len(user_input) > 1:
            user_input = input("Invalid input, enter a letter")


        # if user_inputList.__contains__(user_input):
        #     print("You already guessed that letter!")

    elif (replay == "n"):
        print("Goodbye!")
        break
