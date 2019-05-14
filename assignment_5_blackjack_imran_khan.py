"""
    Assignment Number 5 BLACKJACK
"""
import random
from random import shuffle
import sys
import os

def main():
    """
    --------------------------------------------------------------------------------------
    The possible card values range from 1 to 10 and, unlike a real deck, the probability of
    drawing a card is equal
    The game begins by dealing two visible cards to the player (face up), and two cards
    to the dealer. However, in the case of the dealer,
    one card is visible to other players while the other is hidden.
    The player decides whether to "hit" (draw another card), or "stand" which ends their turn.
    The player may hit any number of times. Should the total of the cards exceed 21,
    the player "busts" and loses the game to the dealer.
    If the player reaches 21, the player stands
    The dealer's turn begins by revealing the hidden card
    The dealer must hit if the total is 16 or less, and must stand if the value is 17 or more
    The dealer wins all ties (i.e. if both the dealer and the player reach 21, the dealer wins)
    The program indicates who the winner is and asks to play again.

    EXTRA
    Ace which can either take the value of 1 or 11. Let's say the user is dealt a 10 and an ace,
    that would equal 21. If the user has 3, gets an ace, the total is 14. If the user hits and
    busts, then the ace is considered to have the value of 1.
    """


def deal_deck():
    """
        Cut the deal and shuffle the cards
    """
    #deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    deck = ['A', '2', '3']
    shuffle(deck)
    return deck

