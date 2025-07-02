import random

def carregar_sala_por_tipo(stage_pool, tipo):
    salas_tipo = stage_pool["salas"].get(tipo, {})

    if not salas_tipo:
        print(f"Nenhuma sala do tipo '{tipo}' encontrada.")
        return None

    sala_id = str(random.randint(1, len(salas_tipo)))
    sala = salas_tipo[sala_id]

    return sala