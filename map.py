import random

class Map:
    @staticmethod
    def map_generate():
        # ARG
        monster_chance = random.random()
        chest_chance = random.random() / 2
        
        return [[[] for row in range(20)] for colunm in range(20)]
    
    matrix_map = map_generate()
    
    def __str__(self):
        return "\n".join(str(row) for row in self.matrix_map)    

map = Map()

print(map)

