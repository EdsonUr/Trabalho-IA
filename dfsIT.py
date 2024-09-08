from utils import estado_igual, gerar_sucessores, print_estado, print_caminho
import time

estado_final = [
    [1, 2, 3],
    [5, 6, 4],
    [7, 8, 0]
]

def dfs_limitado(estado_atual, limite, nivel, caminho, movimento_anterior, explorados, fronteira, max_fronteira):
    max_fronteira[0] = max(max_fronteira[0], len(fronteira))
    print("fronteira:", fronteira)
    print("fronteira len:", len(fronteira))

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
            resultado, encontrado = dfs_limitado(sucessor, limite, nivel + 1, caminho + [(estado_atual, movimento)], movimento, explorados, fronteira, max_fronteira)
            fronteira.pop()
            if encontrado:
                return resultado, True

    return None, False

def busca_em_profundidade_iterativa(estado_inicial):
    limite = 2
    inicio = time.time()
    max_fronteira = [0]

    while True:
        explorados = set()
        fronteira = []
        print(f"\nIniciando busca com limite de profundidade: {limite}")

        caminho, encontrado = dfs_limitado(estado_inicial, limite, 0, [], None, explorados, fronteira, max_fronteira)

        if encontrado:
            fim = time.time()
            print("\nSolução encontrada!")
            print(f"Tempo de execução: {fim - inicio:.4f} segundos")
            print(f"Tamanho máximo da fronteira (memória): {max_fronteira[0]}")
            print_caminho(caminho)
            return True

        limite += 1

estado_inicial = [
    [1, 2, 3],
    [5, 0, 4],
    [7, 6, 8]
]

busca_em_profundidade_iterativa(estado_inicial)