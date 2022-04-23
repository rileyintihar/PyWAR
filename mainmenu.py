# Main menu for PyWAR Baseball Stat Calculator and Analyzer
from player import Player, Fielder
from stats import FielderStats

player = Player()
fielder = Fielder()
fielder_stats = FielderStats()

choice = None
position_choice = None

print('Welcome to PyWAR, the Python-based baseball stat calculator and analyzer.')
print()


while choice != 9:
    print('Enter 1 to add a new player and their info.')
    print('Enter 2 to view a player\'s info.')
    print('Enter 3 to view the entire list of added players.')
    print('Enter 4 to search for players by an identifying statistic.')
    print('Enter 5 to calculate stats.')
    print('Enter 6 to compare stats.')
    print('Enter 7 to delete a player.')
    print('Enter 9 to save and exit program.')
    choice = int(input('Menu selection: '))

    if choice == 1:
        player.get_player_info()
        player.add_player()
        position_choice = int(input('Enter 1 if the player is a fielder, and enter 2 if the player is a pitcher: '))
        if position_choice == 1:
            print()
            fielder.get_fielder_info()
            fielder.add_fielder()
            print()



    elif choice == 2:
        player.search_player_name()

    elif choice == 3:
        player.print_player_list()

    elif choice == 4:
        player.search_player_number()

    elif choice == 5:
        fielder.search_fielder_position()

    elif choice == 7:
        print('Enter 1 to calculate batting average.')
        print('Enter 1 to calculate distribution of types of hits.')

