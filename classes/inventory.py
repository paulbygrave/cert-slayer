class Item:
    def __init__(self, name, type, description, prop):
        self.name = name
        self.type = type
        self.description = description
        self.prop = prop

# Create some Items
redbull = Item("A can of energy drink", "potion", "Heals 2000HP", 2000)
studysnack = Item("A suitable high-energy study snack", "potion", "Heals 4000HP", 4000)
magicbean = Item("A magic bean", "elixer", "Fully restores HP/MP of one party member", 9999)

# grenade = Item("Grenade", "attack", "Deals 500 damage", 500)