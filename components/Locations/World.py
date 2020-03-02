from Location import Location


class World(Location):
    def __init__(self, realms=None, *args, **kwargs):
        super(World, self).__init__(self, *args, **kwargs)
        self.realms = realms
