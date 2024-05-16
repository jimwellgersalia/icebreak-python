# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
sentence = input('Please enter a sentence: ')

upper_case = 0
lower_case = 0
for letter in sentence:
    if letter.isupper():
        upper_case += 1
    elif letter.islower():
        lower_case += 1

print(f'UPPERCASE {upper_case}\nLOWERCASE {lower_case}')
