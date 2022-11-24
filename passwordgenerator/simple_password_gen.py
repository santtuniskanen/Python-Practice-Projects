import string
import random

"""
Very simple password generator that utilizes the string and random libraries.
"""
def pw_gen(size, chars=string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(chars) for i in range(size))

    """
    The function is defined with two parameters: size and chars. 
    Char is given a default value, which is all of the letters,
    digits and punctuations. The size parameter doesn't take any default values, 
    since the length of the password is assigned to it during function call.
    When we return the function, we add to an empty list randomly from 'chars' 
    with the length of 'size'.
    The .choice() returns a randomly selected element from the specified sequence.
    
    """

print(pw_gen(int(input("How many characters? "))))