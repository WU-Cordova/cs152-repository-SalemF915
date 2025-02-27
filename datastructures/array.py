# datastructures.array.Array

""" This module defines an Array class that represents a one-dimensional array. 
    See the stipulations in iarray.py for more information on the methods and their expected behavior.
    Methods that are not implemented raise a NotImplementedError until they are implemented.
"""

from __future__ import annotations
from collections.abc import Sequence
import os
from typing import Any, Iterator, overload
import numpy as np
from numpy.typing import NDArray


from datastructures.iarray import IArray, T


class Array(IArray[T]):  


    def __init__(self, starting_sequence: Sequence[T]=[], data_type: type=object) -> None: 
        

        self.sequence = starting_sequence

        self.data_type = data_type

        if not isinstance(starting_sequence, Sequence):
            raise ValueError("ignore")
        
        if not all(isinstance(item, self.data_type) for item in self.sequence):
            raise TypeError("ignore")
        

        self.car = np.array(self.sequence, dtype=self.data_type)
        





    @overload
    def __getitem__(self, index: int) -> T: ...
    @overload
    def __getitem__(self, index: slice) -> Sequence[T]: ...
    def __getitem__(self, index: int | slice) -> T | Sequence[T]:
        if isinstance(index, slice):
            
            return Array(self.car[index])

        if len(self.car) < index:
            raise IndexError("Index out of bounds")

        else:
        
            return self.car[index]
    
    def __setitem__(self, index: int, item: T) -> None:
        if type(item) != type(self.car):
            raise TypeError("Wrong data type")
        else:
            self.car[index] = item


    def append(self, data: T) -> None:
        self.car = np.append(self.car, data)

    def append_front(self, data: T) -> None:
        raise NotImplementedError('Append front not implemented.')

    def pop(self) -> None:
        raise NotImplementedError('Pop not implemented.')
    
    def pop_front(self) -> None:
        raise NotImplementedError('Pop front not implemented.')

    def __len__(self) -> int: 
        length = len(self.car)
        return length

    def __eq__(self, other: object) -> bool:

        for items in range(len(self.car)):
            if self.car[items] != other[items]:
                return False
        return True
        
    
    def __iter__(self) -> Iterator[T]:
        return iter(self.car)

    def __reversed__(self) -> Iterator[T]:
        return self.car[::-1]

    def __delitem__(self, index: int) -> None:
        self.car = np.delete(self.car, self.car[index])

    def __contains__(self, item: Any) -> bool:

        if item in self.car:
            return True
        else:
            return False


    def clear(self) -> None:
        self.car = np.array([], dtype=self.data_type)

    def __str__(self) -> str:

        return str(self.car)
    
    def __repr__(self) -> str:
        
        return f'Array {self.__str__()}, Logical: {self.__len__()}, Physical: {len(self.car)}, type: {self.data_type}'
    

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')