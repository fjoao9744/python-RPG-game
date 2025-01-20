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
        self.__hp -= damage
        if self.__hp < 0:
            self.__hp = 0
        
    @abstractmethod
    def atack(self):
        pass
        
class Slime(Monster):
    def __init__(self, nome="Slime", level=1):
        self.nome = nome
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
        
    def damage(self):
        return randint(self.atk_min, self.atk_max)
    

    
print(type(Slime))