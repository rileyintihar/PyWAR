# Adds new player to player database

player_list = []
player_number_list = []

class Player:
    def __init__(self, name=None, number=None, throw=None, bat=None):
        self.name = name
        self.number = number
        self.throw = throw
        self.bat = bat

    def get_player_info(self):
        self.name = input('Enter the player\'s name: ')
        self.number = input('Enter the player\'s number: ')
        self.throw = input('Enter R for a right-handed thrower, and enter L for a left-handed thrower: ')
        self.bat = input('Enter R for a right-handed batter, and enter L for a left-handed batter: ')

    def add_player(self):
        player_list.append(self.name)
        player_number_list.append(self.number)
        print()

    def print_player_info(self):
        self.name = input('Enter a player name to search the player list: ')
        for i in range(0, len(player_list)):
            if self.name == player_list[i]:
                print()
                print(f'The player\'s name is {self.name}, and their number is {self.number}. They throw with their {self.throw} and they bat with their {self.bat}.')
                print()
        if self.name not in player_list:
            print()
            print('That player\'s name was not found in the list of added players. Please try again.')
            print()

    def print_player_number(self):
        self.number = input('Enter a player number to search the player list: ')
        for i in range(0, len(player_list)):
            if self.number == player_number_list[i]:
                print()
                print(f'{player_list[i]} has the inputted jersey number of {self.number}.')
                print()
        if self.number not in player_number_list:
            print()
            print('No player has that jersey number in the list of added players. Please try again.')
            print()


    def print_player_list(self):
        print()
        print(f'Current list of players: {player_list}')
        print()


