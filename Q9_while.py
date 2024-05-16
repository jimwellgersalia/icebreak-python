# Write a program that accepts sequence of lines as input and
# prints the lines after making all characters in the sentence capitalized.
my_list = []
while True:
    my_line = input()
    if my_line:
        my_list.append(my_line.upper())
    else:
        break

print('\n'.join(my_list))
