import random
import string
from unittest import result

string_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
# using the "string" library to import lower and uppercase characters and numbers.
# Saving those characters into the variable "string_characters"


from tkinter import *
# Importing tkinter, the library that's being used to generate the User Interface.
  
class Interface:
    def __init__(self, win):
        self.lbl1=Label(win, text='Generate Password', font="Helvetica")
        self.lbl2=Label(win, text='New Password', justify="center")
        self.t1=Entry(bd=3)
        self.t2=Entry(bd=3)
        # Assigning the generate function in the Button widget as the action.
        self.btn1 = Button(win, text='Generate', command=self.generate) 
        self.lbl1.place(x=120, y=20)
        self.btn1.place(x=160, y=60)
        self.t2.place(x=130, y=100)
    def generate(self):
        self.t2.delete(0, 'end')
        generated = "".join(random.sample(string_characters, 18))
        """
            The join method is being used to along with the random library 
            to randomly generate a string containing some of the characters
            from our "string_chars" variable and adding them into the variable
            "generated", which will be inserted into the text box below the "Generate" button. 
        """
        self.t2.insert(END, str(generated))



window = Tk()
mywin = Interface(window)
window.title('Password Generator')
window.geometry("400x125+10+10")
window.mainloop()