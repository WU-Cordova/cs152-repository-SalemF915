
class report:

    def __init__(self, sales):

        self.sales = sales
        self._menu = ["Soda","Coffee","Water","Lattee","Milk"]

        self.sales = sum(self.sales, [])

        print(self.sales)

        self.day_sales()



    def total_sale(self, target):

        _cost = 0

        for i in range(len(self.sales)):
            if self.sales[i].drink == self._menu[target]:
                _cost += self.sales[i].cost
                self.revenue += self.sales[i].cost

        return _cost
    
    def quan_sold(self, target):

        _tot_sold = 0
        for i in range(len(self.sales)):
            if self.sales[i].drink == self._menu[target]:
                _tot_sold += 1

        return _tot_sold
    


    

    
    def day_sales(self):
        self.revenue = 0

        print("End of Day Report: \n--------------\n")
        print("Drink Name       Quantity Sold   Total Sale")

        for i in range(5):
            print(self._menu[i],"          ",self.quan_sold(i),"               $",self.total_sale(i))
        print("Total revenue:          $",self.revenue)





        
