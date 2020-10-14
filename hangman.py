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
        self.letters = []
        self.incorrect = 0

    def new_guess(self):
        guess = ''
        acceptable_guess = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        
        while guess not in acceptable_guess or len(guess) != 1:
            guess = input("Please enter your next guess: ").upper()
        
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
        text = ''
        for l in self.word:
            if l not in self.letters:
                text += ("_ ")
            else:
                text += (l + " ")
        print(text)
        print()

def game_over(incorrect):
    if incorrect == 10:
        clear()
        print(hangman_image.wrong(10))
        print("GAME OVER")
        print(f"The word was: {player_hand.word}")
        print(player_hand.reveal_letters())
        return True

def game_win(letters, word): ### not working correctly
    for w in word: ### showing true as soon as first letter is found, so winning early
        if w in letters:
            print(player_hand.word)
            return True
        else:
        	return False

def clear():
    os.system('cls' if os.name=='nt' else 'clear')


### GAME PLAY ###
#New game conditions

game_on = True

while game_on:

    game_word = new_game()
    player_hand = Hand(game_word)
    print(game_word)
    
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
        #check for game win
        if game_win(player_hand.letters, player_hand.word):
            this_game = False
            print("WINNER!! You have won, well done!!")
        #check if the game is over
        if game_over(player_hand.incorrect):
            this_game = False
            print("ThE GaMe oVeR!!!!")


    again = ''
    if again not in ('Y','N'):
        again = input("Do you want to play again? (Y or N) ").upper()
        if again == 'Y':
            game_on = True
        elif again == 'N':
            game_on = False
        else:
            print("That was not a good answer... ")
    





