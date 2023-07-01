# Cassian
# dict links rooms to other rooms
def main():
    rooms = {
        'Your Cell': {'name': 'Your Cell', 'east': 'Main Room', 'item': 'none'},
        'Main Room': {'name': 'Main Room', 'north': "Nurse's Office", 'south': 'Security', 'east': 'Cafeteria',
                      'west': 'Your Cell', 'item': 'Lock-pick'},
        "Nurse's Office": {'name': "Nurse's Office", 'east': 'Infirmary', 'south': 'Main Room', 'item': 'Badge'},
        'Infirmary': {'name': 'Infirmary', 'west': "Nurse's Office", 'item': 'Scrubs'},
        'Cafeteria': {'name': 'Cafeteria', 'north': 'Library', 'south': 'Rec Room', 'west': 'Main Room',
                      'item': 'Shiv'},
        'Library': {'name': 'Library', 'south': 'Cafeteria', 'item': 'Map'},
        'Rec Room': {'name': 'Rec Room', 'north': 'Cafeteria', 'west': 'Security', 'item': 'Screwdriver'},
        'Security': {'name': 'Security', 'north': 'Main Room', 'east': 'Rec Room', 'item': 'Prison Guard'}
    }

    def intro():
        print('Prison Escape Text Game')
        print("Find the 6 items you need in order to escape the prison wing; "
              "don't let the guard see you until you have all 6")
        print('To move, enter North, East, South, or West')
        print("To pick up an item, enter 'grab'")

    current_room = rooms['Your Cell']
# set starting point
    inventory = []

    def status():
        print('You are currently in', current_room['name'])
    # checking location
        if len(inventory) != 0:
            print('Inventory:', inventory)
            print('_________')
        else:
            print("There's nothing in your inventory")

    intro()

# loop
    while True:
        if current_room['name'] == 'Security':
            if len(inventory) == 6:
                print('Congratulations! You escaped past the guard.')
                break
            else:
                print('STOP! The Prison Guard caught you! Better luck next time.')
                break

        status()
        directions = ['north', 'east', 'south', 'west']

        if current_room['item'] != 'none':
            if current_room['item'] not in inventory:
                print('You see a {}'.format(current_room['item']))
                print('___________')
        # check for item

        player_move = input('Enter move').strip()

        if player_move.lower() in directions:
            if player_move.lower() in current_room:
                current_room = rooms[current_room[player_move.lower()]]
            else:
                print("There's not a door here")
        elif player_move.lower() == 'grab':
            print('You picked up {}'.format(current_room['item']))
            inventory.append(current_room['item'])
        else:
            print('Error: Please enter a valid direction')
        # error if input isn't N,E,S,W,


main()
