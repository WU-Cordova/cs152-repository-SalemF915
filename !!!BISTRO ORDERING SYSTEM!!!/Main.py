from prof import Profile
from profiletype import Profiletype

from order_sys import Order

from order_queue import Dequeue

from drink_menu import menu

from day_report import report

test_login = Profile(login="Alice", admin_type= Profiletype.ADMIN, password="PASS")

#keeps tracks of all the orders
order_list = Dequeue()


#records all the sales made that day
sales = []


#the menu of all the items the coffee place sells(uses a basic list)
drink_menu = menu()

'''
def login():

    _input = input("Please Enter Login:   ")
    if _input in users:
        

        _pass = input("Please enter password:   ")

        if logins[_input] == _pass:
            return "0"
'''

def display_menu():

    print("Bistro Menu: ")

    for i in range(drink_menu.__len__() ):
        print(i + 1,": ", drink_menu.__get_item__(i ), "$", drink_menu.item_price(i))
    
    return main()

def take_order():

    _name = input("What is the name?\n")

    _num = input("How many drinks?\n")

    _order_sum = []

    for i in range(int(_num)):
        _drink_num = (input("Enter drink number(1-5): "))



        _custom = str(input("any custom?"))


        _new_order = Order(name= _name, drink= drink_menu.__get_item__(int(_drink_num )-1), cost= drink_menu.item_price(int(_drink_num )-1), custom= _custom)


        _order_sum.append(_new_order)
    
    print("Order Summary for", _name, ":")
    for i in range(len(_order_sum)):
        print("-", _order_sum[i].drink, " - ", _order_sum[i].custom)
    
    print("Do you confirm the order?")
    _confirm = input("y/n: ")
    if _confirm == "n":
        print("Redo order or cancel?: ")
        _redo = input("r/c: ")
        if _redo == "r":

            return take_order()
        else:
            print("Order canceled: ")
            return main()
    else:
        for i in range(len(_order_sum)):
            order_list.enqueue_front(_order_sum[i])
        
        return main()



def view_order():

    print("Open Orders: ")
    for i in range(order_list.size()):
        print(i + 1, ".", order_list.get(i).name, ":", order_list.get(i).drink, ",", order_list.get(i).custom)
    
    return main()

    
def mark_order():

    sales.append(order_list.deque())

    return main()


def end_of_day_report(s):
    report(s)
    return main()

    


def main():
    '''
    print("Hello! Welcome to Willamette's Bearcat Bistro!")
    print("LOGIN SUCESSFUl\n")
    '''


    print("Main menu:\n")
    print("1.   Display Menu\n2.   Take a new Order\n3.   View Orders\n4.   Mark Next Order as Complete\n5.   View End-of-Day Report\n6.     Exit")

    user_act = input("Enter your choice: ")

    if user_act == "1":
        display_menu()
    if user_act == "2":
        take_order()
    if user_act == "3":
        view_order()
    if user_act == "4":
        mark_order()
    if user_act == "5":
        end_of_day_report(sales)
    if user_act == "6":
        print("\nThank you for using Willamette Bistro!!! ")




main()
