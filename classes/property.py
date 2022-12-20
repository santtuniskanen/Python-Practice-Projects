"""
@property decorator.
A more pythonic way to use getters and setters
in object-oriented programming.

Getters and setters are tools to achieve
encapsulation aka preventing data from being
modified directly. Getters and setter methods
also allow creating complex behaviour like
limiting access under certain conditions
or imposing restrictions on allowable
ranges of values for an attribute.
"""

# an example with one attribute
# Weight is a private attribute
# with a getter and setter
class Box:
    def __init__(self, weight):
        self.__weight = weight

    def getWeight(self):
        return self.__weight

    def setWeight(self, weight):
        if weight >= 0:
            self.__weight = weight

"""
Python doesn't have private attributes,
but I'm are using __ (dunder) notation
to denote weight as private.
The setter also has a restriction so that 
the weight can only be greater than zero.
"""
box = Box(10)

box.setWeight(-5)
print(box.getWeight()) # Returns 10

box.setWeight(5)
print(box.getWeight()) # Returns 5
"""
We need to call the methods instead of 
directly interating with the attribute.
Python has a built-in property() function
that will take care of this.

The property() function accepts four 
optional arguments:
"""

property(fget=None, fset=None, \
    fdel=None, doc=None)

"""
The first three arguments are getter, setter
and deleter and the last one is a docstring
for the attribute.

Let's use the property function with the 
Box example
"""
class Box:
    def __init__(self, weight):
        self.__weight = weight

    def getWeight(self):
        return self.__weight

    def setWeight(self, weight):
        if weight >= 0:
            self.__weight = weight

    def delWeight(self):
        del self.__weight

    weight = property(getWeight, setWeight, \
        delWeight, "Docstring for the \
            'weight' property")

"""
While the delWeight() method isn't necessary, it's used
to show the full potential of the property() function.
The property() function is then called and getter, setter
and deleter are passed into the function as argument.
"""

box = Box(10)

print(box.weight) # Calls .getWeight()
box.weight = 5 # Calls .setWeight()
del box.weight # Calls .delWeight()
box.weight = -5 # box.__weight doesn't change

"""
Weight attribute can now be used without having to call
the setters, getters and deleter methods directly.

Within a bigger database, using the methods in multiple places
could mess up everything if a single change is made to the method
name since it would have to be changed everywhere. Using
the property function is great since you are not directly
calling the methods.


The mosty pythonic way of using property function is to 
use the @property decorator. It will clean up the code.
"""

class Box:
 def __init__(self, weight):
   self.__weight = weight
 
 @property
 def weight(self):
   """Docstring for the 'weight' property"""
   return self.__weight
  
 @weight.setter
 def weight(self, weight):
   if weight >= 0:
     self.__weight = weight
 
 @weight.deleter
 def weight(self):
   del self.__weight

"""
All of the methods are now simply called "weight". Then
the getter is denoted with a @property.
Lastly, @weight.setter and @weight.deleter are used to 
define the setter and deletor methods.
"""
