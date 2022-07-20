# Student name: Paige Flaherty
# Project Two, IT-140

def show_instructions():
    # This function defines the game instructions and will print to the player when called.
    print(' >^.^<   One Cat\'s Revenge Adventure Game   >^.^<  ')
    print('Your humans have adopted an evil puppy that must be destroyed.')
    print('Collect all 6 items to win the game and defeat the evil puppy.')
    print('Move Commands: go South, go North, go East, go West')
    print('Add item to Inventory: get \'item name\'')
    return 'To quit the game enter \'exit\'.'


def get_move_command(command):
    # This function obtains command input and will split the command, and determine if command is valid.
    while True:  # While True is used to loop through if invalid entry is entered.
        command = input('Enter your move: ').title()  # Using .title to auto format input string, e.g "South"
        command = command.split()  # Splitting input.
        if command[0] in ['Go', 'Get', 'Exit']:  # These are the valid commands per the game instructions.
            return command
        else:
            print('Invalid command')  # Output message to user if entered command is invalid.


def puppy_found():
    # For fun/additional practice created a function containing ASCII art to be called if the villain is found.
    print('BARK BARK.. GAME OVER!!!')
    print('     /^-----^\        ')
    print('     V  o o  V        ')
    print('      |  Y  |         ')
    print('       \ U /          ')
    print('       / - \          ')
    print('       |    \         ')
    print('       |     \    )   ')
    print('       || (___\====   ')
    print('       --------       ')
    print('Thanks for playing the game, hope you enjoyed it!')


def cat_wins():
    # For fun/additional practice created a function containing ASCII art to be called if player collects all 6 items.
    print('Congratulations! You have collected all 6 items and defeated the evil puppy!')
    print('      ,_     _,        ')
    print('      |\\\___//|       ')
    print('      | ^   ^ |        ')
    print('     =\=(_Y_)=/=       ')
    print('       )--*--(    ,    ')
    print('      /       \  ((    ')
    print('      |       |   ))   ')
    print('     /| |   | |\_//    ')
    print('     \| |._.| |/-`     ')
    print('       ""    ""        ')
    print('Thanks for playing the game, hope you enjoyed it!')


def exit_game():
    # For fun/additional practice created a function to be called if player exits the game.
    print('Thanks for playing One Cat\'s Revenge Adventure Game. Hope you enjoyed it!')
    print(' ***                             **   ')
    print(' ***                             **   ')
    print(' ***                             **   ')
    print(' ******.  ***  ***  .****.       **   ')
    print(' ***  *** ***  *** ***  ***           ')
    print(' ***  *** ***  *** ********     ****  ')
    print(' ***  *** ***  *** ***.        ****** ')
    print(' ******"  "*******  "*****"     ****  ')
    print('              ***                     ')
    print('         *** ****                     ')
    print('          "****"                      ')
    print('Purr-haps you\'ll play again soon!  >^.^< ')


