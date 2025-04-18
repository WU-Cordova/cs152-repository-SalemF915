import random
#this class handles the main game
class Game:
    def __init__(self, deck):
        self.deck_o_cards = deck
        self.base_d_size = 52
        self.draw_state = 0


        #gets a card for player to draw
        self.randomnum = random.randint(1,52)

        #the value of cards the player has
        self.total = 0
        

        #total of cards the dealer has
        self.dealer_total = 0
        self.fake_total = 0

        self.keys = list(self.deck_o_cards.keys())


        self.max_randint_val = 52


        self.card_player = []
        self.card_dealer = []

    def start(self):
        
        print("WELCOME TO BLACKJACK!!!\nInital deal: ")


        print("Player Hand: ")
        for i in range (2):
            #randomizes the card that will be drawn
            self.random_card()



            #prints the value of the card drawn
            #print(self.deck_o_cards[self.keys[self.randomnum]])
            print(self.keys[self.randomnum])
            self.total += self.deck_o_cards[self.keys[self.randomnum]]

            self.card_player.append(self.keys[self.randomnum])
            #removes card from play
            self.keys.pop(self.randomnum)
            self.max_randint_val -= 1

        print("Player Score: ", self.total)
        print("Cards: ", self.card_player)



        print("\nDealer's Hand: ")
        for i in range(2):

            self.random_card()

            if i == 1:
                print("hidden")
                self.dealer_total += self.deck_o_cards[self.keys[self.randomnum]]               
            else:

                print(self.keys[self.randomnum])
                self.dealer_total += self.deck_o_cards[self.keys[self.randomnum]]
                self.fake_total += self.deck_o_cards[self.keys[self.randomnum]]


            self.card_dealer.append(self.keys[self.randomnum])
            self.keys.pop(self.randomnum)
            self.max_randint_val -= 1  
        
        print("Dealer Score: ", self.fake_total, " + ???")
        while self.draw_state == 0:
            self.draw_card()







    def random_card(self):
        self.randomnum = random.randint(1,self.max_randint_val)

    def draw_card(self):
        print("Would you like to (H)it or (S)tay?")

        HitorStay = input()
        if HitorStay.upper() == "S":

            while self.dealer_total < 17 and self.dealer_total < 21:
                self.random_card()
                self.dealer_total += self.deck_o_cards[self.keys[self.randomnum]]
                self.card_dealer.append(self.keys[self.randomnum])
                self.keys.pop(self.randomnum)
                self.max_randint_val -= 1
                if self.dealer_total >= self.total:
                    break

            print("Dealer's hand :", self.card_dealer)
            print("Dealer Score: ", self.dealer_total)

            self.draw_state += 1


        elif HitorStay.upper() == "H":
            self.random_card()

            print(self.keys[self.randomnum])
            self.total += self.deck_o_cards[self.keys[self.randomnum]]


            self.card_player.append(self.keys[self.randomnum])
            #removes card from play
            self.keys.pop(self.randomnum)
            self.max_randint_val -= 1
            print("Dealer Score: ", self.fake_total, " + ???")

        print("Player Score: ", self.total)
        if self.total > self.dealer_total or self.dealer_total > 21:
            "DEALER BUST, YOU WIN!!!"
        


        if self.total > 21:
            print("BUST\nDEALER WINS")
            self.draw_state += 1
        
