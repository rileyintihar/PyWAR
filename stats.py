from player import Fielder


class FielderStats(Fielder):
    def __init__(self, ab=None, hit=None, bb=None, k=None, rbi=None, single=None, double=None, triple=None, hr=None, sb=None, putout=None, e=None):
        super().__init__(self, ab, hit, bb, k, rbi, single, double, triple, hr, sb, putout, e)

    def calculate_avg(self):
        avg = self.hit / self.ab
        return avg

    def calculate_obp(self):
        obp = (self.hit + self.bb) / self.ab
        return obp


