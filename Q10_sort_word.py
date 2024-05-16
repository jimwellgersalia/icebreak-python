# Write a program that accepts a sequence of whitespace separated words as input
# and prints the words after removing all duplicate words and sorting them alphanumerically.

word = list(set(input('Enter multiple word separated by space: ').split(' ')))
word.sort()
print(' '.join(word))
