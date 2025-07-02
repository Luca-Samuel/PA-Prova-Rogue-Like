from mapa_visual import jogar_com_mapa
from room import *
from stage_mobs import inimigos_da_fase
from battle import Battle
from store import in_store
from stage import stage_counter
from entities import jogador
import json
import random
from random import seed

'''
Este main executa uma seleção aletoria de salas, progredindo em numero gradativamente
'''

seed()

with open("stage_pool.json", "r", encoding="utf-8") as file:
    stage_pool = json.load(file)

def escolher_tipo_sala(fase):
    if fase % 5 == 0:
        return "chefes"
    elif fase % 3 == 0:
        return "lojas"
    else:
        return "comuns"

if __name__ == "__main__":
    contador = stage_counter()

    for _ in range(10):
        fase = contador.current_stage()
        tipo_sala = escolher_tipo_sala(fase)

        print(f"\n=== FASE {fase}: TIPO {tipo_sala.upper()} ===")

        if tipo_sala == "lojas":
            in_store(jogador)
            contador.next_stage()
            continue

        sala_atual = carregar_sala_por_tipo(stage_pool, tipo_sala)

        if not sala_atual:
            print("Erro ao carregar a sala!")
            break

        print(f"\n[Descrição da Sala]: {sala_atual.get('descricao', 'Uma sala misteriosa...')}\n")

        if not sala_atual.get('segura', False):
            inimigos = inimigos_da_fase(sala_atual.get("inimigos", []))
            sucesso = jogar_com_mapa(sala_atual, inimigos)

            if jogador.alive():
                print("Você sobreviveu!")
            else:
                print("\nVocê foi derrotado... Fim de jogo.")
                break
        else:
            print("Você encontra um local seguro para descansar.")
            jogador.hp = min(jogador.hp + 20, jogador.hp_max)
            print(f"Você recuperou um pouco de energia. (HP: {jogador.hp}/{jogador.hp_max})")

        contador.next_stage()
