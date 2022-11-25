"""
    Because I will use such a large list,
    I want to time how long it takes 
    for Python to run this function.
"""

# Creating a random list for the project
import random
randomlist = []
for i in range(1, 1_000_000):
    # You can use underscores to make numbers readable
    n = random.randint(1, 99_999)
    randomlist.append(n)
    
"""
ADDING MERGE SORT HERE OR SOMETHING
"""

"""
    The list is still fairly small for this example,
    since Binary Search can easily find the desired
    value in a list with a length in the millions 
    in under a second.
    
    EDIT: Nevermind, I am using almost one billion as the list size.
    
    EDIT 2: It took too long...
"""


import time
# Importing the time module and starting the timer
start = time.time()
# Creating the function
def binary_search(arr, x):
    """ The function takes two parameters; 
        arr, which is the list 'randomlist'
        and x, which is the targeted integer. """
        
    low = 0
    high = len(arr) - 1

    while low <= high:
        middle = (high + low) // 2
        
        if arr[middle] < x:
            low = middle + 1    
        elif arr[middle] > x:
            high = middle - 1
        else:
            return middle
    
    return -1 # Returning unsuccessful 
        
result = binary_search(randomlist, 50)        

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")

# ending the timer and printing it 
end = time.time()
print("the algorithm took", round(end - start), "Seconds to run.")

