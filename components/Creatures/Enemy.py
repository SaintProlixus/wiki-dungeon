from Combatant import Combatant


class Enemy(Combatant):
    def __init__(self, e_class, *args, **kwargs):
        self.e_class = e_class
        self.loot = None
        self.exp = None
        super(Enemy, self).__init__(*args, **kwargs)

    def notice(self, player):
        pass
