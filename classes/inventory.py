class Item:
    def __init__(self, name, type, description, prop):
        self.name = name
        self.type = type
        self.description = description
        self.prop = prop

# Create some Items
redbull = Item("A can of energy drink", "potion", "Heals 300HP", 300)
studysnack = Item("A suitable high-energy study snack", "potion", "Heals 500HP", 500)

# superpotion = Item("Super-Potion", "potion", "Heals 500HP", 500)
# elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 9999)
# hielixer = Item("MegaElixer", "elixer", "Fully restores party's HP/MP", 9999)
# grenade = Item("Grenade", "attack", "Deals 500 damage", 500)