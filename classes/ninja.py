from classes.character import Character
import random

class Ninja(Character):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.stamina = 30
        self.speed = 25

    def ninja_speed(self, target):
        roll = random.randint(1,20)
        damage = self.strength
        if (roll > 18):
            self.speed *= random.randint(1,5)
            if self.speed > 80:
                target.health -= (damage * 3)
                print(f"Katana slice: Triple Attack! {target.name} -{damage * 3} health")
            elif self.speed > 50:
                target.health -= (damage * 2)
                print(f"Star Throw: Double Attack! {target.name} -{damage * 2} health")
        else:
            target.health -= damage
            print(f"{self.name} attacked! {target.name} -{damage} health")
