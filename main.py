from player import Player
from items import sword, sword2, cure_potion
class World:
    def __init__(self):
        self.fase = 1

p = Player("joao")

p.add_item(cure_potion)
p.add_item(cure_potion)
p.add_item(cure_potion)
p.add_item(cure_potion)
p.add_item(cure_potion)

p.status()

p.remove_item(cure_potion)

p.status()


"""
-> parts of the project
player =
(exp✅, inventory== and level up✅)
monsters =
(exp, drop items, level up and dead)
items ==
damage functions(for monsters and player) ✅
critical system
inventory sistem ===
multi atacks choice system(monsters and player)
battle sistem
(choose the actions)
world sistem and ARG(Artificial Random Generation)

save and load system(automatic if possible)
terminal decoration libs(Curses or InquererPy)
party sistem
npcs
dialogs
loot boxes(chests)

"""


