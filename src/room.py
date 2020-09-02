# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        res = "Room(name = %s, description = %s), " % (
            self.name, self.description)
        return res
