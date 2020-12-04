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
        print(self)


