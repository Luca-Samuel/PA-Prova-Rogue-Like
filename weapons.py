from random import randint 

class Weapon(): 
    def __init__(self,name:str,damage:int) -> None:

        self.weapon_name = name
        self.min_damage = max(damage-2 ,1)
        self.max_damage = damage 

    @property
    def damage(self) -> int:
        return randint(self.min_damage, self.max_damage)
    
weapon = []

fists = Weapon(name = "punhos", damage= 2)
iron_sword = Weapon(name = 'espada de ferro', damage = 100)
short_bow = Weapon(name = 'arco curto',damage = 3)
claws = Weapon(name ='garras' ,damage = 2)
stone_hammer = Weapon(name = 'clava de pedra' ,damage = 5)

itens_store = [iron_sword,short_bow,stone_hammer]
