import random

class Map:
    @staticmethod
    def map_generate():
        # ARG
        map = []
        monster_chance_changeable = 1
        chest_chance_changeable = 2
        
        for colunms in range(20):
            row = []
            for rows in range(20):
                monster_chance = random.random() / monster_chance_changeable
                monster_chance_ = random.random()
                                
                if monster_chance >= monster_chance_: # if monster
                    row.append("M")
                    monster_chance_changeable += 1
                    continue
                
                chest_chance = random.random() / chest_chance_changeable
                chest_chance_ = random.random()
                
                if chest_chance >= chest_chance_: # if chest
                    row.append("C")
                    chest_chance_changeable += 1
                    continue
                
                row.append([])
            map.append(row)
        
        return map
    
    matrix_map = map_generate()
    
    def __next__(self):
        self.matrix_map = self.map_generate()
        return self.__str__()
    
    def __str__(self):
        return "\n".join("".join(f"{str(cell):^3}" for cell in row) for row in self.matrix_map) 

map = Map()

print(map)
print(next(map))
print(next(map))


