import random
from robot import Robot
from dinosaur import Dinosaur

class Battlefield:

    def __init__(self, robot_name, dinosaur_name, dinosaur_power):
        self.robot = Robot(robot_name)
        self.dinosaur = Dinosaur(dinosaur_name, dinosaur_power)


    def run_game(self):
        self.display_welcome()
        self.battle_phase(self.dinosaur, self.robot)

    def display_welcome(self):
        print(f'GOOOOOOOOOOOOOOOOOOOOD MORNING BATTLERS, WE HAVE AN EXCEPTIONAL FIGHT FOR YOU TONIGHT! IN THE LEFT CORNER WE HAVE THE MEAN GREEN BIG BAD DINOSAUR, THEY CALL HIM {self.dinosaur.name}, AND IN THE RIGHT CORNER, HES TOUGH, HES TALL, HES MADE OUT OF METAL! HIS NAME IS {self.robot.name} LETS START THE BATTLE!')


    def battle_phase(self, attacker_1, attacker_2):
        while attacker_1.health > 0 or attacker_2.health > 0:
            attacker_1.attack(attacker_2)
            print(f'{attacker_2.name} just took a hit, his health is now at {attacker_2.health}')
            attacker_2.attack(attacker_1)
            print(f'Oooh thats gotta hurt, {attacker_1.name} health is now reduced to {attacker_1.health}')
            if self.dinosaur.health <= 0:
                self.display_winner(self.robot)
            elif self.robot.health <= 0:
                self.display_winner(self.dinosaur)

    
    def coin_flip(self):
        coin_flip = random.randint(1,2)
        if coin_flip == 1:
            self.battle_phase(self.robot, self.dinosaur)
        elif coin_flip == 2:
            self.battle_phase(self.dinosaur, self.robot)

    def display_winner(self, winner):
        print(f'AND OUR WINNER IS {winner.name}')

    