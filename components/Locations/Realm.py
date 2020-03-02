from Location import Location


class Realm(Location):
    def __init__(self, rooms, portals, discovered=False, setting=None, *args, **kwargs):
        super(Realm, self).__init__(*args, **kwargs)
        self.rooms = rooms
        self.portals = portals
        self.discovered = discovered
        self.setting = setting
