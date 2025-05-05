
#will be using a Liststack to track orders

from copy import deepcopy

class Dequeue:

    def __init__(self):
        self.queue = []
        self.queue_front = None
        self.queue_back = None



    def size(self):
        return len(self.queue)

    def enqueue_front(self, item):
        #adds a item at the back of a queue (adds a new order towards the ordering system)
        self.queue.append(item)

    
    def deque(self):
        #removes element at front and it also returns that element



        if self.queue is None:
            raise IndexError("No items are in the queue")
        
        #deletes item at the front of the queue
        _item_sold = self.queue[:-1]
        del(self.queue[:-1])

        return _item_sold

    def reorder(self):
        #adds items towards the queue
        pass
    
    def get(self, item):
        return self.queue[item]


    def __str__(self):
        #prints out the order
        for i in self.queue:
            print(i, "\n")

