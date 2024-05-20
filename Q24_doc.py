#Please write a program to print some Python built-in functions documents,
#such as abs(), int(), raw_input()
#And add document for your own function

print(abs.__doc__)
print(int.__doc__)
print(input.__doc__)


def square(num, power):
    ''' 
        param num: Any integer number
        param power: power over num
        num^power
    '''
    return num ** power


print(square(5, 3))
print(square.__doc__)
