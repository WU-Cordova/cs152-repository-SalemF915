import random

class CreateAr:
    #Sets all the bacteria in the array2D
    def set_bact(self):
        for r in range(len(self.arr2D)):
            for c in range(len(self.arr2D[0])):
                ranmize = random.randint(1,2)
                if ranmize == 1:
                    self.arr2D[r][c] = "X"
                else:
                    pass
        
    #used to set whether or not a cell has bacteria

    def get_bact_arr(self):
        return self.arr2D


    def __init__(self, rows, cols):
        self.r = rows
        self.c = cols
        self.arr2D = [["_"] * cols for _ in range(rows)]
