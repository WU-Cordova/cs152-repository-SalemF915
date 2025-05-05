from dataclasses import dataclass

@dataclass
class Order:
    name: str
    drink: str
    cost: float
    #allows for customers to input special things with their drink(oat milk, no sugar, etc)
    custom: str
