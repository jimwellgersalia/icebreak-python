# Write a program that accepts a sentence and calculate the number of letters and digits.

word = input('Enter a word & number to count: ')
letter, number = 0, 0

# both will work but we showing here the power of isalpha() and isnumeric()
for items in word:
    if items.isalpha():  # ('a' <= items <= 'z') or ('A' <= items <= 'Z')
        letter += 1
    elif items.isnumeric():  # (_'1' <= items <= '9')
        number += 1

print(f'LETTERS {letter} \nDIGITS {number}')
