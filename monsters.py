class MonsterType(type):
    def __new__(cls, name, bases, dct):
        
        def __init__(self):
            return f"O objeto \"{name}\" é um monstro"
        
        dct["__init__"] = __init__
        
        return super().__new__(cls, name, bases, dct)

class Slime(metaclass = MonsterType):
    class MonsterCreationError(Exception): pass
    
    def __init__(self, nome="Slime", level=1):
        self.nome = nome
        if 1 <= level <= 20:
            self.level = level
            
        else:
            raise self.__class__.MonsterCreationError("O level do monstro deve ser entre 1 e 20")
        
        
    
