# Write a program which accepts a sequence of comma separated 4 digit binary numbers
# as its input and then check whether they are divisible by 5 or not.
# The numbers that are divisible by 5 are to be printed in a comma separated sequence.
num = input('Enter a 4 digit Binary # separated by comma: ').split(',')

my_list = []
for item in num:
    if int(item, 2) % 5 == 0:
        my_list.append(item)

print(', '.join(my_list))
