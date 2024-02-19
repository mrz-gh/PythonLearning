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



if __name__ == "__main__":
    # Comparison of Algorithms
    swapAlgorithms = [Swap1, Swap2, Swap3]
    for swap in swapAlgorithms:
        # Executing each swap algorithms for 1 million times \
        # and calculate each algorithm execution time
        result = timeit.timeit(stmt='swap()', globals=globals(), number=1000000)
        print(f"Elapsed {result:.03f} micro secs.")
    
    pass

# If you run the code, you will figure out that \
# in python for swap function, Swap3 algorithm is better that other two.