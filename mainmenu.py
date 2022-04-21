# Main menu for PyWAR Baseball Stat Calculator and Analyzer
from player import Player

player = Player()

choice = None

print('Welcome to PyWAR, the Python-based baseball stat calculator and analyzer.')
print()


while choice != 9:
    print('Enter 1 to add a new player and their info.')
    print('Enter 2 to view a player\'s basic info.')
    print('Enter 9 to exit program.')
    choice = int(input('Menu selection: '))
    if choice == 1:
        player.get_player_info()
        player.add_player()
    elif choice == 2:
        player.print_player_info()

