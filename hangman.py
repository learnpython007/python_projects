### HANGMAN GAME ###
import os
import random
import hangman_image

#Welcome
print("Welcome to Hangman")
print()
print("___________")
print("|          |")
print("|         ( )")
print("|         /|\\")
print("|          |")
print("|         / \\")
print("|")
print("|_____________")
print()
print("This is a small bit about how the game will play... blah blah blah")

file = open('word_list.txt','r')
word_list = []

for words in file:
    word_list.append(words)

def new_game():
    return word_list[random.randrange(len(word_list))].upper()

class Hand:
    
    def __init__(self,word):
        self.word = word
        self.letters = ['']
        self.incorrect = 0

    def new_guess(self):
        guess = '0'
        acceptable_guess = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        
        while guess not in acceptable_guess or len(guess) != 1:
            guess = input("What letter would you like to try? ").upper()
        
        #if already in letters list (already guessed letter)
        if guess in self.letters:
            clear()
            print(f"{guess} has already been guessed, try again. ")
        #if correct (not is letters list but in word)
        if (guess in self.word) and (guess not in self.letters):
            self.letters.append(guess)
            clear()
            print(f"{guess} was in the word! ")
        #if incorrect (not in letters list and not in word)
        if (guess not in (l for l in self.word)) and (guess not in self.letters):
            clear()
            print(f"{guess} was not in the word. ")
            self.letters.append(guess)
            self.incorrect += 1

    def reveal_letters(self):
        print()
        for l in self.word:
            if l not in self.letters:
                print("_ ")
            else:
                print(l + " ")

def game_over(incorrect):
    if incorrect == 10:
        clear()
        print(hangman_image.wrong(10))
        print("GAME OVER")
        print(f"The word was: {player_hand.word}")
        print(player_hand.reveal_letters())
        return True

def game_win(letters, word):
    if letters == word:
        return True


def clear():
    os.system('cls' if os.name=='nt' else 'clear')


### GAME PLAY ###
#New game conditions

game_on = True

while game_on:

    game_word = new_game()
    player_hand = Hand(game_word)
    
    #While loop for playing current game
    this_game = True
    while this_game:
        #show the blanks or letters of the word
        print(player_hand.reveal_letters())
        #player takes a new guess
        player_hand.new_guess()
        #show the new hangman board
        print(hangman_image.wrong(player_hand.incorrect))
        #show incorrect guesses and letters that have been used
        print(player_hand.incorrect,"wrong guesses, letters that have already been guessed are", player_hand.letters)

        #check if the game is over
        if game_over(player_hand.incorrect):
        	this_game = False
        	print("ThE GaMe oVeR!!!!")
    game_on = False
    # add scrpit for game on to play again





