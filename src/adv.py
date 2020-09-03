from player import Player
from room import Room
from item import Item, LightSource, Pack

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),
    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east."""),
    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),
    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air."""),
    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""),
}

# determine which rooms have natural light source
room['outside'].is_light = True


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Create items for game
dagger = Item(
    'dagger', 'A small but very sharp dagger. Good for cutting things.')
coins = Item('coins', "A small pile of gold coins. Shine brightly in the light")
treasure = Item('treasure', 'A large pile of treasure')
rope = Item('rope', 'A very sturdy long piece of rope. Could be useful...')
flashlight = LightSource('flashlight', 'A tool used to see in the dark')
backpack = Pack('backpack', 'A good way to carry more items', 3)

# Add items to the respective rooms
room['foyer'].items = [dagger, backpack]
room['overlook'].items = [rope]
room['narrow'].items = [treasure]
room['treasure'].items = [coins]
room['outside'].items = [flashlight]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
playerName = input("Please enter your name: \n")
player1 = Player(playerName, room['outside'])
print("\nWelcome %s" % (player1.name))
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# checks that the direction provided is either n, s, e or w


def getDirection(direction):
    switchDirections = ['n', 's', 'e', 'w']
    for item in switchDirections:
        if direction == item:
            return True
    return False


def itemChoice():
    if(player1.current_room.is_light == True or flashlight in player1.inventory):
        userDir = 'c'
        while userDir != 'q':
            print("#############################################\n\n")
            if (len(player1.current_room.items) != 0):
                items = "You find the item(s): \n"
                for item in player1.current_room.items:
                    items += item.name + ': ' + item.description + "\n"

                print(items)
                askUser = "What do you want to do? \n"
                for item in player1.current_room.items:
                    askUser += "get or take " + item.name + "\n"
                userDir = input(askUser)
            else:
                print("\nThere are no more items to get here.\n")
                userDir = input(
                    "What do you want to do? \n Enter q to continue your adventure: \n")

            print('\n')

            commands = userDir.split()

            if commands[0].lower() == 'get' or commands[0].lower() == 'take':
                for item in player1.current_room.items:
                    if item.name == commands[1].lower():
                        player1.inventory.append(item)
                        player1.current_room.items.remove(item)
                        item.on_take()
            elif commands[0] == 'q':
                continue
            else:
                print("Please enter a valid command or item name\n")
    else:
        print("It's pitch black! You can't see anything. Perhaps you should find something to help see in the dark\n")


def dropItem():
    print("#############################################\n\n")
    userDir = 'c'

    if backpack in player1.inventory:
        while len(player1.inventory) > 4:
            print(
                "You have too many items to carry. \n You can only carry 4 items at a time\n")
            prompt = "What would you like to do?\n"
            for item in player1.inventory:
                prompt += "drop or remove " + item.name + "\n"
            userDir = input(prompt + "\n")

            commands = userDir.split()

            if commands[0].lower() == 'drop' or commands[0].lower() == 'remove':
                for item in player1.inventory:
                    if item.name == commands[1].lower():
                        player1.inventory.remove(item)
                        player1.current_room.items.append(item)
                        item.on_drop()
            else:
                print("Please enter a valid command or item name\n")
    else:
        while len(player1.inventory) > 1:
            print(
                "You have too many items to carry. \n You can only carry 1 item at a time\n")

            prompt = "What would you like to do?\n"
            for item in player1.inventory:
                prompt += "drop or remove " + item.name + "\n"
            userDir = input(prompt + "\n")

            commands = userDir.split()

            if commands[0].lower() == 'drop' or commands[0].lower() == 'remove':
                for item in player1.inventory:
                    if item.name == commands[1].lower():
                        player1.inventory.remove(item)
                        player1.current_room.items.append(item)
                        item.on_drop()
            else:
                print("Please enter a valid command or item name\n")


userDir = 'c'

while userDir != 'q':
    # checks if the player's inventory is full
    if backpack in player1.inventory:
        if len(player1.inventory) > 4:
            dropItem()
    elif len(player1.inventory) > 1:
        dropItem()

    print("#############################################\n\n")

    if(player1.current_room.is_light == True or flashlight in player1.inventory):
        print('\nYou find yourself in %s. %s\n' % (
            player1.current_room.name, player1.current_room.description))
        userDir = input(
            'Please enter a command of the following choices: \n Direction to move: n, s, e, w. \n Perform an action: Look around, Check inventory \n Enter q to quit: \n')
        print("\n")
    else:
        print("It's pitch black! You can't see anything. Perhaps you should find something to help see in the dark\n")
        userDir = input(
            'Please enter a command of the following choices: \n Direction to move: n, s, e, w. \n Perform an action: Look around, Check inventory \n Enter q to quit: \n')
        print("\n")

    if userDir.isalpha() and len(userDir) == 1:
        userDir = userDir.lower()
        if getDirection(userDir):
            if userDir == 'n':
                try:
                    player1.current_room = player1.current_room.n_to
                except:
                    print("You can't go that way\n")
            elif userDir == 's':
                try:
                    player1.current_room = player1.current_room.s_to
                except:
                    print("You can't go that way\n")
            elif userDir == 'e':
                try:
                    player1.current_room = player1.current_room.e_to
                except:
                    print("You can't go that way\n")
            else:
                try:
                    player1.current_room = player1.current_room.w_to
                except:
                    print("You can't go that way\n")
        else:
            if userDir != 'q':
                print('Please enter n, s, e or w\n')
    else:
        # checks that there are no numbers in the string
        hasNumbers = False
        for c in userDir:
            if c.isdigit():
                hasNumbers = True

        commands = userDir.split()
        if commands[0].capitalize() == 'Look' and commands[1].lower() == 'around':
            if len(player1.current_room.items) == 0:
                print('There are no items here.\n')
            else:
                itemChoice()
        elif commands[0].capitalize() == 'Check' and commands[1].lower() == 'inventory':
            inventory = "Items in inventory: \n"

            if(len(player1.inventory) == 0):
                print(inventory + "You have no items")
            else:
                for item in player1.inventory:
                    inventory += item.name + "\n"
                print(inventory)
        elif hasNumbers:
            print("Please enter a word or character, not a number.\n")
        else:
            print("Please enter a valid command.\n")
