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

        elif nome == "cultista":
            resultado.append(Mob("Cultista", 28, 1, short_bow, 9, False))

        elif nome == "lodo":
            resultado.append(Mob("Lodo", 30, 0, claws, 5, False))

        elif nome == "sapo_vil":
            resultado.append(Mob("Sapo Vil", 22, 1, claws, 6, False))

        elif nome == "avatar_da_ruina":
            resultado.append(Mob("Avatar da Ruína", 120, 6, stone_hammer, 60, True))

        elif nome == "serpente_gelida":
            resultado.append(Mob("Serpente Gélida", 95, 4, short_bow, 45, True))

        elif nome == "centopeia_ossea":
            resultado.append(Mob("Centopeia Óssea", 110, 5, claws, 50, True))

        elif nome == "fenix_sombrio":
            resultado.append(Mob("Fênix Sombrio", 100, 3, short_bow, 55, True))

        elif nome == "titao_de_ferro":
            resultado.append(Mob("Titão de Ferro", 130, 7, stone_hammer, 70, True))

        else:
            print(f"[ERRO] Inimigo desconhecido: '{nome}'")

    return resultado