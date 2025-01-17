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


class Weapow(type):
    def __new__(cls, name, bases, dct):
        
        return super().__new__(cls, name, bases, dct)
    
class Sword(Item, metaclass=Weapow):
    def __init__(self, name, hp = 0, atk = 0, crit = 0):
        super().__init__(name, hp, atk, crit)
        


        
    