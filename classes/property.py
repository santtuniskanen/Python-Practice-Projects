# This example is from the Python documentation
# https://docs.python.org/3/library/functions.html#property

class Parrot:
    def __init__(self):
        self._voltage = 100000
    
    @property
    def voltage(self):
        """Get the current voltage"""

        return self._voltage
    
    """
    The '@property' decorator turns the voltage()
    method into a "getter" for a read-only attribute
    with the same name, and it sets the docstring for voltage 
    to "Get the current voltage".
    """
