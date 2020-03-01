from Creature import Creature
from Tables import STATS

from random import randint


class Combatant(Creature):
    def __init__(
        self,
        level=1,
        equip={"head": None, "body": None, "arms": None, "legs": None, "weapon": None},
        *args,
        **kwargs
    ):
        super(Combatant, self).__init__(*args, **kwargs)
        self.level = level
        self.equip = equip
        self.str = STATS[self.race][0]
        self.dex = STATS[self.race][1]
        self.con = STATS[self.race][2]
        self.wis = STATS[self.race][3]
        self.int = STATS[self.race][4]
        self.cha = STATS[self.race][5]
        self.atlhletics = self.str // 5
        self.speed = self.dex // 5
        self.notice = self.wis // 5
        self.inspect = self.int // 5
        self.persuade = self.cha // 5
        self.max_hp = self.con // 5 + 10
        self.hp = self.max_hp
        self.max_mp = self.int // 5 + 10
        self.mp = self.max_mp
        self.ac = 5 + self.speed

    def attack(self, enemy):
        roll = randint(1, 10)
        if self.equip["weapon"] is None:
            if roll >= enemy.ac:
                enemy.hp -= self.atlhletics
        else:
            pass

    def isDead(self):
        return self.hp <= 0

    def levelUp(self):
        self.level += 1
