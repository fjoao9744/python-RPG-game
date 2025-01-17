
class PlayerDefinition(type):
    def __new__(cls, name, bases, dct):
        
        def __str__(self):
            return f"O objeto {name} é o jogador"
        
        dct["__str__"] = __str__
        
        return super().__new__(cls, name, bases, dct)

class Player(metaclass = PlayerDefinition):
    def __init__(self, nome):
        self.nome = nome
        self.level = 1
        
        self.__hp_max = 20
        self.__hp = 20
        
        self.atk_min = 2
        self.atk_max = 6
        
    # Decorador property para evitar um setter
    @property
    def hp_max(self):
        return self.__hp_max
    
    @property 
    def hp(self):
        return self.__hp
    
        
        
        
joao = Player("joao")