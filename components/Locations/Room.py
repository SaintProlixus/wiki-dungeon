from Location import Location


class Room(Location):
    def __init__(
        self,
        desc=None,
        discovered=False,
        items=None,
        enemies=None,
        doors=None,
        portals=None,
        traps=None,
        *args,
        **kwargs
    ):
        super(Room, self).__init__(*args, **kwargs)
        self.desc = desc
        self.discovered = discovered
        self.items = items
        self.enemies = enemies
        self.doors = doors
        self.portals = portals
        self.traps = traps
