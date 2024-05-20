# Define a class, which have a class parameter and have a same instance parameter.

class Player():
    name = 'Player'

    def __init__(self, name):
        self.name = name


archer = Player('archer')
mage = Player('mage')

print(f'{Player.name} name is {archer.name}')
print(f'{Player.name} name is {mage.name}')

