# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program: 8 Then, the output should be:40320


fact = int(input('Enter a number: '))
result = 1
for items in range(1, fact+1):
    result = result * items

print(f'The factorial of {fact} is {result}')
