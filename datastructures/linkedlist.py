from __future__ import annotations

from dataclasses import dataclass
import os
from typing import Optional, Sequence
from datastructures.ilinkedlist import ILinkedList, T


class LinkedList[T](ILinkedList[T]):

    @dataclass
    class Node:
        data: T
        next: Optional[LinkedList.Node] = None
        previous: Optional[LinkedList.Node] = None

    def __init__(self, data_type: type = object) -> None:
        self.data_type = data_type

        self.head = None
        self.count = 0
        #self.head: Optional[LinkedList.Node] = None



    @staticmethod
    def from_sequence(sequence: Sequence[T], data_type: type=object) -> LinkedList[T]:

        _linked_list = LinkedList(data_type) #creates a empty linked list

        for i in sequence:
            

            #uses the function below to append items towards the linked list
            _linked_list.append(i)
        
        return _linked_list
            




    def append(self, item: T) -> None:
        if not isinstance(item, int):
            raise TypeError("Test type error, not a object")

        new_node = LinkedList.Node(item)
        

        if self.head is None:
            self.head = new_node #if linked list is empty, makes the new node the head
            self.count += 1
            return 
        
        #traverses to end of the list
        current = self.head


        while current.next:
            current = current.next

        current.next = new_node #sets the next node as new node


        new_node.previous = current #sets new node previous as the current
        #-> important for 2double linked lists
        self.count += 1





    def prepend(self, item: T) -> None:
        self.count += 1
        new_node = LinkedList.Node(item) #creates new node of data
        new_node.next = self.head # puts the next node as the head
        self.head = new_node # puts node at the head


    def insert_before(self, target: T, item: T) -> None:

        self.count += 1
        
        #creates the Node
        new_node = LinkedList.Node(item)
        

        #traveres the linked list
        current = self.head

        #while the current exists
        while current:

            if current.data == target:

                ## 0, 1, 2, 3
                #Current is 1
                prev_node = current.previous # retrieves the previous node


                if prev_node is None:
                    #happens when we are inserting before head
                    new_node.next = self.head
                    self.head.previous = new_node
                    self.head = new_node
                else:

                    prev_node.next = new_node # establishes the next node of the prevois node , to be the node we want to put in

                    new_node.previous = prev_node #sets the previous node of the new node to be the previous node
                    new_node.next = current 
                    current.previous = new_node
                return 
            
            current = current.next
        raise ValueError("Linked list does not have target value")

        

    def insert_after(self, target: T, item: T) -> None:
        self.count += 1

        new_node = LinkedList.Node(item)

        current = self.head

        while current:

            if current.data == target:

                ## 0, 1, 2, 3
                #Current is 1
                next_node = current.next # retrieves the next node


                if next_node is None:
                    #happens when we are inserting before head
                    current.next = new_node
                    new_node.previous = current
                else:

                    new_node.next = current.next # establishes the next node of the prevois node , to be the node we want to put in

                    new_node.previous = current #sets the next node of the new node to be the previous node
                    current.next = new_node
                return 
            
            current = current.next

        raise ValueError("Insert after not found")

    def remove(self, item: T) -> None:
        current = self.head
        while current:

            if current.data == item:
                if current.previous:
                    current.previous.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.previous = current.previous
                else:
                    current = current.previous

                self.count -= 1

                return
                






            current = current.next
        raise ValueError("Remove not found")

    def remove_all(self, item: T) -> None:
        current = self.head
        while current:

            if current.data == item:
                if current.previous:
                    current.previous.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.previous = current.previous
                else:
                    current = current.previous

                self.count -= 1
                


                if current.next is None:
                    return



            current = current.next
        raise ValueError("Remove not found")





    def pop(self) -> T:
        

        current = self.head
        if current:
            while current:
                if current.next is None:
                    self.count -= 1
                    current.previous.next is None


                    return current.data
                
                current = current.next
        raise IndexError("Test pop is empty")
            



    def pop_front(self) -> T:

        current = self.head

        if current is not None:

            current.next.previous = None
            self.count -= 1

            return current.data
        raise IndexError("Test pop front is empty")



    @property
    def front(self) -> T:

        if self.head is None:
            raise IndexError("Linked List is empty")

        #return self.head.data (my way of returning the front)
        current = self.head
        return current.data



    @property
    def back(self) -> T:
        if self.head is None:
            raise IndexError("Back ")
        
        current = self.head
        while current.next:
            current = current.next
        return current.data


    @property
    def empty(self) -> bool:
        current = self.head

        if current:
            return False
        else:
            return True

    def __len__(self) -> int:

        return self.count

    def clear(self) -> None:
        self.count = 0
        current = self.head

        while current:
            next_node = current.next
            current.previous = None
            current.next = None
            current = next_node
        
        self.head = None


    def __contains__(self, item: T) -> bool:
        current = self.head
        while current:
            if current.data == item:
                return True
            current = current.next
        return False

    def __iter__(self) -> ILinkedList[T]:
        current = self.head
        while current:
            yield current.data
            current = current.next


    def __next__(self) -> T:
        raise NotImplementedError("LinkedList.__next__ is not implemented")
    
    def __reversed__(self) -> ILinkedList[T]:

        current = self.head

        while current.next:
            if current.next is None:
                return
            
            current = current.next

        #interate from the tail all the way back to the head
        while current :
            yield current.data

            current = current.previous










    
    def __eq__(self, other: object) -> bool:

        if not isinstance(other, LinkedList):
            raise TypeError("Not a linked list")
        
        if self.count != other.count:
            return False

        current = self.head

        other_cur = other.head

        while current:
            if current.data != other_cur.data:
                return False
            current = current.next
            other_cur = other_cur.next
        
        return True





    def __str__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return '[' + ', '.join(items) + ']'

    def __repr__(self) -> str:
        
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
            
        return f"LinkedList({' <-> '.join(items)}) Count: {self.count}"


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
