
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


    def count_neighbors(self, arr, r, c) -> int:
        counter = 0
        #counts upper left
        if r - 1  != -1 and c - 1 != -1 and arr[r - 1][c - 1] == "X":
            counter += 1
        #counts upper
        if r - 1  != -1 and arr[r - 1][c] == "X":
            counter += 1
        #counts upper right
        if r - 1  != -1 and c + 1 > len(arr[0]) and arr[r - 1][c + 1] == "X":
            counter += 1
        #counts left
        if c - 1 != -1 and arr[r][c - 1] == "X":
            counter += 1
        #counts right
        if c + 1 > len(arr[0]) and arr[r][c + 1] == "X":
            counter += 1
        #count lower left
        if r + 1  > len(arr) and c - 1 != -1 and arr[r + 1][c - 1] == "X":
            counter += 1
        #count lower
        if r + 1  > len(arr) and arr[r + 1][c] == "X":
            counter += 1
        #count right lower
        if r + 1  > len(arr) and c + 1 > len(arr[0]) and arr[r + 1][c + 1] == "X":
            counter += 1




        return counter




#used to simulate the grid
    def sim(self, arr):
        new_arr = arr
        count = 0
        for r in range(len(arr)):
            for c in range(len(arr[r])):
                count = self.count_neighbors(arr,r,c)
                if count <= 1:

                    new_arr[r][c] = "_"
                if count == 3:
                    new_arr[r][c] = "X"
                if count >= 4:
                    new_arr[r][c] = "_"

                print("arr",r ,c, " counts ", count, "neighbors")
                count = 0
        return new_arr
        


                



                    

    def __init__(self, arr):
        self.print_grid(arr)

        new_arr = self.sim(arr)

        self.print_grid(new_arr)







    




