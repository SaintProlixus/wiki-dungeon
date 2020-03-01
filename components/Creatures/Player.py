import Combatant


class Player(Combatant):
    def __init__(self, p_class, *args, **kwargs):
        self.p_class = p_class
        self.inventory = None
        self.equipment = None
        super(Player, self).__init__(*args, **kwargs)

    def levelUp(self):
        self.level += 1

    def notice(self, location):
        pass

    def inspect(self, item):
        pass

    def buy(self, item):
        pass

    def sell(self, item):
        pass

    def rest(self, type):
        pass
