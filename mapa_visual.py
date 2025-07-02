# mapa_visual.py

import random
from battle import Battle
from entities import jogador
from stage_mobs import inimigos_da_fase

# Cores ANSI
class Cores:
    RESET = "\033[0m"
    VERMELHO = "\033[91m"
    VERDE = "\033[92m"
    AMARELO = "\033[93m"
    ROXO = "\033[95m"
    CIANO = "\033[96m"
    CINZA = "\033[90m"

def colorir(simbolo):
    cores = {
        '#': Cores.CINZA,
        '@': Cores.VERDE,
        'S': Cores.CIANO,
        'E': Cores.VERMELHO,
        'T': Cores.AMARELO,
        'C': Cores.ROXO,
        '.': Cores.RESET
    }
    return cores.get(simbolo, Cores.RESET) + simbolo + Cores.RESET

def gerar_mapa_visual(sala, largura=10, altura=10):
    grade = [['#' for _ in range(largura)] for _ in range(altura)]

    # Gera caminho até a saída
    x, y = 0, 0
    caminho = [(x, y)]
    grade[y][x] = '.'
    while (x, y) != (largura - 1, altura - 1):
        direcoes = []
        if x < largura - 1:
            direcoes.append((x + 1, y))
        if y < altura - 1:
            direcoes.append((x, y + 1))
        x, y = random.choice(direcoes)
        grade[y][x] = '.'
        caminho.append((x, y))
    saida = (x, y)
    grade[saida[1]][saida[0]] = 'S'
    grade[0][0] = '@'

    # Coloca inimigos/tesouros/armadilhas
    def colocar_em(codigo, quantidade):
        colocados = 0
        tentativas = 0
        while colocados < quantidade and tentativas < 100:
            x = random.randint(0, largura - 1)
            y = random.randint(0, altura - 1)
            if grade[y][x] == '.' and (x, y) != (0, 0) and (x, y) != saida:
                grade[y][x] = codigo
                colocados += 1
            tentativas += 1

    if not sala.get("segura", False):
        colocar_em('E', len(sala.get("inimigos", [])))
    colocar_em('C', random.randint(1, 2))
    colocar_em('T', random.randint(1, 2))

    return grade, saida

def exibir_mapa(grade):
    for linha in grade:
        print(' '.join([colorir(simbolo) for simbolo in linha]))

def jogar_com_mapa(sala, inimigos):
    grade, saida = gerar_mapa_visual(sala)
    jogador_x, jogador_y = 0, 0

    while True:
        exibir_mapa(grade)
        print(f"\nPosição atual: ({jogador_x}, {jogador_y})")

        direcao = input("Movimentar (cima, baixo, esquerda, direita): ").lower()
        try:
            passos = int(input("Quantos passos? "))
        except ValueError:
            print("Valor inválido.")
            continue

        dx, dy = 0, 0
        if direcao == 'cima':
            dy = -1
        elif direcao == 'baixo':
            dy = 1
        elif direcao == 'esquerda':
            dx = -1
        elif direcao == 'direita':
            dx = 1
        else:
            print("Direção inválida.")
            continue

        for _ in range(passos):
            novo_x = jogador_x + dx
            novo_y = jogador_y + dy
            if 0 <= novo_x < len(grade[0]) and 0 <= novo_y < len(grade):
                if grade[novo_y][novo_x] != '#':
                    simbolo = grade[novo_y][novo_x]
                    grade[jogador_y][jogador_x] = '.'
                    jogador_x, jogador_y = novo_x, novo_y

                    if simbolo == 'E':
                        print("⚔️ Você encontrou um inimigo!")
                        Battle(inimigos)
                        if not jogador.alive():
                            return False
                    elif simbolo == 'T':
                        print("💥 Você caiu em uma armadilha!")
                        jogador.hp -= 5
                        print(f"HP atual: {jogador.hp}/{jogador.hp_max}")
                        if jogador.hp <= 0:
                            print("Você morreu!")
                            return False
                    elif simbolo == 'C':
                        print("💰 Você encontrou um tesouro!")
                        jogador.gold += random.randint(5, 15)
                        print(f"Ouro atual: {jogador.gold}")
                    elif simbolo == 'S':
                        print("🚪 Você chegou à saída!")
                        return True

                    grade[jogador_y][jogador_x] = '@'
                else:
                    print("🚧 Bateu numa parede!")
                    break
            else:
                print("❌ Fora do mapa!")
                break