os.system('CLS')
while True:
    print("\n\n\nWelcome to BlackJack\n\n")
    print(f"{'':-<50}")
    ANS = input("Please enter y or n to start a new game y/n: ")

    if ANS in ('Y', 'YES', 'y', 'Yes', 'yes'):
        PLAYER_DECK = []
        DEALER_DECK = []
        while len(PLAYER_DECK) != 2:
            PLAYER_DECK.append(random.choice(deal_deck()))
            if len(PLAYER_DECK) == 2:
                if PLAYER_DECK[0] in 'A':
                    PLAYER_DECK.pop()
                    print("\n********************************************\n")
                    print("\n* ACE!!!!!!, Player takess 10             *\n")
                    print("\n*********************************************\n")
                    PLAYER_DECK.append('10')
                if  PLAYER_DECK[0] == 'A':
                    PLAYER_DECK.pop(0)
                    print("\n********************************************\n")
                    print("\n* ACE!!!!!, Player takess 10             *\n")
                    print("\n*********************************************\n")
                    PLAYER_DECK.append('10')
                elif PLAYER_DECK[1] == 'A':
                    PLAYER_DECK.pop(1)
                    print("\n********************************************\n")
                    print("\n* ACE!!!!!!!!, Player takess 10             *\n")
                    print("\n*********************************************\n")
                    PLAYER_DECK.append('10')
                else:
                    pass
                PLAYER_CARD1 = int(PLAYER_DECK[0])
                PLAYER_CARD2 = int(PLAYER_DECK[1])
                PLAYER_DECKER = map(int, PLAYER_DECK)
                TOT_PLAYER = sum(PLAYER_DECKER)
                print(f"\n\nYou draw {PLAYER_CARD1} and {PLAYER_CARD2}.", end="")
                print(f" Your total is {TOT_PLAYER}")
        while len(DEALER_DECK) != 2:
            DEALER_DECK.append(random.choice(deal_deck()))
            if len(DEALER_DECK) == 2:
                if DEALER_DECK[0] in 'A':
                    DEALER_DECK.pop()
                    DEALER_DECK.append('10')
                if  DEALER_DECK[0] == 'A':
                    DEALER_DECK.pop(0)
                    DEALER_DECK.append('10')
                elif DEALER_DECK[1] == 'A':
                    DEALER_DECK.pop(1)
                    DEALER_DECK.append('10')
                else:
                    pass
                DEALER_CARD1 = int(DEALER_DECK[0])
                DEALER_CARD2 = int(DEALER_DECK[1])
                DEALER_DECKER = map(int, DEALER_DECK)
                TOT_DEALER = sum(DEALER_DECKER)
                print(f"\n\nThe dealer draw {DEALER_CARD1} and a hidden card.\n ")
        while True:
            RESPONSE = input("\nHit or Stand? (h/s): ")
            if RESPONSE in ('H', 'h', 'HIT', 'hit', 'Hit'):
                PLAYER_DECK.append(random.choice(deal_deck()))
                if PLAYER_DECK[-1] == 'A':
                    if (TOT_PLAYER + 10) > 21:
                        PLAYER_DECK.pop()
                        print("\n**************************************************\n")
                        print("\n* You HIT an ACE, but treat it as 1 then 10 ;)!!  *\n\n")
                        print("\n**************************************************\n")
                        PLAYER_DECK.append('1')
                    elif (TOT_PLAYER + 10) <= 21:
                        PLAYER_DECK.pop()
                        print("\n**************************************************\n")
                        print("\n* You HIT an ACE, Wohoo!! 10 Points;)!!           *\n")
                        print("\n**************************************************\n")
                        PLAYER_DECK.append('10')
                PLAYER_DECKER = map(int, PLAYER_DECK)
                TOT_PLAYER = sum(PLAYER_DECKER)
                if TOT_PLAYER == 21:
                    print(f"\nHit! You with draw a {PLAYER_DECK[-1]} ", end="")
                    print(f"Your total is {TOT_PLAYER}")
                    print(f"\nThe dealer's reveals the hidden card of {DEALER_CARD2} ", end="")
                    print(f"and has a total of {DEALER_CARD1 + DEALER_CARD2}")
                    break
                elif TOT_PLAYER > 21:
                    break
                elif TOT_PLAYER < 21:
                    print(f"\nHit! You with draw a {PLAYER_DECK[-1]} ", end="")
                    print(f"Your total is {TOT_PLAYER} ")
            elif RESPONSE in ('S', 's', 'Stand', 'STAND', 'stand'):
                print("\nYou have decided to Stand: \n")
                print(f"\nThe dealer's reveals the hidden card of {DEALER_CARD2} ", end="")
                print(f"and has a total of {TOT_DEALER}")
                break
            else:
                print("\nPlease enter the right choice of 'h' or 's'\n\n")


        while True:
            if TOT_PLAYER > 21:
                print(f"\n\nGREEDY CALL....YOU BUSTED....!!!!!!.")
                break
            elif TOT_DEALER <= 16:
                DEALER_DECK.append(random.choice(deal_deck()))
                if DEALER_DECK[-1] == 'A':
                    if (TOT_DEALER + 10) > 21:
                        DEALER_DECK.pop()
                        PLAYER_DECK.append('1')
                    elif (TOT_DEALER + 10) <= 21:
                        DEALER_DECK.pop()
                        DEALER_DECK.append('10')
                DEALER_DECKER = map(int, DEALER_DECK)
                TOT_DEALER = sum(DEALER_DECKER)
                print(f"\nHit! The dealer now has a total of {TOT_DEALER}")
            elif 17 <= TOT_DEALER <= 21:
                print("\nDealer has decided to STAND...\n")
                break
            else:
                break
        if (TOT_DEALER == 21 and TOT_PLAYER == 21):
            print(f"\nYour total is {TOT_PLAYER} and dealer's total is {TOT_DEALER}\n")
            print("\nThe dealer win!!")

        if TOT_DEALER > 21:
            print(f"\nGREEDY Dealer BUSTED....!!!!! \n")
            print(f"\nYour total is {TOT_PLAYER} and dealer's total is {TOT_DEALER}\n")
            print(" YOU WIN!!!")
        elif  TOT_DEALER < TOT_PLAYER <= 21:
            print(f"\nYour total is {TOT_PLAYER} and dealer's total is {TOT_DEALER}\n")
            print("\nYou win!\n")
        else:
            print(f"\nYour total is {TOT_PLAYER} and dealer's total is {TOT_DEALER}\n")
            print("Dealer WIN!!!! ")
    else:
        if ANS in ('n', 'NO', 'N', 'No', 'no'):
            print("\nThanks for stoping By, though Gamling is NEVER Good.. \n")
            sys.exit()
        else:
            print("\n\nPlease Enter Yes or No.....\n")

if __name__ == '__main__':
    main()
