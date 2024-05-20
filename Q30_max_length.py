# Define a function that can accept two strings as input and print the string with maximum length in console.
# If two strings have the same length, then the function should print all strings line by line.

def display(str1, str2):
    str1_length = len(str1)
    str2_length = len(str2)
    if str1_length > str2_length:
        return str1
    elif str1_length < str2_length:
        return str2
    else:
        return str1 + str2


print(display('123456', '123'))
print(display('abc', 'abcd'))
print(display('equal', 'equal'))
