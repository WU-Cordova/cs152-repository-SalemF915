import os

from datastructures.array import Array, T
from datastructures.istack import IStack

class ArrayStack(IStack[T]):
    ''' ArrayStack class that implements the IStack interface. The ArrayStack is a 
        fixed-size stack that uses an Array to store the items.'''
    
    def __init__(self, max_size: int = 0, data_type=object) -> None:
        ''' Constructor to initialize the stack 
        
            Arguments: 
                max_size: int -- The maximum size of the stack. 
                data_type: type -- The data type of the stack.       
        '''
        #initalizes the stack, and sets the max stack
        self._maxstack = max_size
        self._stack = []
        self.tracker = 0
        #self._stacktop = self._stack[0]



    def push(self, item: T) -> None:
        if len(self._stack) < self._maxstack:
            self._stack.append(item)
        else:
            raise IndexError("as")

    def pop(self) -> T:
       test = self._stack[-1]

       del self._stack[-1]



       return test

    def clear(self) -> None:
       self._stack = []
    @property
    def peek(self) -> T:
       return self._stack[-1]

    @property
    def maxsize(self) -> int:
        ''' Returns the maximum size of the stack. 
        
            Returns:
                int: The maximum size of the stack.
        '''
        return len(self._stack)
 
    @property
    def full(self) -> bool:
        ''' Returns True if the stack is full, False otherwise. 
        
            Returns:
                bool: True if the stack is full, False otherwise.
        '''
        if len(self._stack) == self.maxsize:
            return True
        return False

    @property
    def empty(self) -> bool:
        if len(self._stack) == 0:
            return True
        return False
    def __eq__(self, other: object) -> bool:
       
       if self._stack == other:
           return True
       else:
           return False

    def __len__(self) -> int:
       return len(self._stack)
    
    def __contains__(self, item: T) -> bool:
       if item in self._stack:
           return True
       else:
           return False

    def __str__(self) -> str:
        return str([self._stack[i] for i in range(self.maxsize)])
    
    def __repr__(self) -> str:
        return f"ArrayStack({self.maxsize}): items: {str(self)}"
    
if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')

