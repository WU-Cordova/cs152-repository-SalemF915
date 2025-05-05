

#is a Array
class menu:

    def __init__(self):

        self.menu = ["Soda", "Coffee", "Water", "Latte", "Milk"]

        self.prices = {"Soda": 1.25, "Coffee": 2.50, "Water": 1.00, "Latte": 3.00, "Milk": 3.00}


    def __get_item__(self, item):
        
        return self.menu[item-1]

    def item_price(self, target):
        return self.prices[str(self.menu[target ])]

    def __len__(self):
        return len(self.menu)
    

    








