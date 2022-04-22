from sportsipy.mlb.teams import Teams


def print_most_losses(year, losses):
    most_losses = max(losses, key=losses.get)
    print('%s: %s - %s' % (year, losses[most_losses], most_losses))


for year in range(2022, 2023):
    losses = {}
    for team in Teams(year):
        losses[team.name] = team.losses
    print_most_losses(year, losses)

