from random import randint 

class Weapon(): 
    def __init__(self,name:str,damage:int,aoe:bool) -> None:

        self.aoe = aoe
        self.weapon_name = name
        self.min_damage = max(damage-2 ,1)
        self.max_damage = damage 

    @property
    def damage(self) -> int:
        return randint(self.min_damage, self.max_damage)
    
# Criação das armas
fists = Weapon(name="punhos", damage=2,aoe=False)
claws = Weapon(name="garras", damage=3, aoe=False)
dagger = Weapon(name="adaga", damage=8, aoe=False)
iron_sword = Weapon(name="espada de ferro", damage=15, aoe=False)
short_sword = Weapon(name="espada curta", damage=12, aoe=False)
stone_hammer = Weapon(name="clava de pedra", damage=15, aoe=False)
rapier = Weapon(name="florete", damage=14, aoe=False)
battle_axe = Weapon(name="machado de batalha", damage=18, aoe=False)
mace = Weapon(name="maça", damage=16, aoe=False)
scythe = Weapon(name="foice", damage=20, aoe=False)
warhammer = Weapon(name="martelo de guerra", damage=22, aoe=False)
katana = Weapon(name="katana", damage=25, aoe=False)
greatsword = Weapon(name="espada grande", damage=28, aoe=False)
morning_star = Weapon(name="estrela da manhã", damage=19, aoe=False)
halberd = Weapon(name="alabarda", damage=24, aoe=False)
spear = Weapon(name="lança", damage=17, aoe=False)
trident = Weapon(name="tridente", damage=21, aoe=False)
bone_crusher = Weapon(name="esmagador de ossos", damage=26, aoe=False)
poisoned_blade = Weapon(name="lâmina envenenada", damage=15, aoe=False) 
vampiric_dagger = Weapon(name="adaga vampírica", damage=18, aoe=False)  
short_bow = Weapon(name="arco curto", damage=10, aoe=False)
longbow = Weapon(name="arco longo", damage=16, aoe=False)
crossbow = Weapon(name="besta", damage=20, aoe=False)
sling = Weapon(name="funda", damage=6, aoe=False)
throwing_knives = Weapon(name="facas de arremesso", damage=8, aoe=False)
javelin = Weapon(name="dardo", damage=14, aoe=False)
boomerang = Weapon(name="bumerangue", damage=12, aoe=False)
blowgun = Weapon(name="zarabatana", damage=5, aoe=False)  
hand_cannon = Weapon(name="canhão de mão", damage=25, aoe=False)
arcane_orb = Weapon(name="orbe arcano", damage=30, aoe=False)  
whip = Weapon(name="chicote", damage=9, aoe=False)
chain_sickle = Weapon(name="foice de corrente", damage=22, aoe=False)
explosive_flask = Weapon(name="frasco explosivo", damage=35,aoe=False)  # área de efeito
cursed_blade = Weapon(name="lâmina amaldiçoada", damage=40,aoe=False)  # com algum efeito negativo

# Lista com todas as armas
weapon = [
    fists, dagger, iron_sword, short_sword, stone_hammer, rapier, battle_axe, mace, scythe,
    warhammer, katana, greatsword, morning_star, halberd, spear, trident, bone_crusher, poisoned_blade,
    vampiric_dagger, short_bow, longbow, crossbow, sling, throwing_knives, javelin, boomerang, blowgun,
    hand_cannon, arcane_orb, whip, chain_sickle, explosive_flask, cursed_blade
]

# Dicionário para busca rápida por nome
armas_dict = {w.weapon_name: w for w in weapon}

itens_store = weapon
