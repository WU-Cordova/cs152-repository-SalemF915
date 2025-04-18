import random
from character import Character
from charactertype import CharacterType




class Game:
    def __init__(self, player1: Character, player2: Character) -> None:
        """ Constructor for the Game class. Sets the players to instance variables.
        Args:   
            player1 (Character): The first player.
            player2 (Character): The second player.
        """
        self.alice = player1

        self.bob = player2

        self.number = 0



    def attack(self, attacker: Character, defender: Character) -> None:
        """ Attacks the defender. Algorithm: 
            1. Roll a random number between 1 and 6 for the attack.
            2. Subtract the attack value from the defender's health.
            3. If the defender's health is less than or equal to 0, they are defeated.
            4. Print the result of the attack.
        Args:
            attacker (Character): The attacker.
            defender (Character): The defender. 
        """
        self.number = random.randint(1,6)

        print(attacker.name, "attacks!!!")

        defender.health -= self.number
        if defender.health <= 0:
            print("DEFEATED, BATTLE OVER")

        
        print(defender.name ," took ",self.number ,"damage and has ", defender.health, " health left")


        


    def start_battle(self) -> None:
        """ Starts the battle between the two players. Algorithm: 
            1. While both players are alive, do the following:
                1.1. Player 1 attacks Player 2.
                1.2. If Player 2 is defeated, break the loop.
                1.3. Player 2 attacks Player 1.
                1.4. If Player 1 is defeated, break the loop.
            2. Print the result of the battle.
        """
        while self.alice.health > 0 and self.bob.health > 0:
            self.attack(self.alice, self.bob)
            if self.bob.health > 0:
                self.attack(self.bob, self.alice)
            else:
                break










