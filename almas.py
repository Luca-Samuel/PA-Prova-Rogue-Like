def mostrar_altar_almas(dados):
    
    poderes = {
        "1": {"nome": "Força do Guerreiro", "custo": 3, "efeito": "Aumenta dano em 15%"},
        "2": {"nome": "Pele de Aço", "custo": 2, "efeito": "+2 de defesa permanente"},
        "3": {"nome": "Sede de Sangue", "custo": 4, "efeito": "Cura 10 '%' do dano causado"},
        "4": {"nome": "Bolso sem Fundo", "custo": 1, "efeito": "+5 de ouro no início"}
    }

    print("\n=== ALTAR DAS ALMAS ===")
    print(f"Almas disponíveis: {dados.get('almas', 0)}\n")
    
    for key, poder in poderes.items():
        status = "(COMPRADO)" if poder["nome"] in dados.get("poderes_ativos", []) else ""
        print(f"[{key}] {poder['nome']} - {poder['efeito']} {status}")

    escolha = input("\nEscolha um poder ou Enter para sair: ")

    if escolha in poderes:
        poder = poderes[escolha]
        if poder["nome"] in dados.get("poderes_ativos", []):
            print("Você já possui este poder!")
        elif dados["almas"] >= poder["custo"]:
            dados["almas"] -= poder["custo"]
            dados.setdefault("poderes_ativos", []).append(poder["nome"])
            from store import salvar_progresso
            salvar_progresso(dados)
            print(f"\n✅ {poder['nome']} adquirido!")
        else:
            print("Almas insuficientes!")
    elif escolha:
        print("Opção inválida!")

def aplicar_poderes(dados, jogador):
    """
    Aplica os efeitos dos poderes comprados
    """

    for poder in dados.get("poderes_ativos", []):
        if poder == "Força do Guerreiro":
            jogador.dano_mult = 1.15
        elif poder == "Pele de Aço":
            jogador.defense += 2
            jogador.base_defense += 2
        elif poder == "Bolso sem Fundo":
            jogador.gold += 5