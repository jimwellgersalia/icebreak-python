# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.

class IOString():
    def getString(self):
        self.my_char = input('Please input anything: ')

    def printString(self):
        print(self.my_char.upper())


me = IOString()

me.getString()
me.printString()
