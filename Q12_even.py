# Write a program, which will find all such numbers between 1000 and 3000 (both included)
# such that each digit of the number is an even number.The numbers obtained should be printed in
# a comma-separated sequence on a single line.


my_list = []

for item in range(1000, 3001):
    flag = 1
    for j in str(item):
        # ord returns the ascii value, j is every digit of item.
        if ord(j) % 2 != 0:
            flag = 0
    if flag == 1:
        my_list.append(str(item))

print(','.join(my_list))
