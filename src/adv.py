from room import Room
from player import Player
from item import Item

# Declare all the rooms


room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),


    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

#Declare all the items

items = {
    'gold coin':   Item('Gold Coins', """Here are some small gold coins. Might be valuable."""),
    
    'murder hornet': Item('Murder Hornets', """Attack your enemy if needed with these"""),

    'key': Item('Rusty Key', """Rusty old key lays here, Hopefully opens something."""),

    'hearts': Item('Hearts', """Give a hug to yourself. Adds longevity and an extra life!"""),

} 

#link items to rooms
room['outside'].items = items['key']
room['foyer'].items = items['hearts']
room['overlook'].items = items['murder hornet']
room['narrow'].items = items['gold coin']
room['treasure'].items = (items['gold coin'])

#
# Main
#
print(room['outside'].items)
# Make a new player object that is currently in the 'outside' room.
player_1 = Player("Player_1", room["outside"])

# Write a loop that:
while True:
    player_1.current_room
    # * Prints the current room name
    print("\nYou are now in room:\n", player_1.current_room.name)
    # * Prints the current description (the textwrap module might be useful here).
    print("Description:\n", player_1.current_room.description)
    print(player_1.current_room.items)

# * Waits for user input and decides what to do.
    print("\nWhich direction would you like to move?")
    cmd = input("Press 'n', 's,', 'e', 'w' or ('q' to quit the game):")

# If the user enters "q", quit the game.
    if cmd == 'q':
        print("Thanks for playing.  Have a nice day!")
        break

# If the user enters a cardinal direction, attempt to move to the room there.

    if cmd == 'n':
        print("\nWalking north...\n")
        if player_1.current_room.n_to is None:
            print("****There is no room to the North of you, select different direction.****")
        else:
            player_1.current_room = player_1.current_room.n_to
                
    elif cmd == 's':
        print("\nWalking south...\n")
        if player_1.current_room.s_to is None:
            print("****There is no room to the South of you. Select a different direction.****")
        else:
            player_1.current_room = player_1.current_room.s_to
    elif cmd == 'e':
        print("\nWalking east...\n")
        if player_1.current_room.e_to is None:
            print("****There is no room to the East of you. Select a different direction.****")
        else:
            player_1.current_room = player_1.current_room.e_to
    elif cmd == 'w':
        print("\nWalking west...\n")
        if player_1.current_room.w_to is None:
            print("****There is no room to the West of you. Select a different direction.****")
        else:
            player_1.current_room = player_1.current_room.w_to

# Print an error message if the movement isn't allowed.
    else:
        print ("This movement is not allowed.")



