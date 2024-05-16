message = input().split()
sorted_msg = sorted(set(message))

for item in sorted_msg:
    print(f'{item}:{message.count(item)}')
