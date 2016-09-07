from Hero import Hero
from Skill import Skill
from Attack import Attack
import pprint

jinx_q = Skill("makinali", 30, 3, "AD")
jinx_w = Skill("cızt", 40, 5, "AD")
jinx_e = Skill("patlangaç", 20, 2, "AP")
jinx_r = Skill("Manyak Güçlü Ölüm Roketi", 120, 6, "AD")
thresh_q = Skill("KANÇA", 20, 3, "AP")
thresh_w = Skill("FENER", 5, 1, "AD")
thresh_e = Skill("DERİSİNİ YÜZ", 35, 2, "AD")
thresh_r = Skill("HÜCRE", 100, 6, "AP")

karakterler = {
    "Jinx" : {"skill_q" : jinx_q,
              "skill_w" : jinx_w,
              "skill_e" : jinx_e,
              "ulti"    : jinx_r,
              "base_armor" : 30,
              "base_hp" : 583,
              "base_mr" : 20,
              "is_ad" : True,
              "name" : "Jinx"},
    "Thresh" : {"skill_q" : thresh_q,
                "skill_w" : thresh_w,
                "skill_e" : thresh_e,
                "ulti"    : thresh_r,
                "base_armor": 50,
                "base_hp": 650,
                "base_mr": 40,
                "is_ad": False,
                "name" : "Thresh"}
}


while True:
    pprint.pprint(karakterler)
    oyuncu1 = input("\noynamak istediğiniz karakteri seçiniz")
    hero = karakterler.get(oyuncu1, None)
    if not hero:
        print("yok böyle bişey")
        break

    player = Hero(hero["name"],skill_q=hero["skill_q"],skill_w=hero["skill_w"],skill_e=hero["skill_e"],
                  ulti=hero["ulti"],base_armor=hero["base_armor"],base_mr=hero["base_mr"],base_hp=hero["base_hp"],
                  is_ad=hero["is_ad"])


    if oyuncu1 == "Jinx":
        bot = karakterler.get("Thresh")
    else:
        bot = karakterler.get("Jinx")

    player2 = Hero(bot["name"], skill_q=bot["skill_q"], skill_w=bot["skill_w"], skill_e=bot["skill_e"],
                  ulti=bot["ulti"], base_armor=bot["base_armor"], base_mr=bot["base_mr"], base_hp=bot["base_hp"],
                  is_ad=bot["is_ad"])

    while range(0,10):
        print("""
                Rakiple Karşılaştınız!!!
                Saldırmak için : 1
                Çıkmak için : quit
                """)
        komut = input("\nseçiminizi yapın : ")
        if komut == "1":
            player.mevcut_durumu_görüntüle()
            yetenek = input("Yeteneği seçiniz (Q-W-E-R) : ")
            if yetenek == "Q":
                skill = player.skill_q
            elif yetenek == "W":
                skill = player.skill_w
            elif yetenek == "E":
                skill = player.skill_e
            elif yetenek == "R":
                skill = player.ulti
            else:
                skill = player.skill_q

            attack = Attack(player,player2,skill)
            attack.attack()
            öldü_mü = player2.öldümü()
            if öldü_mü:
                print("kazandınız")
                break





