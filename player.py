# Collects basic player stats and goes into specialized position stat collection for eventual advanced stat calculation

player_list_text = open('player_list.txt', 'r')
player_list = player_list_text.read().splitlines()

player_number_list_text = open('player_number_list.txt', 'r')
player_number_list = player_number_list_text.read().splitlines()


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
                print(f'The player\'s name is {player_list[i]}, and their number is {player_number_list[i]}.')
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


fielder_list_text = open('fielder_list.txt', 'r')
fielder_list = fielder_list_text.read().splitlines()

fielder_position_list_text = open('fielder_position_list.txt', 'r')
fielder_position_list = fielder_position_list_text.read().splitlines()

fielder_ab_list_text = open('fielder_ab_list.txt', 'r')
fielder_ab_list = fielder_ab_list_text.read().splitlines()

fielder_hit_list_text = open('fielder_hit_list.txt', 'r')
fielder_hit_list = fielder_hit_list_text.read().splitlines()

fielder_bb_list_text = open('fielder_bb_list.txt', 'r')
fielder_bb_list = fielder_bb_list_text.read().splitlines()

fielder_k_list_text = open('fielder_k_list.txt', 'r')
fielder_k_list = fielder_k_list_text.read().splitlines()

fielder_rbi_list_text = open('fielder_rbi_list.txt', 'r')
fielder_rbi_list = fielder_rbi_list_text.read().splitlines()

fielder_single_list_text = open('fielder_single_list.txt', 'r')
fielder_single_list = fielder_single_list_text.read().splitlines()

fielder_double_list_text = open('fielder_double_list.txt', 'r')
fielder_double_list = fielder_double_list_text.read().splitlines()

fielder_triple_list_text = open('fielder_triple_list.txt', 'r')
fielder_triple_list = fielder_triple_list_text.read().splitlines()

fielder_hr_list_text = open('fielder_hr_list.txt', 'r')
fielder_hr_list = fielder_hr_list_text.read().splitlines()

fielder_hbp_list_text = open('fielder_hbp_list.txt', 'r')
fielder_hbp_list = fielder_hbp_list_text.read().splitlines()

fielder_sb_list_text = open('fielder_sb_list.txt', 'r')
fielder_sb_list = fielder_sb_list_text.read().splitlines()

fielder_putout_list_text = open('fielder_putout_list.txt', 'r')
fielder_putout_list = fielder_putout_list_text.read().splitlines()

fielder_e_list_text = open('fielder_e_list.txt', 'r')
fielder_e_list = fielder_e_list_text.read().splitlines()


