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
ask = Spell("Asked for help on Slack", 100, 700, "black")
handson = Spell("Do a Hands-On lab", 200, 1200, "black")

# Create Enemy Black Magic
exhaustion = Spell("Exhaustion", 100, 800, "black")
paternity = Spell("Paternity Leave", 100, 2000, "black")
sick = Spell("Sick Leave", 100, 900, "black")
drinking = Spell("Contino Monthly Gathering Drinking Session", 100, 2500, "black")

# Create White Magic
sleep = Spell("Get a good night's sleep", 120, 1200, "white")
weekend = Spell("It's the weekend!", 180, 2000, "white")

# Create Enemy White Magic
revision = Spell("Change the exam questions", 180, 2000, "white")
