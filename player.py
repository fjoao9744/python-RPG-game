import items
import pandas as pd
from random import randint
from sys import stdout
from collections import deque

class PlayerDefinition(type):
    def __new__(cls, name, bases, dct):
        
        def __str__(self):
            return f"object \"{name}\" is player"
        
        dct["__str__"] = __str__
        
        return super().__new__(cls, name, bases, dct)

class Player(metaclass = PlayerDefinition):
    """
    -> Create player for game
    methods:
    # Basic methods
        status(): Display all player attributes
        level_up(): Increase player attributes
        exp_owner(exp): Increase exp attribute, if exp is high the player level up
        
    # Battle methods
        damage(): Return player damage # Not use
        take_damage(damage): Receive the damage
        heal(hp): Restore hp
        atack(monster): Decreases monster hp 
    
    # Invetory methods
        add_item(item): Add item to inventory
        remove_item(item): Remove item to inventory(if the item is there)
        item_equip(item): Equip item(receive attributes extras)
        item_desiquip(item): Desiquip item
        
    """
    def __init__(self, name):
        self.name = name
        self.level = 1
        
        self.exp = self.Exp(self)
        
        self.__hp_max = 20
        self.__hp = 20
        
        self.atk_min = 2
        self.atk_max = 6
        
        self.crit = 8
        
        self.inventory = deque()
        self.equippeds = {"weapow": None, "armor": None, "relic": None}
    
    # basic methods
    def status(self):
        status = {
            "atributos" : ["name", "level", "exp", "hp max", "hp", "damage min", "damage max", "crit", "inventory", "weapow", "armor", "relic"],
            "valores": [self.name, self.level, self.exp.exp, self.hp_max, self.__hp, self.atk_min, self.atk_max, self.crit, self.inventory, self.equippeds["weapow"], self.equippeds["armor"], self.equippeds["relic"]]
        }
        
        df = pd.DataFrame(status)
        
        stdout.write(df.to_string(index=False))
    
    def level_up(self):
        if self.level < 20:
            self.level += 1
            
            self.__hp_max += self.__hp_max // 3
            
            self.atk_min += self.atk_min // 2
            self.atk_max += int(self.atk_max // 2.25)
            
            self.crit = self.atk_min + self.atk_max
            
            self.heal(self.__hp_max // 4)
            next(self.exp)
    
    # exp system
    def exp_owner(self, exp):
        self.exp.add(exp)
        
        if self.exp.exp >= self.exp.exp_required:
            self.level_up()
            
    class Exp:
        def __init__(self, player):
            self.player = player
            self.exp = 0
            self.can_gain_exp = True
            self.exp_generator = self.exp_required_setter()
            self.exp_required = next(self.exp_generator)
            
        def exp_required_setter(self):
            self.exp_required = 50
            while self.can_gain_exp:
                if not self.player.level < 20:
                    self.can_gain_exp = False
                    yield
                    
                yield self.exp_required * 2
                        
        def add(self, exp):
            if self.can_gain_exp:
                self.exp += exp
                return self.exp
            
        def __next__(self):
            self.exp_required = next(self.exp_generator)
    
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
        crit = randint(0, 10)
        
        return damage if crit != 10 else crit
    
    def take_damage(self, damage):
        self.__hp -= damage
        if self.__hp < 0:
            self.__hp = 0

    def heal(self, hp):
        self.__hp += hp
        if self.__hp > self.__hp_max:
            self.__hp = self.__hp_max
        
    def atack(self, monster):
        damage = self.damage()
        monster.take_damage(damage)
        print(f"{self.name} atacou {monster.name}, deu {damage} de dano")
        print(f"{self.name} esta com {self.hp} de hp")
        
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
        
    def item_desiquip(self, item: items.Item):
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
        
    def __gameover(self):
        exit()
        
    def dead(self):
        print("You dead.")
        print("Your status: ")
        self.status()
        self.__gameover()
        
    def killed(self, monster):
        for item in monster.drops:
            self.add_item(item)
        self.exp_owner(monster.exp)
        
        monster.dead()


joao = Player("joao")

