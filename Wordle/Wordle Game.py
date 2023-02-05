# Wordle Game

from random import choice
import os

letters = 'abcdefghijklmnopqrstuvwxyz'
word_file = open("C:\\Users\\mjarv\\OneDrive\\Documents\\Python\\Wordle\\Word_list.txt", "r")
words = word_file.read()
words_split = words.split("\n")

def board():

    print("""Welcome to Wordle\n
    You have 5 attempts to work out the hidden word
    letters shown in upper case are the correct letter in the correct position
    letters shown in lower case are the correct letter in the wrong place
    Good luck! """)

    counter = 0
    word = choice(words_split)
    # print(word)
    while True:
        print()
        print(f"Attempt: {counter+1}/5")
        guess_results = []
        guess = ""
        while len(guess) != 5: 
            guess = input("Type a 5 letter word: ").lower()

        index = 0
        while index < 5:
            if guess[index] == word[index]:
                guess_results.append(guess[index].upper())
            else:
                guess_results.append("_")
            index += 1

        word_list = []
        for letter in word:
            word_list.append(letter)

        # take out the right letter right place
        for index in range(0,5):
            if guess_results[index] == word_list[index].upper():
                word_list[index] = "*"
                guess_results[index] = "*"

        # print right letter wrong place
        for index, letter in enumerate(guess):
            for index2, let in enumerate(word_list):
                if letter == let:
                    guess_results[index] = letter
                    word_list[index2] = "!"

        for step in range(0,5):
            if word_list[step] == "*":
                guess_results[step] = guess[step].upper()
        print(guess_results)

        counter += 1

        if letters not in guess_results and "_" not in guess_results:
            print("\nWinner! ")
            break
        elif counter == 5:
            print("\nGame over, out of turns! ")
            print(f"The word was {word}!! ")
            break


play = True
while play:
    board()
    play_again = ""
    while play_again not in ("Y", "N"):
        play_again = input("Another game? (Y/N) ").upper()
    if play_again == "N":
        print("\nThanks for playing! ")
        break
    else:
        print("\nThink you're tough enough? ")
    # clear the old game
    os.system("cls")
