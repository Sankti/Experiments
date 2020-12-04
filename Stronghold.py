class Structure():
    """
    Defines a type of in-game structure.

    """
    def __init__(self, id, name, housing, gold, morale, space, food, water, herbs, firewood, weapons, iron, workers, price):
        self.id = int(id)
        self.name = name
        self.housing = housing
        self.gold = gold
        self.morale = morale
        self.space = space
        self.food = food
        self.water = water
        self.herbs = herbs
        self.firewood = firewood
        self.weapons = weapons
        self.iron = iron
        self.workers = workers
        self.price = price

    def display(self):
        print(self.price)

tent = Structure(1, "Namiot", 1, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 100)
hut = Structure(2, "Chatka", 2, -5, 1, 10, 0, 0, 0, 0, 0, 0, 0, 500)

hut.display()