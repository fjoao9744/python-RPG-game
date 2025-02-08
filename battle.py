from monsters import Monster, Slime
from player import Player

class Battle:
    def __init__(self, player: Player, monster: Monster):
        self.player = player
        self.monster = monster
        
        self.end = False
                
    def turn(self):
        turn = 1
        fighting = True
        
        # bad code ⚠
        while fighting:
            if not self.player.hp <= 0:
                self.player.atack(self.monster)
                
            else:
                fighting = False
                self.dead_player()
                
            if not self.monster.hp <= 0: # type:ignore
                self.monster.atack(self.player) # type:ignore
                
            else:
                fighting = False
                self.dead_monster(self.monster, self.player)
                
            turn += 1
            
        self.end_battle()
                    
    def dead_monster(self, monster, player):
        if monster.alive:
            print("monster died")
            player.killed(monster)
            monster.dead()
        
    def dead_player(self):
        self.player.dead()
            
    def __call__(self):
        if self.end:
            print("Nothing battle activate")
            return
            
        self.turn()
    
    def new_battle(self, player: Player, monster: Monster):
        if not monster.alive:
            print("monster is dead")
            return
            
        self.player = player
        self.monster = monster
            
        self.end = False
        
    def end_battle(self):
        self.end = True

joao = Player("joao")
slime = Slime()
slime2 = Slime(name="slime2")

battle = Battle(joao, slime)
battle()
battle.new_battle(joao, slime) # monster is dead
battle()
battle.new_battle(joao, slime2)

battle()
battle()

joao.status()