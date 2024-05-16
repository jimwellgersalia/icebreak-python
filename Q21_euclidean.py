from math import sqrt

x, y = 0, 0
while True:
    step = input('Enter the direction and steps: ').split()
    if not step:
        break
    if step[0].upper() == 'UP':
        x -= int(step[1])
    elif step[0].upper() == 'DOWN':
        x += int(step[1])
    elif step[0].upper() == 'LEFT':
        y -= int(step[1])
    elif step[0].upper() == 'RIGHT':
        y += int(step[1])

distance = round(sqrt(x**2 + y ** 2))
print(distance)
