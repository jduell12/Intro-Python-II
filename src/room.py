# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.is_light: False

    def __repr__(self):
        res = "Room(name = %s, description = %s, items =  " % (
            self.name, self.description)
        for item in self.items:
            res += str(item.name) + ", "
        res += ")"
        return res
