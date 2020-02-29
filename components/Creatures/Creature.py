class Creature(object):
    def __init__(self, name, race, gender):
        self.name = name
        self.race = race
        self.gender = gender

    def __str__(self):
        return self.name

    def speak(self, speach):
        return f"{self.name}: {speach}"
