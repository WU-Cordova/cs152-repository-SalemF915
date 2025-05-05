import numpy as np
from CreateArray import *
from Simulation import *

####starts game
print("How many rows and columns do you want int the simulation?")
r = input("Rows:\n")
c = input("Columns:\n")

Array = CreateAr(int(r),int(c))
Array.set_bact()
sim_ar = Array.get_bact_arr()
#Tester is used as a debug to test current state of "CreateArray.py"


Simulate(sim_ar)