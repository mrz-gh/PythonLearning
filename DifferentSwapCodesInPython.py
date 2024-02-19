
from typing import Any
# import numpy as np
import math
import time
import timeit

def Swap1 ():
    P = 203 
    Q = 204
    
    # To Swap the values of two variables using XOR  
    return P > Q
    
    #print ("The Value of P after swapping: ", P)  
    #print ("The Value of Q after swapping: ", Q)  

def Swap2():
    P = 203 
    Q = 204
    
    # To Swap the values of two variables using XOR  
    # To swap the value of two variables  
    # we will user third variable which is a temporary variable  
    temp = Q
    Q = P
    P = temp
   
    
    # ("The Value of P after swapping: ", P)  
    #print ("The Value of Q after swapping: ", Q)  


def Swap3(): 
    P = 203 
    Q = 204

    P, Q = Q, P  

# Swap3 and Swap2 are similar, but they are better than Swap1
# In python for swap function, we use just Swap3


if __name__ == "__main__":
    start = time.process_time()
    Swap2()
    end = time.process_time()
    ms = (end-start) * 1e06
    result = timeit.timeit(stmt='Swap2()', globals=globals(), number=10000000)
    print(f"Elapsed {result:.03f} micro secs.")
    