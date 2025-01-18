import items
import pandas as pd
from random import randint
from collections import deque

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
        
        self.inventory = deque()
        self.equippeds = {"weapow": None, "armor": None, "relic": None}
        
    def status(self):
        status = {
            "atributos" : ["name", "level", "hp max", "hp", "damage min", "damage max", "crit", "inventory", "weapow", "armor", "relic"],
            "valores": [self.name, self.level, self.hp_max, self.__hp, self.atk_min, self.atk_max, self.crit, self.inventory, self.equippeds["weapow"], self.equippeds["armor"], self.equippeds["relic"]]
        }
        
        df = pd.DataFrame(status)
        
        print(df.to_string(index=False))
        
    # Decorator to avoid a setter
    @property
    def hp_max(self):
        return self.__hp_max
    
    @property 
    def hp(self):
        return self.__hp
    
    # Battle
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
        
    # Inventory
    def add_item(self, item: items.Item):
        self.inventory.appendleft(item)
    
    def remove_item(self, item: items.Item):
        self.inventory.remove(item)
    
    def item_equip(self, item: items.Item):
        if item in self.inventory:
            self.__hp += item.hp
            self.atk_min += item.atk
            self.atk_max += item.atk
            self.crit += item.crit
            
            if item in self.equippeds.values():
                return "The item is equipped"
            
            if isinstance(item, items.Weapow):
                self.equippeds["weapow"] = item # type: ignore
                
            elif isinstance(item, items.Armor):
                self.equippeds["armor"] = item # type: ignore
                
            elif isinstance(item, items.Relic):
                self.equippeds["relic"] = item # type: ignore
        
    def item_desiquip(self, item):
        if item in self.equippeds.values():
            self.__hp -= item.hp
            self.atk_min -= item.atk
            self.atk_max -= item.atk
            self.crit -= item.crit
            
            if isinstance(item, items.Weapow):
                self.equippeds["weapow"] = None
                
            elif isinstance(item, items.Armor):
                self.equippeds["armor"] = None
                
            elif isinstance(item, items.Relic):
                self.equippeds["relic"] = None
            
        else: print("This item not equipped")

joao = Player("joao")

joao.status()
joao.add_item(items.espada1)
joao.status()


joao.item_equip(items.espada1)
joao.status()

