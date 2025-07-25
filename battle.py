from entities import *
from weapons import *
from action import * 
import os
import time
from random import sample, seed
from room import *
from stage_mobs import *
from almas import *
import json

# Carregar dados do arquivo JSON
try:
    with open("dados.json", "r") as f:
        dados = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    dados = {}

seed()
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def Battle(inimigos_da_fase):
    clear()
    print("=== BATALHA INICIADA ===")
    for mob in inimigos_da_fase:
        print(f"Você encontra {mob.name}!")
    time.sleep(1)

    while jogador.alive() and any(mob.alive() for mob in inimigos_da_fase): 
        player_turn(jogador, inimigos_da_fase)
        jogador.reset_defense()
        time.sleep(1.5)
        clear()

        for mob in inimigos_da_fase: 
            if mob.alive():
                print(f"Turno do(a) {mob.name}!\n")
                mob.action(jogador)
                time.sleep(1)
            
            elif not mob.ouro_dropado:
                print(f"{mob.name} foi derrotado!")
                mob.drop_gold(jogador)
                mob.ouro_dropado = True

                if mob.boss == True:
                    dados["almas"] = dados.get("almas", 0) + 1
                    print("Você absorveu uma Alma de Chefe!")
                    # Salvar dados atualizados
                    with open("dados.json", "w") as f:
                        json.dump(dados, f, indent=4)
                time.sleep(1)

        clear()

    print("Batalha terminou!")
    
    if jogador.alive():
        print(f"\n{jogador.name} venceu a batalha!")
    else:
        print(f"\n{jogador.name} foi derrotado...")

    time.sleep(2)
    clear()