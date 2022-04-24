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

    def search_player_name(self):
        print()
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

    def search_player_number(self):
        print()
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


fielder_list = []
fielder_position_list = []
fielder_ab_list = []
fielder_hit_list = []
fielder_bb_list = []
fielder_k_list = []
fielder_rbi_list = []
fielder_single_list = []
fielder_double_list = []
fielder_triple_list = []
fielder_hr_list = []
fielder_sb_list = []
fielder_putout_list = []
fielder_e_list = []


class Fielder(Player):
    def __init__(self, name=None, position=None, ab=None, hit=None, bb=None, k=None, rbi=None, single=None, double=None, triple=None, hr=None, sb=None, putout=None, e=None):
        super().__init__(self, name)
        self.position = position
        self.ab = ab
        self.hit = hit
        self.bb = bb
        self.k = k
        self.rbi = rbi
        self.single = single
        self.double = double
        self.triple = triple
        self.hr = hr
        self.sb = sb
        self.putout = putout
        self.e = e

    def get_fielder_info(self):
        print(f'Below, you\'ll enter fielder stats for {self.name}')
        self.position = input('Enter player position abbreviation: ')
        self.ab = input('Enter player\'s number of at bats: ')
        self.hit = input('Enter player\'s number of hits: ')
        self.bb = input('Enter player\'s number of walks: ')
        self.k = input('Enter player\'s number of strikeouts: ')
        self.rbi = input('Enter player\'s number of runs batted in: ')
        self.single = input('Enter player\'s number of singles: ')
        self.double = input('Enter player\'s number of doubles: ')
        self.triple = input('Enter player\'s number of triples: ')
        self.hr = input('Enter player\'s number of home runs: ')
        self.sb = input('Enter player\'s number of stolen bases: ')
        self.putout = input('Enter player\'s number of fielding putouts: ')
        self.e = input('Enter player\'s number of errors: ')

    def add_fielder(self):
        fielder_list.append(self.name)
        fielder_position_list.append(self.position)
        fielder_ab_list.append(self.ab)
        fielder_hit_list.append(self.hit)
        fielder_bb_list.append(self.bb)
        fielder_k_list.append(self.k)
        fielder_rbi_list.append(self.rbi)
        fielder_single_list.append(self.single)
        fielder_double_list.append(self.double)
        fielder_triple_list.append(self.triple)
        fielder_hr_list.append(self.hr)
        fielder_sb_list.append(self.sb)
        fielder_putout_list.append(self.putout)
        fielder_e_list.append(self.e)
        print()

    def search_fielder_position(self):
        print()
        self.position = input('Enter a position abbreviation to search the fielder list: ')
        for i in range(0, len(fielder_position_list)):
            if self.position == fielder_position_list[i]:
                print()
                print(f'{self.name} plays {self.position}.')
                print()
        if self.position not in fielder_position_list:
            print()
            print('No players play the inputted position. Please try again.')
            print()


pitcher_list = []
pitcher_type_list = []
pitcher_k_list = []
pitcher_bb_list = []
pitcher_ip_list = []
pitcher_w_list = []
pitcher_l_list = []
pitcher_save_list = []
pitcher_strike_list = []
pitcher_ball_list = []
pitcher_hbp_list = []
pitcher_e_list = []


class Pitcher(Player):
    def __init__(self, name=None, type=None, k=None, bb=None, ip=None, w=None, l=None, save=None, strike=None, ball=None, hbp=None, e=None):
        super().__init__(self, name)
        self.type = type
        self.k = k
        self.bb = bb
        self.ip = ip
        self.w = w
        self.l = l
        self.save = save
        self.strike = strike
        self.ball = ball
        self.hbp = hbp
        self.e = e

    def get_pitcher_info(self):
        print(f'Below, you\'ll enter pitcher stats for {self.name}')
        self.type = input('Enter SP for a starter, RP for a reliever, and CL for a closer: ')
        self.k = input('Enter pitcher\'s number of strikeouts: ')
        self.bb = input('Enter pitcher\'s number of walks: ')
        self.ip = input('Enter pitcher\'s number of innings pitched: ')
        self.w = input('Enter pitcher\'s number of wins: ')
        self.l = input('Enter pitcher\'s number of losses: ')
        self.save = input('Enter pitcher\'s number of saves: ')
        self.strike = input('Enter pitcher\'s number of strikes thrown: ')
        self.ball = input('Enter pitcher\'s number of balls thrown: ')
        self.hbp = input('Enter pitcher\'s number of hit batsmen: ')
        self.e = input('Enter pitcher\'s number of errors: ')

    def add_pitcher(self):
        pitcher_list.append(self.name)
        pitcher_type_list.append(self.type)
        pitcher_k_list.append(self.k)
        pitcher_bb_list.append(self.bb)
        pitcher_ip_list.append(self.ip)
        pitcher_w_list.append(self.w)
        pitcher_l_list.append(self.l)
        pitcher_save_list.append(self.save)
        pitcher_strike_list.append(self.strike)
        pitcher_ball_list.append(self.ball)
        pitcher_hbp_list.append(self.hbp)
        pitcher_e_list.append(self.e)

    def search_pitcher_position(self):
        print()
        self.type = input('Enter SP, RP, or CL to search the pitcher list: ')
        for i in range(0, len(pitcher_type_list)):
            if self.type == pitcher_type_list[i]:
                print()
                print(f'{self.name} is a {self.type}.')
                print()
        if self.type not in pitcher_type_list:
            print()
            print(f'No pitchers are classified as {self.type}. Please try again.')
            print()

