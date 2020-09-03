# item class
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        print("You have picked up %s\n" % (self.name))

    def on_drop(self):
        print("You have dropped %s\n" % (self.name))

# Lightsource subclass of Item


class LightSource(Item):
    def __init__(self, name, description):
        super().__init__(name, description)

    def on_drop(self):
        print("It's not wise to drop your source of illumination! %s\n" %
              (self.name))

# Pack subclass of item


class Pack(Item):
    def __init__(self, name, description, size):
        super().__init__(name, description)
        self.size = size
