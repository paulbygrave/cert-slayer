import random

class Spell:
    def __init__(self, name, cost, dmg, type):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.type = type

    def generate_damage(self):
        low = self.dmg - 15
        high = self.dmg + 15
        return random.randrange(low, high)

# Create Black Magic
study = Spell("Study for the exam", 100, 1000, "black")
practice = Spell("Do the Practice Tests", 100, 1000, "black")
ask = Spell("Asked for help on Slack", 80, 700, "black")
handson = Spell("Do a Hands-On lab", 200, 1750, "black")

# Create Enemy Black Magic
exhaustion = Spell("Exhaustion", 100, 800, "black")
parental = Spell("Parental Leave", 150, 1200, "black")
sick = Spell("Sick Leave", 80, 700, "black")
drinking = Spell("Contino Monthly Gathering Drinking Session", 250, 1750, "black")

# Create White Magic
sleep = Spell("Get a good night's sleep", 80, 1200, "white")
weekend = Spell("It's the weekend!", 120, 3000, "white")

# Create Enemy White Magic
revision = Spell("Change the exam questions", 250, 2000, "white")
