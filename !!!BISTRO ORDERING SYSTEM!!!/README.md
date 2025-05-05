The data structures I choose for each of the following components are as follows.
Menu - Array
    The menu uses two basic fixed array to contain the items in the menu and the price tag for each of them. I chose to use a Array mainly because the menu does not need to be changed at all.
Customer Order - Dequeue/queue
    For the order system I used a deque system, as it would allow for more easy access in removing orders, and adding them. It would add new orders to the end and the oldest orders took priority, and when a order was complete the queue would remove that item and the next item in the queue would be assigned to be fullfilled.

Order Confirmation - Array
    For order confirmation, I created a new array that would be shown to the user, if the user was satisfied with the results then the user can confirm, and the items in the order confimration would be taken and put into the actual order deque for order processing. But other it serves as a temporary array to be disposed. 


Open Orders - Deque/queue
    For Open Orders, I would print the deque, and from that list it would arranged in a way that would tell the waitress/waiter the orders, from 1st to last to complete. 

Completed Orders - Array
    When orders completed they are removed from the deque and placed into a new array("sales"), which are then run through a class("day_report"). I choose an array as it was a very simple way to store the orders that had been completed.






***BUGS
Main bugs I found within my program are as follows
- If you attempt to Finish all orders in the queue, the last order does not go through
- If your input is not what the computer is looking for the code does not run.



***If I had more time

As of now I've already spent enough time on it but if i had more time i would have
- Corrected the login system by creating a object that would contain a user's login and password, and if the user had a ADMIN user then they would get special functions, such as creating new users, removing users, etc.
- Perhaps I would look into changing the Completed Orders into a stack, so once they are printed out or etc, they are discarded, however I would be concerned about doing this as what if I wished to try to retrieve that data or place it into a Json or CVS file.


Intructions:
run python file "Main.py"
input desired function using number 1-6


    inputing 1(Display menu)
    displays the menu before immediatly showing the main menu

    inputting 2(Takeing orders)
    First input name of customer
    enter amount of drinks the customer orders
    enter the drink number(from menu, and assuming employees remember the drink number), and enter any customizations the customer has for the drink
    confirm or deny order(if denied, choose to either cancel order altogether or have them reorder)

    inputting 3(Viewing orders)
    displays all the orders that are in queue
    the orders are listed from high priority to lowest priority(1 = current order, >1 in queue)

    inputting 4(Marking orders)
    Marks the current order as complete

    inputting 5(Viewing end of day report)
    displays the orders completed, and the revenue gotten from all orders

    inputting 6(Ends program)
    ends program


