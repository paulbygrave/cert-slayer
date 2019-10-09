class Item:
    def __init__(self, name, type, description, prop):
        self.name = name
        self.type = type
        self.description = description
        self.prop = prop

# Create some Items
potion = Item("Potion", "potion", "Heals 50HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100HP", 100)
superpotion = Item("Super-Potion", "potion", "Heals 500HP", 500)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 9999)
hielixer = Item("MegaElixer", "elixer", "Fully restores party's HP/MP", 9999)
grenade = Item("Grenade", "attack", "Deals 500 damage", 500)