class Fielder(Player):
    def __init__(self, name=None, position=None, ab=None, hit=None, bb=None, k=None, rbi=None, single=None, double=None, triple=None, hr=None, hbp=None, sb=None, putout=None, e=None):
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
        self.hbp = hbp
        self.sb = sb
        self.putout = putout
        self.e = e

    def get_fielder_info(self):
        print(f'Below, you\'ll enter fielder stats.')
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
        self.hbp = input('Enter player\'s number of times hit by pitch: ')
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
        fielder_hbp_list.append(self.hbp)
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
                print(f'{player_list[i]} plays {self.position}.')
                print()
        if self.position not in fielder_position_list:
            print()
            print('No players play the inputted position. Please try again.')
            print()

    def calculate_avg(self):
        self.name = input('Enter player name for calculation: ')
        for i in range(0, len(player_list)):
            if self.name == player_list[i]:
                avg = float(fielder_hit_list[i]) / float(fielder_ab_list[i])
                print()
                print(f'{self.name} is batting {avg}.')
                print()
            if self.name not in player_list:
                print()
                print('That player\'s name was not found in the list of added players. Please try again.')
                print()

    def calculate_obp(self):
        self.name = input('Enter player name for calculation: ')
        for i in range(0, len(player_list)):
            if self.name == player_list[i]:
                obp = (float(fielder_hit_list[i]) + float(fielder_bb_list[i]) + float(fielder_hbp_list[i])) / float(fielder_ab_list[i])
                print()
                print(f'{self.name} has an on base percentage of {obp}.')
                print()
            if self.name not in player_list:
                print()
                print('That player\'s name was not found in the list of added players. Please try again.')
                print()

    def calculate_slg(self):
        self.name = input('Enter player name for calculation: ')
        for i in range(0, len(player_list)):
            if self.name == player_list[i]:
                slg = ((int(fielder_single_list[i]) + int(fielder_double_list[i] * 2) + int(fielder_triple_list[i] * 3) + int(fielder_hr_list[i] * 4)) / int(fielder_ab_list[i]))
                print()
                print(f'{self.name} has a slugging percentage of {slg}.')
                print()
        if self.name not in player_list:
            print()
            print('That player\'s name was not found in the list of added players. Please try again.')
            print()

    def calculate_ops(self):
        self.name = input('Enter player name for calculation: ')
        for i in range(0, len(player_list)):
            if self.name == player_list[i]:
                ops = (((int(fielder_single_list[i]) + int(fielder_double_list[i] * 2) + int(fielder_triple_list[i] * 3) + int(fielder_hr_list[i] * 4)) / int(fielder_ab_list[i])) / 100) + ((float(fielder_hit_list[i]) + float(fielder_bb_list[i]) + float(fielder_hbp_list[i])) / float(fielder_ab_list[i]))
                print()
                print(f'{self.name} has an on base plus slugging value of {ops}.')
                print()
        if self.name not in player_list:
            print()
            print('That player\'s name was not found in the list of added players. Please try again.')
            print()

    def calculate_bb_percent(self):
        self.name = input('Enter player name for calculation: ')
        for i in range(0, len(player_list)):
            if self.name == player_list[i]:
                bb_percent = int(fielder_bb_list[i]) / int(fielder_ab_list[i])
                print()
                print(f'{self.name} has a walk percentage of {bb_percent}.')
                print()
        if self.name not in player_list:
            print()
            print('That player\'s name was not found in the list of added players. Please try again.')
            print()

    def calculate_k_percent(self):
        self.name = input('Enter player name for calculation: ')
        for i in range(0, len(player_list)):
            if self.name == player_list[i]:
                k_percent = int(fielder_k_list[i]) / int(fielder_ab_list[i])
                print()
                print(f'{self.name} has a strikeout percentage of {k_percent}.')
                print()
        if self.name not in player_list:
            print()
            print('That player\'s name was not found in the list of added players. Please try again.')
            print()

    def calculate_bb_to_k_ratio(self):
        self.name = input('Enter player name for calculation: ')
        for i in range(0, len(player_list)):
            if self.name == player_list[i]:
                bb_to_k_ratio = int(fielder_bb_list[i]) / int(fielder_k_list[i])
                print()
                print(f'{self.name} has a walk to strikeout ratio of {bb_to_k_ratio}.')
                print()
        if self.name not in player_list:
            print()
            print('That player\'s name was not found in the list of added players. Please try again.')
            print()

    def calculate_ab_to_hr_ratio(self):
        self.name = input('Enter player name for calculation: ')
        for i in range(0, len(player_list)):
            if self.name == player_list[i]:
                ab_to_hr_ratio = int(fielder_ab_list[i]) / int(fielder_hr_list[i])
                print()
                print(f'{self.name} has an at bat to home run ratio of {ab_to_hr_ratio}.')
                print()
        if self.name not in player_list:
            print()
            print('That player\'s name was not found in the list of added players. Please try again.')
            print()

    def calculate_xbh(self):
        self.name = input('Enter player name for calculation: ')
        for i in range(0, len(player_list)):
            if self.name == player_list[i]:
                xbh = (int(fielder_double_list[i]) + int(fielder_triple_list[i]) + int(fielder_hr_list[i]))/ int(fielder_ab_list[i])
                print()
                print(f'{self.name} has an extra base hit percentage of {xbh}.')
                print()
        if self.name not in player_list:
            print()
            print('That player\'s name was not found in the list of added players. Please try again.')
            print()


