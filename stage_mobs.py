from entities import Mob
from weapons import claws, stone_hammer, short_bow

def inimigos_da_fase(nomes: list) -> list:
    resultado = []

    for nome in nomes:
        nome = nome.lower() 

        if nome == "orc":
            resultado.append(Mob("Orc", 35, 2, stone_hammer, 10,False))

        elif nome == "goblin":
            resultado.append(Mob("Goblin", 25, 1, short_bow, 7,False))

        elif nome == "lobo":
            resultado.append(Mob("Lobo", 20, 1, claws, 5,False))

        elif nome == "esqueleto":
            resultado.append(Mob("Esqueleto", 22, 1, short_bow, 6,False))

        elif nome == "dragao":
            resultado.append(Mob("Dragão", 80, 4, stone_hammer, 30,False))

        elif nome == "sapo_vil":
            resultado.append(Mob("Sapo Vil", 18, 0, claws, 4,False))

        elif nome == "lodo":
            resultado.append(Mob("Lodo", 30, 0, claws, 5,False))

        elif nome == "rei_orc":
            resultado.append(Mob("Rei Orc", 60, 3, stone_hammer, 25,True))

        elif nome == "demônio_antigo":
            resultado.append(Mob("Demônio Antigo", 90, 5, stone_hammer, 40,True))

        elif nome == "avatar da ruína":
            resultado.append(Mob("Avatar da Ruína", 100, 6, claws, 50,True))

        else:
            print(f"[ERRO] Inimigo desconhecido: '{nome}'")

    return resultado