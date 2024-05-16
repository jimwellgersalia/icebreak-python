# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

a = input('Please enter a number: ')

total = 0
temp = ''

for items in range(4):
    temp += a
    total += int(temp)

print(total)
