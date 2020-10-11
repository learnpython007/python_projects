### BLACKJACK GAME ###
import random
import os

suits = ("Diamonds","Hearts","Spades","Clubs")
ranks = ("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace")
values = {"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":10,"Queen":10,"King":10,"Ace":(11)}

game_on = True

# DEFINE CARDS CLASS
class Cards:

    def __init__(self,rank,suit):

        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    def __str__(self):

        return f"The {self.rank} of {self.suit}"

# DEFINE DECK CLASS

class Deck:

    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                new_card = Cards(rank,suit)
                self.all_cards.append(new_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

# DEFINE CHIPS CLASS
class Chips:

    def __init__(self,start_balance=100):
		
        self.total = start_balance

    def __str__(self):
        return f"Player One has {self.total} chips remaining. "

    def win_bet(self,bet):
        self.total = self.total + bet

    def lose_bet(self,bet):
        self.total = self.total - bet

# DEFINE HAND CLASS

class Hand:

    def __init__(self):

        self.all_cards = []
        self.total_hand_value = 0
        self.aces = 0

    def add_card(self,new_cards):
        self.all_cards.append(new_cards)
        self.total_hand_value += self.all_cards[-1].value

        if new_cards.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self): 
        while self.total_hand_value > 21 and self.aces:
            self.total_hand_value = self.total_hand_value - 10
            self.aces = self.aces - 1

def take_bet(balance): 
    bet = "Nil"
    acceptable_bet = range(1,101)

    print(f"Your balance is: {balance}. ")
    while bet not in acceptable_bet or balance < bet:
        try:
            bet = int(input("How much do you want to bet? (max bet 100) "))
        except:
            print("That was not an integar value, try again! ")
    return bet

def hit(deck, hand):
    hitting = True

    while hitting:
        hit_again = input("Do you want to hit? (Y or N) ")
        if hit_again.upper() == 'N':
            hitting = False
        elif hit_again.upper() == 'Y':
            player_one_hand.add_card(new_deck.deal_one())
            player_one_hand.adjust_for_ace()
            print(f'The card delt to Player One was {player_one_hand.all_cards[-1]} \nPlayer one sum of cards: {player_one_hand.total_hand_value}. ')
            if player_one_hand.total_hand_value > 21:
                print("BUST!!")
                hitting = False
                return "BUST"
        else:
            print("Type Y or N. ")

def show_some(): 
    print(f"The dealer has {dealer.all_cards[0]} and ***. ")
    print(f"Player One has {player_one_hand.all_cards[0]} and {player_one_hand.all_cards[1]}. ")

def show_all(): 
    print(f"The dealer has {dealer.all_cards[0]} and {dealer.all_cards[1]}. Total value: {dealer.total_hand_value}")

def player_loses(bet): 
    # take bet, remove from chip count
    balance.lose_bet(bet)

def player_wins(bet): 
    balance.win_bet(bet)

def push(): 
    print("Push, your money has been returned. ")

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

###create and shuffle new deck
new_deck = Deck()
new_deck.shuffle()

###Add starting chips
balance = Chips(10)

while game_on:

    ###Place new bet
    betting = True
    while betting:
        new_bet = take_bet(balance.total)
        print(f'The amount bet was {new_bet}.')

        ### Create new hands for dealer and player
        player_one_hand = Hand()
        dealer = Hand()
        player_one_hand.add_card(new_deck.deal_one())
        dealer.add_card(new_deck.deal_one())
        player_one_hand.add_card(new_deck.deal_one())
        dealer.add_card(new_deck.deal_one())
        print(player_one_hand.aces)
        ### Show players hand and part of dealers
        show_some()
		
        ### Players turn
        print(f'Player one sum of cards: {player_one_hand.total_hand_value}. ')
		
        ### HITTING
        player_hit = hit(new_deck,player_one_hand)
        if player_hit == "BUST":
            player_loses(new_bet)
            betting = False
        else:
            show_all()
            # Dealer draws cards up until 17 or going bust.
            while dealer.total_hand_value < 17:
                dealer.add_card(new_deck.deal_one())
                dealer.adjust_for_ace()
                print(f"The dealer drew a {dealer.all_cards[-1]}")
                print(f"The dealers hand is worth {dealer.total_hand_value}")

            # Dealer goes bust
            if dealer.total_hand_value > 21:
                print("Dealer has gone bust! You win!")
                player_wins(new_bet)
                break

            # Player wins
            elif dealer.total_hand_value <= 21 and dealer.total_hand_value < player_one_hand.total_hand_value:
                print("Player One has won!")
                player_wins(new_bet)
                break

            # Dealer wins
            elif dealer.total_hand_value <= 21 and dealer.total_hand_value > player_one_hand.total_hand_value:
                print("Dealer has won, you lose!")
                player_loses(new_bet)
                break
            #Push
            elif dealer.total_hand_value == player_one_hand.total_hand_value:
                push()
                break
		
            betting = False
    print(f"Current balance: {balance.total} ")
    print(f'There are {len(new_deck.all_cards)} cards remaining in the current deck. ')
	
    if balance.total == 0:
        print("You have no balance remaining. GAME OVER! ")
        game_on = False
        break
	### create a new deck and reshuffle when deck gets below 20 cards. 
    if len(new_deck.all_cards) < 20:
        new_deck = Deck()
        new_deck.shuffle()
        print("The deck has been reshuffled. ")
    
	#PLAY ON
    play_on = input("Do you want to play on? (Y or N) ")
    if play_on.upper() == "N":
        # clear the screen
        clear()
        game_on = False
    elif play_on.upper() == "Y":
        # clear the screen
        clear()
        continue
    else:
        print("That was not Y or N. ")




