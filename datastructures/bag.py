from typing import Iterable, Optional
from datastructures.ibag import IBag, T

class Bag(IBag[T]):
    def __init__(self, *items: Optional[Iterable[T]]) -> None:

        #creates a emtpy dictionary/ code to reset a dict
        self._bag = {}
        self._counter = 0
        self.ex = []



        if items is not None:
            for item in items:
                self.add(item)
                self._counter += 1
                self.ex.append(item)
        

                
        print(self._bag)

    def add(self, item: T) -> None:
        if item is None:
            raise(TypeError)
        else:
            if item in self._bag:
                self._bag[item] += 1
                
            else:
                self._bag[item] = 1
                self.ex.append(item)
                
            self._counter += 1

    def remove(self, item: T) -> None:

        if item not in self._bag:
            raise(ValueError)
        
        if item in self._bag:
            self._bag[item] -= 1
            self._counter -= 1




    def count(self, item: T) -> int:
        _counter = 0
        if item in self._bag:
            _counter += self._bag[item]
        return _counter

        

    def __len__(self) -> int:
        return self._counter

    def distinct_items(self) -> Iterable[T]:
        return self.ex

    def __contains__(self, item) -> bool:
        if item in self._bag:
            return True
        else:
            return False

    def clear(self) -> None:
        
        self._bag = {}
        self._counter = 0
        self.ex = 0