from player import Fielder


class FielderStats(Fielder):
    def __init__(self, ab=None, hit=None, bb=None, k=None, rbi=None, single=None, double=None, triple=None, hr=None, sb=None, putout=None, e=None):
        super().__init__(self, ab, hit, bb, k, rbi, single, double, triple, hr, sb, putout, e)

    def calculate_avg(self):
        self.name = input('Enter player name for calculation: ')
        for i in range(0, len(player_list)):
            if self.name == player_list[i]:
                avg = self.hit / self.ab
                print(avg)

    def calculate_obp(self):
        obp = (self.hit + self.bb) / self.ab
        return obp

    def calculate_slg(self):
        slg = (self.single + (self.double * 2) + (self.triple * 3) + (self.hr * 4) / self.ab)
        return slg

    def calculate_ops(self):
        ops = (self.hit + self.bb + self.hbp) / self.ab
        return ops

    def calculate_bb_percentage(self):
        bb_percentage = self.bb / self.ab
        return bb_percentage
