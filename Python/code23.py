# OOPS Classes & objcets
class pen():
    refil = 1      # class variable
    colour = 1
    def __init__(self):     # Objcet initialization
        self.refil = 1      # Instance variable or object variable
        self.colour = 1
    def write(self):
        print(self.refil)
book= pen()                 # Object creating by using book variable
book.write()                # Accessing the class data
