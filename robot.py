from weapon import Weapon
class Robot:

    def __init__(self, name):
        self.name = name
        self.health = 500
        self.active_weapon = Weapon('Default', 50)
    
    def attack(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power
    



