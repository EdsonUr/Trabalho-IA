from utils import estado_igual, gerar_sucessores, print_estado, print_caminho
import time

estado_final = [
    [1, 2, 3],
    [5, 6, 4],
    [7, 8, 0]
]

def dfs_com_limite(estado_atual, limite, nivel, caminho, movimento_anterior, explorados, fronteira, max_fronteira):
    max_fronteira[0] = max(max_fronteira[0], len(fronteira))
    print(f"\nExplorando estado no nível {nivel}:")
    print_estado(estado_atual, nivel)

    if estado_igual(estado_atual, estado_final):
        return caminho + [(estado_atual, movimento_anterior)], True

    if nivel >= limite:
        return None, False

    explorados.add(tuple(map(tuple, estado_atual)))

    for sucessor, movimento in gerar_sucessores(estado_atual, movimento_anterior):
        if tuple(map(tuple, sucessor)) not in explorados:
            fronteira.append(sucessor)
            resultado, encontrado = dfs_com_limite(sucessor, limite, nivel + 1, caminho + [(estado_atual, movimento)], movimento, explorados, fronteira, max_fronteira)
            fronteira.pop()
            if encontrado:
                return resultado, True

    return None, False

def busca_em_profundidade_com_limite(estado_inicial, limite):
    inicio = time.time()
    explorados = set()
    fronteira = []
    max_fronteira = [0]
    
    print(f"Iniciando busca em profundidade com limite de {limite}")
    
    caminho, encontrado = dfs_com_limite(estado_inicial, limite, 0, [], None, explorados, fronteira, max_fronteira)

    if encontrado:
        fim = time.time()
        print("\nSolução encontrada!")
        print(f"Tempo de execução: {fim - inicio:.4f} segundos")
        print(f"Tamanho máximo da fronteira (memória): {max_fronteira[0]}")
        print_caminho(caminho)
        return True

    fim = time.time()
    print(f"Solução não encontrada dentro do limite de profundidade {limite}. Tempo de execução: {fim - inicio:.4f} segundos")
    return False

estado_inicial = [
    [1, 2, 3],
    [5, 0, 4],
    [7, 6, 8]
]

limite_profundidade = 2
busca_em_profundidade_com_limite(estado_inicial, limite_profundidade)