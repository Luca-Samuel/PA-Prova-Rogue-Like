from weapons import *
from entities import *

in_it = True
def in_store(jogador):
    
    print("===== BEM VINDO A LOJA =====\n")
    while(in_it):
  
        for i, iten in enumerate(itens_store): 
            print(f"[{i+1}]{iten.weapon_name} - Dano:{iten.min_damage}/{iten.max_damage} - Custo: 10 P.O")

        print("\n(aperte 0 para sair da loja) \n\n")

        try:
            escolha = int(input("QUAL ARMA VOCÊ DESEJA COMPRAR? \n\t ->"))-1

            if escolha == -1: 
                print("\nVocê saiu da loja")
                break
            
            new_weapon = itens_store[escolha] 

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


    