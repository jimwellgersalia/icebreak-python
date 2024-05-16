# Write a program that computes the net amount of a bank account based a transaction log from console input.
# The transaction log format is shown as following:
# D 100
# W 200
# D means deposit while W means withdrawal.

net_amount = 0
while True:
    trans = input('Please enter transaction and amount: ').split(' ')

    if trans[0] == 'D':
        net_amount += int(trans[1])
    elif trans[0] == 'W':
        net_amount -= int(trans[1])
    else:
        break

print(net_amount)
