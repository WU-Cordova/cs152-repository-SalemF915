
from Card_draw_man import Game
from BagJack_1v1 import CardsDeck

#this class handles dealing and shuffingling the deck

deck_of_cards = CardsDeck.make_deck()

i = 0 
blackjack = Game(deck_of_cards)
blackjack.start()
while i == 0:

    print("Would you like to play again?\n(Y)es or (N)o)")
    answer = input()
    if answer.upper() == "Y":
        #makes a fresh new deck
        deck_of_cards = CardsDeck.make_deck()
        blackjack = Game(deck_of_cards)
        blackjack.start()


    else:
        print("THANK YOU FOR PLAYING!!!")
        i += 1