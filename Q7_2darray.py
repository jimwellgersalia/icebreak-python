# _Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i _ j.*
# Note: i=0,1.., X-1; j=0,1,¡­Y-1

X, Y = map(int, input('Please enter 2 numbers: ').split(','))
my_list = []
for i1 in range(X):
    temp = []
    for i2 in range(Y):
        temp.append(i1*i2)
    my_list.append(temp)

print(my_list)
