from classes.character import Character

class Monk(Character):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.health = 150
        self.stamina = 40

