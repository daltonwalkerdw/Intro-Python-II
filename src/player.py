# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__(self, name, location, hp):
        self.name = name
        self.location = location
        self.hp = hp
    def __str__(self):
        return f"{self.name} hp: {self.hp} location: {self.location}"