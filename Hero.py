class Hero:
    def __init__(self, name, skill_q, skill_w, skill_e, ulti, base_armor, base_mr, base_hp, is_ad):
        self.name = name
        self.skill_q = skill_q
        self.skill_w = skill_w
        self.skill_e = skill_e
        self.ulti = ulti
        self.base_armor = base_armor
        self.base_mr = base_mr
        self.base_hp = base_hp
        self.is_ad = is_ad

    def mevcut_durumu_görüntüle(self):
        if self.is_ad:
            skill_type = "AD"
        else:
            skill_type = "AP"

        print("""
        Name: {}
        Q : {}
        W : {}
        E : {}
        Ulti : {}
        Base Armor : {}
        Base MR : {}
        Base HP : {}
        Skill Type : {}
        """.format(self.name,self.skill_q,self.skill_w,self.skill_e,self.ulti,self.base_armor,
                   self.base_mr,self.base_hp,skill_type))
    def get_hp(self):
        return self.base_hp

    def set_hp(self, damage):
        self.base_hp -= damage


    def get_armor(self):
        return self.base_armor

    def get_mr(self):
        return self.base_mr

    def öldümü(self):
        if self.base_hp < 1:
            return True
        else:
            return False



