class Attack:
    def __init__(self, saldıran, saldırılan, skill):
        self.saldıran = saldıran
        self.saldırılan = saldırılan
        self.skill = skill

    def attack(self):
        damage = self.skill.get_damage()
        damage_type = self.skill.get_stype()
        if damage_type == "AD":
            defans = self.saldırılan.get_armor()
        else:
            defans = self.saldırılan.get_mr()
        print("Rakibin HP'si : ",self.saldırılan.get_hp())
        print("Hasarınız : ",damage)
        eksilecek_damage = damage * (defans * 20.0 / 100.0) / 100
        sonuç = damage - eksilecek_damage
        print("Verdiğiniz Hasar : ", sonuç)
        self.saldırılan.set_hp(sonuç)
        print("Rakinizin Kalan Hp'si : ",self.saldırılan.get_hp())
        return sonuç









