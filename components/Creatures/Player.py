from Combatant import Combatant


class Player(Combatant):
    def __init__(self, location=None, p_class=None, *args, **kwargs):
        super(Player, self).__init__(*args, **kwargs)
        self.location = location
        self.p_class = p_class
        self.inventory = None
        self.equipment = None
        self.exp = None

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
