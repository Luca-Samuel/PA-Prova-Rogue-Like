from entities import Mob
from weapons import claws, stone_hammer, short_bow

def inimigos_da_fase(nomes: list) -> list:
    resultado = []

    for nome in nomes:
        nome = nome.lower() 

        if nome == "orc":
            resultado.append(Mob("Orc", 35, 2, stone_hammer, 10))

        elif nome == "goblin":
            resultado.append(Mob("Goblin", 25, 1, short_bow, 7))

        elif nome == "lobo":
            resultado.append(Mob("Lobo", 20, 1, claws, 5))

        elif nome == "esqueleto":
            resultado.append(Mob("Esqueleto", 22, 1, short_bow, 6))

        elif nome == "dragao":
            resultado.append(Mob("Dragão", 80, 4, stone_hammer, 30))

        elif nome == "sapo_vil":
            resultado.append(Mob("Sapo Vil", 18, 0, claws, 4))

        elif nome == "lodo":
            resultado.append(Mob("Lodo", 30, 0, claws, 5))

        elif nome == "rei_orc":
            resultado.append(Mob("Rei Orc", 60, 3, stone_hammer, 25))

        elif nome == "demônio_antigo":
            resultado.append(Mob("Demônio Antigo", 90, 5, stone_hammer, 40))

        elif nome == "avatar da ruína":
            resultado.append(Mob("Avatar da Ruína", 100, 6, claws, 50))

        else:
            print(f"[ERRO] Inimigo desconhecido: '{nome}'")

    return resultado