def main():
    inventory_add = []  # Creating empty list to be called in update_inventory function.

    def get_new_room(current_roomstate, direction):
        # This function is called if player entered a "Go" command. Function will use the rooms dictionary to identify
        # current location and then determine player's new room.
        new_room = current_roomstate  # This is in case the player enters invalid direction, we stay in current room.
        for i in rooms:  # Step through all of the rooms in the dictionary until,
            if i == current_roomstate:  # the current room is found.
                if direction in rooms[i]:  # If the direction the player entered is in the dict. for the current room,
                    new_room = rooms[i][direction]  # set the new room to the room in the dictionary.
                elif direction not in rooms[i]:  # If direction is not in dict., present player with output message.
                    print('You can\'t go that way!')
                return new_room  # The main program will set the results of this function to be the current room.

    def show_status(current_roomstate, inventory_add, room_inventory):
        # This function will print the player's current room, current inventory, and unretrieved items in current room.
        print('You are in the', current_roomstate)
        print('Inventory:', inventory_add)  # This is a list.
        room_inventory = ()
        room_inventory = get_room_inventory(current_roomstate, room_inventory)  # Calling get_room_inventory function.
        if room_inventory is None:  # If room does not contain any item, then do not print anything.
            pass
        elif room_inventory in inventory_add:  # If room item is already listed in the player's inventory,
            pass                               # then do not print room_inventory.
        elif room_inventory not in inventory_add:  # If room item is not listed in player's inventory, then:
            if room_inventory != 'Puppy':  # if item not puppy, print this message that item is available in room.
                print('You see a', room_inventory)
            elif room_inventory == 'Puppy':  # If item is puppy, print this message that you see see the villain.
                print('You see the evil', room_inventory)
        print('~-------------------------------------~')  # Including linebreak to improve output readability/UX.

    def get_room_inventory(current_roomstate, room_inventory):
        # This function will use the rooms dictionary to identify the item available in the room.
        for i in rooms:  # Step through all of the rooms in the dictionary until,
            if i == current_roomstate:  # the current room is found.
                try:
                    room_inventory = rooms[i]['item']
                except KeyError:  # Using except KeyError to bypass KeyError is room does not contain an item.
                    room_inventory = None  # Otherwise player would receive KeyError.
        return room_inventory  # The main program will set the results of this function to be the current room.

    def update_inventory(current_roomstate, room_inventory):
        # This function is called if player entered a "Get" command. Function will use rooms dictionary to determine
        # that item entered is a valid entry and if so the player's inventory will be updated. Note: inventory_add
        # list must be created outside of function otherwise data will continuously be overridden.
        for i in rooms:  # Step through all of the rooms in the dictionary until,
            if i == current_roomstate:  # the current room is found.
                try:
                    if room_inventory == rooms[i]['item']:  # Item entered by player is listed in rooms dict. for room
                        print(room_inventory, 'successfully retrieved!')
                        inventory_add.append(room_inventory)
                        if total_inventory(inventory_add) < 6:  # Calling total_inventory function to determine list
                            continue                            # count, if < 6 then game will continue.
                        elif total_inventory(inventory_add) == 6:  # Calling total_inventory function to determine list
                            cat_wins()                          # count, if == 6 then game over and player wins!
                            exit()  # exits game/program
                    elif room_inventory != rooms[i]['item']:  # Item entered by player isn't listed in rooms dict-room
                        print(room_inventory, 'is not a valid item for this room.')
                except KeyError:  # Using except KeyError to bypass KeyError if user enters 'Get North' as initial
                    print(room_inventory, 'is not a valid item for this room.')  # command in gameplay.
                    pass                                                 # Otherwise player would receive KeyError.
        return inventory_add

    def total_inventory(inventory_add):
        # This function is used to count the number of items in player's inventory list.
        if inventory_add is None:  # If player's inventory list is empty, assign count value 0
            count_inventory = 0
        elif inventory_add is not None:  # If player's inventory list is not empty, perform count using len function.
            count_inventory = len(inventory_add)
        return count_inventory

    # The dictionary links a room to other rooms, as well as room items and the villain.
    rooms = {
        'Hallway': {'East': 'Basement', 'North': 'Kitchen'},
        'Basement': {'West': 'Hallway', 'item': 'Mouse'},
        'Kitchen': {'North': 'Living Room', 'South': 'Hallway', 'East': 'Bedroom', 'West': 'Office', 'item': 'Bone'},
        'Office': {'East': 'Kitchen', 'item': 'Puppy'},
        'Bedroom': {'West': 'Kitchen', 'North': 'Nursery', 'item': 'Laser'},
        'Nursery': {'South': 'Bedroom', 'item': 'Catnip'},
        'Living Room': {'South': 'Kitchen', 'West': 'Attic', 'item': 'Leash'},
        'Attic': {'East': 'Living Room', 'item': 'Trunk'}
    }

    current_room = 'Hallway'  # Start player in the Hallway.
    inventory = []  # Creating empty inventory to be called by show_status function.
    room_item = ()  # Creating empty room_item to be called by show_status function.
    move_command = ()  # Creating empty move_command.

    print(show_instructions())  # Call and print the instructions defined in the function.

    # loop forever
    while True:
        print('~-------------------------------------~')  # Including linebreak to improve output readability/UX.
        show_status(current_room, inventory, room_item)
        if current_room != 'Office':  # Using if to iterate as long as current_room is not office (villain room).
            move_command = get_move_command(move_command)  # Calls get_move_command function.
            if move_command[0] == 'Go':  # Calling get_new_room function and assigning new room,
                current_room = get_new_room(current_room, move_command[1])  # using move_command[1] from split input.
            elif move_command[0] == 'Get':  # Calling update_inventory function and updating inventory,
                inventory = update_inventory(current_room, move_command[1])  # using move_command[1] from split input.
            elif move_command[0] == 'Exit':  # Calling exit_game function when player inputs exit as move command.
                exit_game()
                exit()  # exits game/program
            else:
                None
        elif current_room == 'Office':  # Else if current_room is office, then call puppy_found function and end game.
            puppy_found()
            exit()


if __name__ == "__main__":  # Must be used with main function, it calls and runs the function.
    main()
