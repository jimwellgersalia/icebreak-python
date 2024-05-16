# Write a program that accepts a comma separated sequence of words
# as input and prints the words in a comma-separated sequence after sorting them alphabetically.

my_input = input('Enter multiple word seperated by comma: ').split(',')
my_input.sort()
print(','.join(my_input))
