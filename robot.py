from weapon import Weapon
class Robot:

    def __init__(self, name):
        self.name = name
        self.health = 500
        self.active_weapon = Weapon('Crusader', 100)
    
    def attack(self, dinosaur):
        pass


