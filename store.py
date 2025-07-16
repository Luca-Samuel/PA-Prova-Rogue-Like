from weapons import *
from entities import *
from random import randint, sample 

in_it = True
def in_store(jogador):
    
    print("===== BEM VINDO A LOJA =====\n")
    while(in_it):
        # Seleciona até 3 armas aleatórias da loja
        armas_disponiveis = sample(itens_store, min(3, len(itens_store)))
        for i, iten in enumerate(armas_disponiveis):
            print(f"[{i+1}]{iten.weapon_name} - Dano:{iten.min_damage}/{iten.max_damage} - Custo: 10 P.O")

        print("\n(aperte 0 para sair da loja) \n\n")

        try:
            escolha = int(input("QUAL ARMA VOCÊ DESEJA COMPRAR? \n\t ->"))-1

            if escolha == -1: 
                print("\nVocê saiu da loja")
                break
            
            new_weapon = armas_disponiveis[escolha]  # Corrigido aqui

            if jogador.gold >= 10: 
                jogador.gold -= 10
                
                print(f"{jogador.name} comprou {new_weapon.weapon_name}!")
                jogador.equip_weapon(new_weapon)
                print("\n")

            else:
                print("Você não tem ouro suficiente.")
                print("\n")


        except:
            print("Escolha inválida. Tente novamente.")