pitcher_list_text = open('pitcher_list.txt', 'r')
pitcher_list = pitcher_list_text.read().splitlines()

pitcher_type_list_text = open('pitcher_type_list.txt', 'r')
pitcher_type_list = pitcher_type_list_text.read().splitlines()

pitcher_k_list_text = open('pitcher_k_list.txt', 'r')
pitcher_k_list = pitcher_k_list_text.read().splitlines()

pitcher_bb_list_text = open('pitcher_bb_list.txt', 'r')
pitcher_bb_list = pitcher_bb_list_text.read().splitlines()

pitcher_ip_list_text = open('pitcher_ip_list.txt', 'r')
pitcher_ip_list = pitcher_ip_list_text.read().splitlines()

pitcher_w_list_text = open('pitcher_w_list.txt', 'r')
pitcher_w_list = pitcher_w_list_text.read().splitlines()

pitcher_l_list_text = open('pitcher_l_list.txt', 'r')
pitcher_l_list = pitcher_l_list_text.read().splitlines()

pitcher_save_list_text = open('pitcher_save_list.txt', 'r')
pitcher_save_list = pitcher_save_list_text.read().splitlines()

pitcher_strike_list_text = open('pitcher_strike_list.txt', 'r')
pitcher_strike_list = pitcher_strike_list_text.read().splitlines()

pitcher_ball_list_text = open('pitcher_ball_list.txt', 'r')
pitcher_ball_list = pitcher_ball_list_text.read().splitlines()

pitcher_hbp_list_text = open('pitcher_hbp_list.txt', 'r')
pitcher_hbp_list = pitcher_hbp_list_text.read().splitlines()

pitcher_e_list_text = open('pitcher_e_list.txt', 'r')
pitcher_e_list = pitcher_e_list_text.read().splitlines()


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
        print(f'Below, you\'ll enter pitcher stats.')
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

    def search_pitcher_type(self):
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

    def calculate_strike_percentage(self):
        self.name = input('Enter player name for calculation: ')
        for i in range(0, len(player_list)):
            if self.name == player_list[i]:
                strike_percent = int(pitcher_strike_list[i]) / (int(pitcher_strike_list[i]) + int(pitcher_ball_list[i]))
                print()
                print(f'{self.name} has a strike percentage of {strike_percent}.')
                print()
        if self.name not in player_list:
            print()
            print('That player\'s name was not found in the list of added players. Please try again.')
            print()

    def calculate_ball_percentage(self):
        self.name = input('Enter player name for calculation: ')
        for i in range(0, len(player_list)):
            if self.name == player_list[i]:
                ball_percent = int(pitcher_ball_list[i]) / (int(pitcher_ball_list[i]) + int(pitcher_strike_list[i]))
                print()
                print(f'{self.name} has a ball percentage of {ball_percent}.')
                print()
        if self.name not in player_list:
            print()
            print('That player\'s name was not found in the list of added players. Please try again.')
            print()

    def calculate_hbp_percentage(self):
        self.name = input('Enter player name for calculation: ')
        for i in range(0, len(player_list)):
            if self.name == player_list[i]:
                hbp_percent = int(pitcher_hbp_list[i]) / (int(pitcher_strike_list[i]) + int(pitcher_ball_list[i]))
                print()
                print(f'{self.name} has a hit batsmen per pitch percentage of {hbp_percent}.')
                print()
        if self.name not in player_list:
            print()
            print('That player\'s name was not found in the list of added players. Please try again.')
            print()

    def calculate_bb_to_k_percentage(self):
        self.name = input('Enter player name for calculation: ')
        for i in range(0, len(player_list)):
            if self.name == player_list[i]:
                bb_to_k_percent = int(pitcher_bb_list[i]) / int(pitcher_k_list[i])
                print()
                print(f'{self.name} has a walk to strikeout percentage of {bb_to_k_percent}.')
                print()
        if self.name not in player_list:
            print()
            print('That player\'s name was not found in the list of added players. Please try again.')
            print()

    def calculate_w_percentage(self):
        self.name = input('Enter player name for calculation: ')
        for i in range(0, len(player_list)):
            if self.name == player_list[i]:
                w_percent = int(pitcher_w_list[i]) / (int(pitcher_w_list[i]) + int(pitcher_l_list[i]))
                print()
                print(f'{self.name} has a win percentage of {w_percent}.')
                print()
        if self.name not in player_list:
            print()
            print('That player\'s name was not found in the list of added players. Please try again.')
            print()

    def calculate_l_percentage(self):
        self.name = input('Enter player name for calculation: ')
        for i in range(0, len(player_list)):
            if self.name == player_list[i]:
                l_percent = int(pitcher_l_list[i]) / (int(pitcher_w_list[i]) + int(pitcher_l_list[i]))
                print()
                print(f'{self.name} has a win percentage of {l_percent}.')
                print()
        if self.name not in player_list:
            print()
            print('That player\'s name was not found in the list of added players. Please try again.')
            print()

    def calculate_war_percentage(self):
        self.name = input('Enter player name for calculation: ')
        war_factor = 11.266578 # MLB 2021 Average
        for i in range(0, len(player_list)):
            if self.name == player_list[i]:
                war = ((int(pitcher_w_list[i]) + int(pitcher_save_list[i]) + int(pitcher_ip_list[i])) * war_factor) / int(pitcher_k_list[i]) * war_factor
                print()
                print(f'{self.name} has a WAR rating (using 2021 average WAR factor) of {war}.')
                print()
        if self.name not in player_list:
            print()
            print('That player\'s name was not found in the list of added players. Please try again.')
            print()


