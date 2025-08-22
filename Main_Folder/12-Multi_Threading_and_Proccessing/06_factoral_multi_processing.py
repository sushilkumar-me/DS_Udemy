'''
Real-World Example: Multiprocessing for CPU-bound Tasks
Scenario: Factorial Calculation
Factorial calculations, especially for large numbers,
involve significant computational work. Multiprocessing
can be used to distribute the workload across multiple
CPU cores, improving performance.
'''

import multiprocessing
import math 
import sys 
import time 

# Increase the maximum number of digits for integer conversion 
sys.set_int_max_str_digits(1000000)

# Function to compute factorials of a given number 

def computer_factorial(number): 
    print(f"Computing factoral of {number}")
    result = math.factorial(number)
    print(f"factoral of {number} is {result}")
    return result

if __name__ == "__main__":
    numbers = [50000,10000,6000,7000]

    start_time = time.time() 

    # craete pool of workers processes 
    with multiprocessing.Pool() as pool:
        results = pool.map(computer_factorial,numbers)

    end_time = time.time() 
    print(f"Results: {results}")
    print(f"Time taken: {end_time - start_time} Seconds")