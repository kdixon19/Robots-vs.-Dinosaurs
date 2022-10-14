import random
from robot import Robot
from dinosaur import Dinosaur

class Battlefield:

    def __init__(self, robot_name, dinosaur_name, dinosaur_power):
        self.robot = Robot(robot_name)
        self.dinosaur = Dinosaur(dinosaur_name, dinosaur_power)


    def run_game(self):
        self.display_welcome()
        self.battle_phase()

    def display_welcome(self):
        print(f'GOOOOOOOOOOOOOOOOOOOOD MORNING BATTLERS, WE HAVE AN EXCEPTIONAL FIGHT FOR YOU TONIGHT! IN THE LEFT CORNER WE HAVE THE MEAN GREEN BIG BAD DINOSAUR, THEY CALL HIM {self.dinosaur.name}, AND IN THE RIGHT CORNER, HES TOUGH, HES TALL, HES MADE OUT OF METAL! HIS NAME IS {self.robot.name} LETS START THE BATTLE!')


    def battle_phase(self):
        robot_first = False
        dinosaur_first = False
        coin_flip = random.randint(1,2)
        if coin_flip == 1:
            robot_first = True
        elif coin_flip == 2:
            dinosaur_first = True
        while robot_first == True:
            self.robot.attack(self.dinosaur)
            print(f'Dinosaur just took a hit, his health is now at {self.dinosaur.health}')
            self.dinosaur.attack(self.robot)
            print(f'Oooh thats gotta hurt, Robots health is now reduced to {self.robot.health}')
            if self.dinosaur.health <= 0:
                dinosaur_first == False
                self.display_winner(self.robot)
            elif self.robot.health <= 0:
                dinosaur_first == False
                self.display_winner(self.dinosaur)
        while dinosaur_first == True:
            self.dinosaur.attack(self.robot)
            print(f'Oooh thats gotta hurt, Robots health is now reduced to {self.robot.health}')
            self.robot.attack(self.dinosaur)
            print(f'Dinosaur just took a hit, his health is now at {self.dinosaur.health}')
            if self.dinosaur.health <= 0:
                dinosaur_first == False
                self.display_winner(self.robot)
            elif self.robot.health <= 0:
                dinosaur_first == False
                self.display_winner(self.dinosaur)

    def display_winner(self, winner):
        print(f'AND OUR WINNER IS {winner.name}')

    