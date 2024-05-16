# Use a list comprehension to square each odd number in a list.
# The list is input by a sequence of comma-separated numbers.

num_list = [str(int(num)**2) for num in input(
    'Please input multiple number separated by comma: ').split(',') if int(num) % 2 != 0]

print(','.join(num_list))
