from abc import ABC, abstractmethod
from random import randint 
from weapons import *

class Entity(ABC): 

    '''
    this class refers to any entity, player or foe, each and every one of them has the same paramenters
    except the player has acess to few more methods than foes, like looting, buying weapons, etc

    ====================================================================================================

    Essa classe refere-se a qualquer entidade, jogador ou inimigo, e todas elas tem os mesmos parametros
    exeto que o jogador tem acesso a mais metodos que seus inimigos, como lootiar, comprar armas, etc
    '''

    def __init__(self, name, hp, defense):
        self.name = name 
        self.hp = hp 
        self.hp_max = hp  
        self.defense = defense 
        self.weapon = fists

    def alive(self): 
        return self.hp > 0 
    
    '''
    this method verifies if the entity is still alive, if it is, it will keep fighting, if not
    it will show to the player that it died 

    ===============================================================================================

    Esse metodo verifica se a entidade ainda esta viva, se ela estiver, ela vai continyar lutando,
    se não, ela mostrará ao player que ela morreu
    '''

    def damage_taken(self,damage): 
        damage_total = max(0,damage - self.defense)
        self.hp -= damage_total 

        print(f"{self.name} recebeu {damage_total} de dano! \n\n (HP: {self.hp}/{self.hp_max})")
        return damage_total

    '''
    this method refers to the damage took of each and every entity. The damage is mesuared over the
    diference between the output and the defense of each entity, the final ammount is considered the
    damage to be removed from the HP of the entity

    ================================================================================================

    esse metodo se refere ao dano que cada entidade leva. O dano é medido pela diferença entre o dano
    maximo e a defesa de cada entidade, o que restou é debitado da vida (HP) da entidade
    '''

    @abstractmethod 

    def action(self):
        pass

    '''
    Abstrac method to get actions

    ================================================================================================

    Metodo abstrato para receber ações
    '''


class Player(Entity):
    
    '''
    This is a class that refers to the player

    =================================================================================================

    Essa classe se refere ao jogador
    '''
    
    def __init__(self, name:str, hp:int, defense:int, gold = 0, potion = 1) -> None:
        super().__init__(name, hp, defense)

        self.base_defense = defense
        self.weapon_default = self.weapon
        self.gold = gold
        self.potion = potion

    def equip_weapon(self,weapon):
        '''
        essa função faz com que o player equipe uma arma
        '''
        self.weapon = weapon 
        print(f"{self.name} equipou um(a) {self.weapon.weapon_name}") 

    def drop_weapon(self,weapon): 
        '''
        essa função faz com que o player solte uma arma
        '''
        print(f'{self.name} largou um(a) {self.weapon.weapon_name}!')
        self.weapon_default = weapon

    def gold_get(self,gold): 
        self.gold += gold 

    def attack(self,inimigos:list):
        vivos = [mob for mob in inimigos if mob.alive()]
        if not vivos:
            print("Nenhum inimigo restante!")
            return

        print("\nINIMIGOS RESTANTES: ")
        for i, mob in enumerate(vivos):
            print(f"[{i+1}] {mob.name} (HP: {mob.hp}/{mob.hp_max})") 
        
        try: 
            
            alvo_index = int(input("Digite o numero do inimigo a ser atacado: ")) - 1
            alvo = vivos[alvo_index]

        except: 
            print("Escolha inválida! Você perde o turno.")
            return      
        
        dano = self.weapon.damage
        print(f"{self.name} ataca {alvo.name} com {self.weapon.weapon_name}")
        alvo.damage_taken(dano)

    def defend(self):
        self.defense = max(self.defense + 10, 20)
        print(f"você se defendeu do proximo ataque! (sua defesa atual é: {self.defense})")        
        return
    
    def reset_defense(self):  
        self.defense = self.base_defense

    def heal(self):
        if self.potion > 0:             
            cura = 10
            self.hp = min(self.hp + cura,self.hp_max)
            self.potion -= 1
            print(f"Você toma uma poção, {self.name} se curou em {cura} (HP:{self.hp}/{self.hp_max})")

        else: 
            print("Você não tem mais poções!")

    def action(self):
        raise NotImplementedError

jogador = Player("HERO", hp=100, defense=2)
jogador.equip_weapon(iron_sword)



class Mob(Entity): 

    '''
    this class refers to the mobs/foes 

    =============================================================================================

    Essa classe se refere aos monstos
    '''
    def __init__(self, name:str, hp:int, defense:int, weapon, gold_drop: int, boss: bool) -> None:
        super().__init__(name, hp, defense)

        self.boss = boss
        self.ouro_dropado = False
        self.min_gold_drop = max(gold_drop - 10, 0)
        self.max_gold_drop = gold_drop + 10 
        self.weapon = weapon

    def action(self, jogador):
        if not self.alive():
            return
        dano = self.weapon.damage
        print(f"{self.name} ataca com {self.weapon.weapon_name}")
        jogador.damage_taken(dano)


    def drop_gold(self,jogador):
        valor = randint(self.min_gold_drop, self.max_gold_drop)
        print(f"{self.name} derrubou {valor} de ouro!")
        gold_earned = valor
        jogador.gold_get(gold_earned)
        return valor
    
'''
after creating the list of enemies it is filled by itself soon after in other archive
'''
