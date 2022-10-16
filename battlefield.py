import random
from robot import Robot
from dinosaur import Dinosaur
from weapon import Weapon

class Battlefield:

    def __init__(self, robot_name, dinosaur_name, dinosaur_power):
        self.robot = Robot(robot_name)
        self.dinosaur = Dinosaur(dinosaur_name, dinosaur_power)


    def run_game(self):
        self.display_welcome()
        self.coin_flip()

    def display_welcome(self):
        print(f'GOOOOOOOOOOOOOOOOOOOOD MORNING BATTLERS, WE HAVE AN EXCEPTIONAL FIGHT FOR YOU TONIGHT! IN THE LEFT CORNER WE HAVE THE MEAN GREEN BIG BAD DINOSAUR, THEY CALL HIM {self.dinosaur.name}, AND IN THE RIGHT CORNER, HES TOUGH, HES TALL, HES MADE OUT OF METAL! HIS NAME IS {self.robot.name} LETS START THE BATTLE!')


    def battle_phase(self, attacker_1, attacker_2):
        battle = True
        while battle == True:
            if attacker_1 == self.robot:
                self.weapon_choice(attacker_1)
            attacker_1.attack(attacker_2)
            print(f'{attacker_2.name} just took a hit, his health is now at {attacker_2.health}')
            battle = self.determine_winner(attacker_1,attacker_2)
            if battle == False:
                break
            if attacker_2 == self.robot:
                self.weapon_choice(attacker_2)
            attacker_2.attack(attacker_1)
            print(f'Oooh thats gotta hurt, {attacker_1.name} health is now reduced to {attacker_1.health}')
            battle = self.determine_winner(attacker_1, attacker_2)
            if battle == False:
                break

        

    def determine_winner(self,attacker_1, attacker_2):
        if attacker_1.health <= 0:
            self.display_winner(attacker_2)
            return False
        elif attacker_2.health <= 0:
            self.display_winner(attacker_1)
            return False
        else:
            return True
        
    
    def coin_flip(self):
        coin_flip = random.randint(1,2)
        if coin_flip == 1:
            print(f"The Coin Flip landed heads, therefore {self.robot.name} has the first move!")            
            self.battle_phase(self.robot, self.dinosaur)
        elif coin_flip == 2:
            print(f"The Coin Flip landed tails, therefore {self.dinosaur.name} has the first move!")
            self.battle_phase(self.dinosaur, self.robot)
    
    def display_winner(self, winner):
        print(f'AND OUR WINNER IS {winner.name}')

    def weapon_choice(self, attacker):
        user_input = input(f"{attacker.name} weapon would you like to use? [Duskfang, DawnBreaker, Rutheful Axe]: ")
        if user_input == "Duskfang":
            active_weapon = Weapon('Duskfang', 100)
            print(f'{attacker.name} has chosen Duskfang which does a mighty 100 damage!')
        elif user_input == "DawnBreaker":
            active_weapon = Weapon('DawnBreaker', 150)
            print(f'{attacker.name} has chosen DawnBreaker and its holy light does an insane 150 damage!')            
        elif user_input == "Rutheful Axe":
            active_weapon = Weapon('Rutheful Axe', 200)
            print(f'{attacker.name} has chosen the powerful Rutheful Axe! It injures its enemy greatly with 200 damage!')            
        return active_weapon