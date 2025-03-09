import copy


class Simulate:
    def print_grid(self, arr):
        _c_len = len(arr[0])

        grid = ""
        for rows in arr:
            for items in rows:
                grid += str(items)
                _c_len -= 1
                if _c_len == 0:
                    grid += "\n"
                    _c_len = len(arr[0])
                    
        print(grid)


    def count_neighbors(self, arr, r, c) :
        counter = 0
        #counts upper left
        if ((r - 1  != -1 and c - 1 != -1 ) and arr[r - 1][c - 1] == "X"):
            counter += 1
            
        
        #counts upper
        if r - 1  != -1 and arr[r - 1][c] == "X":
            counter += 1
        
        #counts upper right
        if r - 1  != -1 and c + 1 < len(arr[0] ) and arr[r - 1][c + 1] == "X":
            counter += 1
        
        #counts left
        if c - 1 != -1 and arr[r][c - 1] == "X":
            counter += 1
        
        #counts right
        if c + 1 < len(arr[0]) and arr[r][c + 1] == "X":
            counter += 1
        
        #count lower left
        
        if r + 1  < len(arr) and c - 1 != -1 and arr[r + 1][c - 1] == "X":
            counter += 1
        #count lower
        if r + 1  < len(arr) and arr[r + 1][c] == "X":
            counter += 1
        #count right lower
        if r + 1  < len(arr) and c + 1 < len(arr[0]) and arr[r + 1][c + 1] == "X":
            counter += 1
        
        return counter




#used to simulate the grid
    def sim(self, arr):

        self.new_arr = copy.deepcopy(arr)

        count = 0

        for r in range(len(self.basearr)):
            for c in range(len(self.basearr[r])):
                count = self.count_neighbors(self.basearr,r,c)
                #print("arr",r ,c, " counts ", count, "neighbors")
                if count <= 1:

                    self.new_arr[r][c] = "_"
                if count == 3:
                    self.new_arr[r][c] = "X"
                if count >= 4:
                    self.new_arr[r][c] = "_"


                count = 0
                
        return self.new_arr

                    

    def __init__(self, arr):
        #keeps track of the current simulation
        gen = 0

        #used as a base reference for the last 2D arry input
        self.basearr = arr
        #used as a array to store data of new generation of 2D array
        self.testarr = []
        
        while self.basearr != self.testarr:
            #used as a array to store data of new generation of 2D array
            self.testarr = copy.deepcopy(self.basearr)


            #prints a grid of the array
            print("Generation: ", gen)
            self.print_grid(self.basearr)

            #creats a new array for simulation
            new_arr = self.sim(self.testarr)
            gen += 1

            #prints out the new arr after the simulation
            print("Generation: ", gen)
            self.print_grid(new_arr)

            self.basearr = copy.deepcopy(new_arr)

            if gen == 1000:
                print("Too many simulations infinate simualtion")
                break


            














    




