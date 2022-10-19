import time
from random_word import RandomWords


word = RandomWords().get_random_word()
guess_right = []
guess_wrong = []
game_running = True


def man():
    if len(guess_wrong) == 1:
        print(" O\n")
    if len(guess_wrong) == 2:
        print(" O\n"
              " |\n")
    if len(guess_wrong) == 3:
        print(" O\n"
              "/|\n")
    if len(guess_wrong) == 4:
        print(" O\n"
              "/|\\\n")
    if len(guess_wrong) == 5:
        print(" O\n"
              "/|\\\n"
              "/\n")
    if len(guess_wrong) == 6:
        print(" O\n"
              "/|\\\n"
              "/ \\\n")
    else:
        pass


print("Let's play Hangman.")
time.sleep(1)
# print("  ------\n"
#       "  |     |\n"
#       "  |\n"
#       "  |\n"
#       "  |\n"
#       "  |\n"
#       "-----")
print("I'll choose a word and you guess.")
time.sleep(1)

didWin = False
while game_running:

    print("\n")
    man()

    for i in word:
        if i in guess_right:
            print(i, end="")
        else:
            print("_", end="")

    guess: str = input("\nWhat is your guess? ")

    if len(guess_right) != 0 and len(guess_wrong) != 0 and game_running is not False:
        print("Wrong guesses: ", end="")
        for i in range(len(guess_wrong)):
            print(guess_wrong[i] + " ", end="")
        print("")

    if guess in word and guess not in guess_right and guess != "":
        print("You got it!\n")
        guess_right.append(guess)

    if guess == "":
        print("That's not a guess.")

    if guess not in word:
        print("Wrong!\n")
        guess_wrong.append(guess)
        print("Wrong guesses: ", end="")
        for i in range(len(guess_wrong)):
            print(guess_wrong[i] + " ", end="")
        print("")

    didWin = True
    for i in word:
        if i not in guess_right:
            didWin = False

    if didWin == True:
        print("\nYou won!")
        print("The word was " + word)
        break

    if len(guess_wrong) == 6:
        game_running = False
        print("\nYou lost!")
        print("The word was " +word)
        break