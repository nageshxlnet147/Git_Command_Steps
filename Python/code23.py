# OOPS Classes & objcets

# To define a class name as pen.
class pen():
    refil = 1      # class variable
    colour = 1

    # To initialize the object data. The self parameter refers to the current instance of the class and its default argument.
    def __init__(self):     # Object initialization
        self.refil = 1      # Instance variable or object variable
        self.colour = 1
    
    # To create the methods like functions or behaviors.
    def write(self):
        print(self.refil)
book= pen()                 # Object creating by using book variable.
book.write()                # Accessing the class data or printing the required data.