def clear_all():
    player_list.clear()
    player_number_list.clear()
    fielder_list.clear()
    fielder_position_list.clear()
    fielder_ab_list.clear()
    fielder_hit_list.clear()
    fielder_bb_list.clear()
    fielder_k_list.clear()
    fielder_rbi_list.clear()
    fielder_single_list.clear()
    fielder_double_list.clear()
    fielder_triple_list.clear()
    fielder_hr_list.clear()
    fielder_hbp_list.clear()
    fielder_sb_list.clear()
    fielder_putout_list.clear()
    fielder_e_list.clear()
    pitcher_list.clear()
    pitcher_type_list.clear()
    pitcher_k_list.clear()
    pitcher_bb_list.clear()
    pitcher_ip_list.clear()
    pitcher_w_list.clear()
    pitcher_l_list.clear()
    pitcher_save_list.clear()
    pitcher_strike_list.clear()
    pitcher_ball_list.clear()
    pitcher_hbp_list.clear()
    pitcher_e_list.clear()


def save_and_exit():
    save_text = open('player_list.txt', 'w')
    for stat in player_list:
        save_text.write("%s\n" % str(stat))
    save_text.close()

    save_text = open('player_number_list.txt', 'w')
    for stat in player_number_list:
        save_text.write("%s\n" % str(stat))
    save_text.close()

    save_text = open('fielder_list.txt', 'w')
    for stat in fielder_list:
        save_text.write("%s\n" % str(stat))
    save_text.close()

    save_text = open('fielder_position_list.txt', 'w')
    for stat in fielder_position_list:
        save_text.write("%s\n" % str(stat))
    save_text.close()

    save_text = open('fielder_ab_list.txt', 'w')
    for stat in fielder_ab_list:
        save_text.write("%s\n" % str(stat))
    save_text.close()

    save_text = open('fielder_hit_list.txt', 'w')
    for stat in fielder_hit_list:
        save_text.write("%s\n" % str(stat))
    save_text.close()

    save_text = open('fielder_bb_list.txt', 'w')
    for stat in fielder_bb_list:
        save_text.write("%s\n" % str(stat))
    save_text.close()

    save_text = open('fielder_k_list.txt', 'w')
    for stat in fielder_k_list:
        save_text.write("%s\n" % str(stat))
    save_text.close()

    save_text = open('fielder_rbi_list.txt', 'w')
    for stat in fielder_rbi_list:
        save_text.write("%s\n" % str(stat))
    save_text.close()

    save_text = open('fielder_single_list.txt', 'w')
    for stat in fielder_single_list:
        save_text.write("%s\n" % str(stat))
    save_text.close()

    save_text = open('fielder_double_list.txt', 'w')
    for stat in fielder_double_list:
        save_text.write("%s\n" % str(stat))
    save_text.close()

    save_text = open('fielder_triple_list.txt', 'w')
    for stat in fielder_triple_list:
        save_text.write("%s\n" % str(stat))
    save_text.close()

    save_text = open('fielder_hr_list.txt', 'w')
    for stat in fielder_hr_list:
        save_text.write("%s\n" % str(stat))
    save_text.close()

    save_text = open('fielder_hbp_list.txt', 'w')
    for stat in fielder_hbp_list:
        save_text.write("%s\n" % str(stat))
    save_text.close()

    save_text = open('fielder_sb_list.txt', 'w')
    for stat in fielder_sb_list:
        save_text.write("%s\n" % str(stat))
    save_text.close()

    save_text = open('fielder_putout_list.txt', 'w')
    for stat in fielder_putout_list:
        save_text.write("%s\n" % str(stat))
    save_text.close()

    save_text = open('fielder_e_list.txt', 'w')
    for stat in fielder_e_list:
        save_text.write("%s\n" % str(stat))
    save_text.close()

    save_text = open('pitcher_list.txt', 'w')
    for stat in pitcher_list:
        save_text.write("%s\n" % str(stat))
    save_text.close()

    save_text = open('pitcher_type_list.txt', 'w')
    for stat in pitcher_type_list:
        save_text.write("%s\n" % str(stat))
    save_text.close()

    save_text = open('pitcher_k_list.txt', 'w')
    for stat in pitcher_k_list:
        save_text.write("%s\n" % str(stat))
    save_text.close()

    save_text = open('pitcher_bb_list.txt', 'w')
    for stat in pitcher_bb_list:
        save_text.write("%s\n" % str(stat))
    save_text.close()

    save_text = open('pitcher_ip_list.txt', 'w')
    for stat in pitcher_ip_list:
        save_text.write("%s\n" % str(stat))
    save_text.close()

    save_text = open('pitcher_w_list.txt', 'w')
    for stat in pitcher_w_list:
        save_text.write("%s\n" % str(stat))
    save_text.close()

    save_text = open('pitcher_l_list.txt', 'w')
    for stat in pitcher_l_list:
        save_text.write("%s\n" % str(stat))
    save_text.close()

    save_text = open('pitcher_save_list.txt', 'w')
    for stat in pitcher_save_list:
        save_text.write("%s\n" % str(stat))
    save_text.close()

    save_text = open('pitcher_strike_list.txt', 'w')
    for stat in pitcher_strike_list:
        save_text.write("%s\n" % str(stat))
    save_text.close()

    save_text = open('pitcher_ball_list.txt', 'w')
    for stat in pitcher_ball_list:
        save_text.write("%s\n" % str(stat))
    save_text.close()

    save_text = open('pitcher_hbp_list.txt', 'w')
    for stat in pitcher_hbp_list:
        save_text.write("%s\n" % str(stat))
    save_text.close()

    save_text = open('pitcher_e_list.txt', 'w')
    for stat in pitcher_e_list:
        save_text.write("%s\n" % str(stat))
    save_text.close()
