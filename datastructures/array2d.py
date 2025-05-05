from __future__ import annotations
import os
from typing import Iterator, Sequence

from datastructures.iarray import IArray
from datastructures.array import Array
from datastructures.iarray2d import IArray2D, T
import numpy as np


class Array2D(IArray2D[T]):

    class Row(IArray2D.IRow[T]):
        def __init__(self, row_index: int, array: IArray, num_columns: int) -> None:

            self.row_index = row_index
            self.col_index = num_columns
            self.arr = array

        def __getitem__(self, column_index: int) -> T:
            raise NotImplementedError('Row.__getitem__ not implemented.')
        
        def __setitem__(self, column_index: int, value: T) -> None:
            raise NotImplementedError('Row.__setitem__ not implemented.')
        
        def __iter__(self) -> Iterator[T]:
            raise NotImplementedError('Row.__iter__ not implemented.')
        
        def __reversed__(self) -> Iterator[T]:
            raise NotImplementedError('Row.__reversed__ not implemented.')

        def __len__(self) -> int:
            return self.num_columns
        
        def __str__(self) -> str:
            return f"[{', '.join([str(self[column_index]) for column_index in range(self.num_columns)])}]"
        
        def __repr__(self) -> str:
            return f'Row {self.row_index}: [{", ".join([str(self[column_index]) for column_index in range(self.num_columns - 1)])}, {str(self[self.num_columns - 1])}]'


    def __init__(self, starting_sequence: Sequence[Sequence[T]]=[[]], data_type=object) -> None:


        #makes sure all items passed through are sequences
        if type(starting_sequence) is int:
            raise ValueError("must be a sequence of sequences")
        if type(starting_sequence) is str:
            raise ValueError("must be a sequence of sequences")
        if type(starting_sequence) is dict:
            raise ValueError("must be a sequence of sequences")
        


        #tests to make sure all items are the same type
        all_items = []
        for r in range(len(starting_sequence)):
            for c in range(len(starting_sequence[r])):
                all_items.append(starting_sequence[r][c])

        for i in range(len(all_items) - 1):
            if type(all_items[i]) != type(all_items[i + 1]):
                raise ValueError("All items must be of the same type")

        


        for r in range(len(starting_sequence) ):
            if len(starting_sequence[r]) != len(starting_sequence[r + 1]):
                raise ValueError("must be a sequence of sequences with the same length")


        self.col = len(starting_sequence[0])
        self.rows = len(starting_sequence)

        self.test = []
        self.array2d = np.array(starting_sequence)


    @staticmethod
    def empty(rows: int=0, cols: int=0, data_type: type=object) -> Array2D:
        empty = [[0] * cols] * rows
        return empty

    def __getitem__(self, row_index: int) -> Array2D.IRow[T]: 

        return self.array2d[row_index]
    
    def __iter__(self) -> Iterator[Sequence[T]]: 

        return iter(self.array2d)
    
    def __reversed__(self):
        return self.array2d[::-1]
    
    def __len__(self): 
        return self.rows
                                  
    def __str__(self) -> str: 
        l = (self)
        return f'[{", ".join(f"{row}" for row in l)}]'
    
    def __repr__(self) -> str: 
        return f'Array2D {self.__num_rows} Rows x {self.__num_columns} Columns, items: {str(self)}'


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')