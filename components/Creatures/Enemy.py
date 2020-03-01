from Combatant import Combatant


class Enemy(Combatant):
    def __init__(self, e_class=None, *args, **kwargs):
        super(Enemy, self).__init__(*args, **kwargs)
        self.e_class = e_class
        self.loot = None
        self.exp = None

    def notice(self, player):
        pass
