from random import randint
from player import Player
from abc import ABCMeta, abstractmethod

class MonsterType(ABCMeta, type):
    def __new__(cls, name, bases, dct):
        
        def __str__(self):
            return f"The object \"{name}\" is monster"
        
        dct["__str__"] = __str__
        
        return super().__new__(cls, name, bases, dct)

class Monster(metaclass = MonsterType):
    class MonsterCreationError(Exception): pass
    
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        
    @abstractmethod
    def atack(self):
        pass
        
class Slime(Monster):
    def __init__(self, name="Slime", level=1):
        self.name = name
        if 1 <= level <= 20:
            self.level = level
        else:
            raise self.__class__.MonsterCreationError("O level do monstro deve ser entre 1 e 20")
        
        self.exp = 0
        self.hp_max = 15 * level
        self.hp = self.hp_max
        self.atk_min = 2 * level
        self.atk_max = 3 * level
        
    def level_up(self):
        if self.level < 20:
            self.level += 1
            
            self.hp_max = 15 * self.level
            self.hp = self.hp_max
            
            self.atk_min = 2 * self.level
            self.atk_max = 3 * self.level
            
    def atack(self, player: Player):
        damage = self.damage()
        player.take_damage(damage)
        print(f"{self.name} atacou {player.name}, deu {damage} de dano")
        print(f"{self.name} esta com {self.hp} de hp")
        
        
        
    def damage(self):
        return randint(self.atk_min, self.atk_max)
    

    
print(type(Slime))