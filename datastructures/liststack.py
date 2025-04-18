import os
from datastructures.istack import IStack
from typing import Generic

from datastructures.linkedlist import LinkedList,T

class ListStack(IStack[T]):
    """
    ListStack (LinkedList-based Stack)

    """

    def __init__(self, data_type:object) -> None:
        """
        Initializes the ListStack.

        Args:
            data_type (type): The type of data the stack will hold.

        """
        self.stack = []
        self.datatype = data_type
        

    def push(self, item: T):
        """
        Pushes an item onto the stack.

        Args:
            item (T): The item to push onto the stack.
        
        Raises:
            TypeError: If the item is not of the correct type.

        """
        self.stack.append(item)

    def pop(self) -> T:
        """
        Removes and returns the top item from the stack.

        Returns:
            T: The top item from the stack.
        
        Raises:
            IndexError: If the stack is empty.
        """



        _poped = self.stack[-1]
        del(self.stack[-1])




        return _poped

    def peek(self) -> T:
        """
        Returns the top item from the stack without removing it.

        Returns:
            T: The top item from the stack.
        
        Raises:
            IndexError: If the stack is empty.
        """
        return self.stack[-1]

    @property
    def empty(self) -> bool:
        """
        Checks if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        if len(self.stack) == 0:
            return True
        else:
            return False

    def clear(self):
        """
        Clears all items from the stack.
        """
        self.stack = []

    def __contains__(self, item: T) -> bool:
        """
        Checks if an item exists in the stack.

        Args:
            item (T): The item to check for.

        Returns:
            bool: True if the item exists in the stack, False otherwise.

        """
        if item in self.stack:
            return True
        else:
            return False

    def __eq__(self, other) -> bool:
        """
        Compares two stacks for equality.

        Args:
            other (ListStack): The stack to compare with.

        Returns:
            bool: True if the stacks are equal, False otherwise.

        """
        if not isinstance(other, ListStack):
            return False
        
        if len(self.stack) != len(other.stack):
            return False
        
        for i in self.stack:
            if self.stack[i] != other.stack[i]:
                return False
        
        return True


    def __len__(self) -> int:
        """
        Returns the number of items in the stack.

        Returns:
            int: The number of items in the stack.
        """
        return len(self.stack)

    def __str__(self) -> str:
        """
        Returns a string representation of the stack.

        Returns:
            str: A string representation of the stack.
        """
        raise NotImplementedError("ListStack.__str__ is not implemented.")

    def __repr__(self) -> str:
        """
        Returns a detailed string representation of the stack.

        Returns:
            str: A detailed string representation of the stack.

        """
        raise NotImplementedError("ListStack.__repr__ is not implemented.")
    

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
