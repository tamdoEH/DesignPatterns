class Warrior:
    def __init__(self):
        self.state = "normal"

    def move(self):
        if self.state == "normal":
            return "Walking normally"
        elif self.state == "battle":
            return "Moving in combat stance"
        elif self.state == "stunned":
            return "Can't move while stunned"
        elif self.state == "stealth":
            return "Moving silently"

    def attack(self):
        if self.state == "normal":
            return "Can't attack in normal state"
        elif self.state == "battle":
            return "Attacking the enemy"
        elif self.state == "stunned":
            return "Can't attack while stunned"
        elif self.state == "stealth":
            return "Performing sneak attack"

    def interact(self):
        if self.state == "normal":
            return "Interacting with NPC"
        elif self.state == "battle":
            return "Can't interact during battle"
        elif self.state == "stunned":
            return "Can't interact while stunned"
        elif self.state == "stealth":
            return "Can't interact in stealth mode"