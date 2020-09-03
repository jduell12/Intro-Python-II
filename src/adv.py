from player import Player
from room import Room
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),
    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east."""),
    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),
    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air."""),
    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""),
}


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

# Add items to the respective rooms
room['foyer'].items = [dagger]
room['overlook'].items = [rope]
room['narrow'].items = [treasure]
room['treasure'].items = [coins]

# print(room['outside'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player1 = Player('Jess', room['outside'])
print("Welcome %s" % (player1.name))
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
    userDir = 'c'
    while userDir != 'q':
        if (len(player1.current_room.items) != 0):
            print("You find the item(s): \n %s: %s\n" % (
                player1.current_room.items[0].name, player1.current_room.items[0].description))
            userDir = input("What do you want to do? \n get or take %s \n Enter q to continue your adventure: \n" % (
                player1.current_room.items[0].name))
        else:
            print("\nThere are no more items to get here.\n")
            userDir = input(
                "What do you want to do? \n Enter q to continue your adventure: \n")

        commands = userDir.split()

        if commands[0].lower() == 'get' or commands[0].lower() == 'take':
            for item in player1.current_room.items:
                if item.name == commands[1]:
                    player1.inventory.append(item)
                    player1.current_room.items.remove(item)
        else:
            print("Please enter a valid command\n")


userDir = 'c'

while userDir != 'q':
    print('\nYou find yourself in %s. %s\n' % (
        player1.current_room.name, player1.current_room.description))
    userDir = input(
        'Please enter a command of the following choices: \n Direction to move: n, s, e, w. \n Perform an action: Look around \n Enter q to quit: \n')
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
        elif hasNumbers:
            print("Please enter a word or character, not a number.\n")
        else:
            print("Please enter a valid command.\n")
