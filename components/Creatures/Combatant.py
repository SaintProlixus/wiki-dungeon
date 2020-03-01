import Creature


class Combatant(Creature):
    def __init__(self, level, *args, **kwargs):
        self.level = level
        super(Combatant, self).__init__(*args, **kwargs)

    def attack(self, enemy):
        pass

    def isDead(self):
        return self.hp <= 0
