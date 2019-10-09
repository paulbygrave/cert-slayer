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
fire = Spell("Fire", 100, 1000, "black")
thunder = Spell("Thunder", 100, 1000, "black")
blizzard = Spell("Blizzard", 100, 1000, "black")
meteor = Spell("Meteor", 200, 2000, "black")
quake = Spell("Quake", 140, 1400, "black")

# Create White Magic
cure = Spell("Cure", 120, 1200, "white")
cura = Spell("Cura", 180, 2000, "white")