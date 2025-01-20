from monsters import MonsterType, Slime
from player import Player

class Battle:
    def __init__(self, player: Player, monster: MonsterType):
        self.player = player
        self.monster = monster
        
    def turn(self):
        turn = 1
        fighting = True
        
        while fighting:
            if not self.monster.hp <= 0: # type: ignore
                self.player.atack(self.monster)
                
            if not self.player.hp <= 0: 
                self.monster.atack(self.player) # type:ignore
                
            turn += 1
            
            yield

joao = Player("joao")
slime = Slime()

