import pprint
class Skill:
    def __init__(self,name, damage, cd, stype):
        self.name = name
        self.damage = damage
        self.cd = cd
        self.stype = stype

    def get_damage(self):
        return self.damage

    def get_stype(self):
        return self.stype

    def __str__(self):
        return str(pprint.pprint(self.name))
