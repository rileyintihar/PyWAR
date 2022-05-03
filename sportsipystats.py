from sportsipy.mlb.teams import Teams
from sportsipy.mlb.roster import Player


def print_team_wins():
    teams = Teams()
    for team in teams:
        print(f'{team.abbreviation} has {team.wins} wins so far this season.')


def print_team_losses():
    teams = Teams()
    for team in teams:
        print(f'{team.abbreviation} has {team.losses} losses so far this season.')


def get_player_stats():
    player_selection = input('Enter player\'s first five letters of last name, first two letters of first name, and 01 at the end with no spaces: ')
    p = Player(player_selection)
    print()
    print(f'Player\'s career number of hits is {p.hits}.')
    print(f'Player\'s career number of plate appearances is {p.plate_appearances}.')
    print(f'Player\'s career number of strikeouts is {p.times_struck_out}.')
    print(f'Player\'s career walk count is {p.bases_on_balls}.')
    print(f'Player\'s career RBI count is {p.runs_batted_in}.')
    print(f'Player\'s career complete game count is {p.complete_games}.')
    print(f'Player\'s career on base percentage is {p.on_base_percentage}.')
    print(f'Player\'s career slugging percentage is {p.slugging_percentage}.')
    print(f'Player\'s career on base plus slugging percentage plus is {p.on_base_plus_slugging_percentage_plus}.')
    print(f'Player\'s career putout count is {p.putouts}.')
    print(f'Player\'s career assist count is {p.assists}.')
    print(f'Player\'s career error count is {p.errors}.')
    print()
    print('Pitching stats if applicable:')
    print()
    print(f'Player\'s career thrown strikeout count is {p.strikeouts}.')
    print(f'Player\'s career thrown walk count is {p.bases_on_balls_given}.')
    print(f'Player\'s career wild pitch count is {p.wild_pitches}.')
    print(f'Player\'s career earned runs count is {p.earned_runs_allowed}.')
    print(f'Player\'s career hits allowed count is {p.hits_allowed}.')
    print(f'Player\'s career batters faced count is {p.batters_faced}.')




