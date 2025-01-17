from dataclasses import dataclass

@dataclass
class Item:
    name: str
    #buffs
    hp: int = 0
    atk: int = 0
    crit: int = 0
    
    def __str__(self):
        return self.name

class ItemType(type):
    def __new__(cls, name, bases, dct):
        dct["item_type"] = name.lower()
        
        return super().__new__(cls, name, bases, dct)
    
class Weapow(Item, metaclass = ItemType):
    pass

class Armor(Item, metaclass = ItemType):
    pass

class Relic(Item, metaclass = ItemType):
    pass

class Consumible(Item, metaclass = ItemType):
    pass

class Sword(Weapow):
    def __init__(self, name, hp = 0, atk = 0, crit = 0):
        super().__init__(name, hp, atk, crit)
        
class Helmet(Armor):
    def __init__(self, name, hp = 0, atk = 0, crit = 0):
        super().__init__(name, hp, atk, crit)

class Ring(Relic):
    def __init__(self, name, hp = 0, atk = 0, crit = 0):
        super().__init__(name, hp, atk, crit)

class Potion(Consumible):
    def __init__(self, name, hp = 0, atk = 0, crit = 0):
        super().__init__(name, hp, atk, crit)
        
    
espada1 = Sword("espada longa", atk = 2)
espada2 = Sword("espada curta", atk = 1)


        
    