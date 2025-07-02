from entities import *

def player_turn(jogador: Player,inimigos:list[Mob]):
        print("\n--- Sua vez ---\n")
        print(f"HP: {jogador.hp}/{jogador.hp_max} | Poções: {jogador.potion} | Ouro: {jogador.gold}")
        print(f"Arma atual: {jogador.weapon.weapon_name} (Dano: {jogador.weapon.min_damage}-{jogador.weapon.max_damage})")
        print("[1] Atacar \n[2] Defender \n[3] Usar poção")

        escolha = input("ESCOLHA SUA AÇÃO: \n\t-->")

        match escolha: 
            case "1":
                jogador.attack(inimigos)

            case "2": 
                jogador.defend()

            case "3":
                jogador.heal()

            case _:
                print("Escolha inválida! Você perdeu o turno.\n")

