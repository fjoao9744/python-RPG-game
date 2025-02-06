from monsters import Monster, Slime
from player import Player

class Battle:
    def __init__(self, player: Player, monster: Monster):
        self.player = player
        self.monster = monster
        
    def turn(self):
        turn = 1
        fighting = True
        
        # bad code ⚠
        while fighting:
            if not self.player.hp <= 0:
                self.player.atack(self.monster)
                
            else:
                fighting = False
                
            if not self.monster.hp <= 0: # type:ignore
                self.monster.atack(self.player) # type:ignore
            else:
                fighting = False
            turn += 1
        
        """
        def player_dead():
            player.gameover()
        
        def monster_dead():
            player.killed(monster)
            
        
        # in player
        def killed(monster):
            monster.drop()
            self.exp_owner(monster.exp)
            
        # in monster
        def drop():
            ...
        
        
        
        
        """
            
    def __call__(self):
        self.turn()

joao = Player("joao")
slime = Slime()

battle = Battle(joao, slime)

battle()
