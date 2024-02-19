
from typing import Any
# import numpy as np
import math
import time
import timeit

def Swap1 ():
    a = 203
    b = 204
    
    # Perform the swap using XOR operations
    a = a ^ b
    b = a ^ b
    a = a ^ b
    

def Swap2():
    P = 203 
    Q = 204

    # To swap the value of two variables  
    # we will user third variable which is a temporary variable  
    temp = Q
    Q = P
    P = temp



def Swap3(): 
    P = 203 
    Q = 204

    P, Q = Q, P  

# Swap3 and Swap2 are similar, but they are better than Swap1
# In python for swap function, we use just Swap3


if __name__ == "__main__":
    # Comparison of Algorithms
    swapAlgorithms = [Swap1, Swap2, Swap3]
    for swap in swapAlgorithms:
        # Executing each swap algorithms for 1e6 times \
        # and calculate each algorithm execution time
        result = timeit.timeit(stmt='swap()', globals=globals(), number=1e6)
        print(f"Elapsed {result:.03f} micro secs.")
    