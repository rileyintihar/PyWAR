# Main menu for PyWAR Baseball Stat Calculator and Analyzer

from player import Player, Fielder, Pitcher, save_and_exit, clear_all

player = Player()
fielder = Fielder()
pitcher = Pitcher()

choice = None
position_choice = None

print('Welcome to PyWAR, the Python-based baseball stat calculator and analyzer.')
print()


while choice != 643:
    print('Enter 1 to add a new player and their info.')
    print('Enter 2 to view a player\'s basic info.')
    print('Enter 3 to view the entire list of added players.')
    print('Enter 4 to search for players by an identifying statistic.')
    print('Enter 5 to calculate stats.')
    print('Enter 6 to clear all saved data.')
    print('Enter 643 (double play reference) to save and exit program.')
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
        elif position_choice == 2:
            print()
            pitcher.get_pitcher_info()
            pitcher.add_pitcher()
            print()

    elif choice == 2:
        player.search_player_name()

    elif choice == 3:
        player.print_player_list()

    elif choice == 4:
        print()
        print('Enter 1 to search for players by name.')
        print('Enter 2 to search for players by number.')
        print('Enter 3 to search for fielders by position.')
        print('Enter 4 to search for pitchers by type.')
        search_choice = int(input('Menu selection: '))
        if search_choice == 1:
            player.search_player_name()
        elif search_choice == 2:
            player.search_player_number()
        elif search_choice == 3:
            fielder.search_fielder_position()
        elif search_choice == 4:
            pitcher.search_pitcher_type()

    elif choice == 5:
        print()
        print('Enter 1 to calculate batting average.')
        print('Enter 2 to calculate on base percentage.')
        print('Enter 3 to calculate slugging percentage.')
        print('Enter 4 to calculate on base plus slugging.')
        print('Enter 5 to calculate walk percentage.')
        print('Enter 6 to calculate strikeout percentage.')
        print('Enter 7 to calculate walk to strikeout ratio.')
        print('Enter 8 to calculate at bat to home run ratio.')
        print('Enter 9 to calculate extra base hit percentage.')
        stat_choice = int(input('Menu selection: '))
        if stat_choice == 1:
            fielder.calculate_avg()
        elif stat_choice == 2:
            fielder.calculate_obp()
        elif stat_choice == 3:
            fielder.calculate_slg()
        elif stat_choice == 4:
            fielder.calculate_ops()
        elif stat_choice == 5:
            fielder.calculate_bb_percent()
        elif stat_choice == 6:
            fielder.calculate_k_percent()
        elif stat_choice == 7:
            fielder.calculate_bb_to_k_ratio()
        elif stat_choice == 8:
            fielder.calculate_ab_to_hr_ratio()
        elif stat_choice == 9:
            fielder.calculate_xbh()

    elif choice == 6:
        clear_all()

save_and_exit()
