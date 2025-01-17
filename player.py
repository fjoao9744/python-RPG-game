from random import randint
from items import Item
import pandas as pd

class PlayerDefinition(type):
    def __new__(cls, name, bases, dct):
        
        def __str__(self):
            return f"object \"{name}\" is player"
        
        dct["__str__"] = __str__
        
        return super().__new__(cls, name, bases, dct)

class Player(metaclass = PlayerDefinition):
    def __init__(self, name):
        self.name = name
        self.level = 1
        
        self.__hp_max = 20
        self.__hp = 20
        
        self.atk_min = 2
        self.atk_max = 6
        
        self.crit = 8
        
    def status(self):
        status = {
            "atributos" : ["name", "level", "hp max", "hp", "damage min", "damage max", "crit"],
            "valores": [self.name, self.level, self.hp_max, self.__hp, self.atk_min, self.atk_max, self.crit]
        }
        
        df = pd.DataFrame(status)
        
        print(df.to_string(index=False))
        
    # Decorador property para evitar um setter
    @property
    def hp_max(self):
        return self.__hp_max
    
    @property 
    def hp(self):
        return self.__hp
    
    def damage(self):
        damage = randint(self.atk_min, self.atk_max)
        
        return damage
    
    def take_damage(self, damage):
        self.__hp -= damage
        if self.__hp < 0:
            self.__hp = 0
        
    def heal(self, hp):
        self.__hp += hp
        if self.__hp > self.__hp_max:
            self.__hp = self.__hp_max
        
    def atack(self, monster):
        monster.take_damage(self.damage())
        
    def item_equip(self, item: Item):
        self.__hp += item.hp
        self.atk_min += item.atk
        self.atk_max += item.atk
        self.crit += item.crit
        
        



joao = Player("joao")

joao.status()