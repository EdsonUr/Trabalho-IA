from collections import deque
import time

estado_final = [
    [1, 2, 3],
    [5, 6, 4],
    [7, 8, 0]
]

def estado_igual(estado1, estado2):
    return estado1 == estado2

def encontrar_zero(estado):
    for i in range(len(estado)):
        for j in range(len(estado[i])):
            if estado[i][j] == 0:
                return i, j

def gerar_sucessores(estado, ultimo_movimento):
    sucessores = []
    i, j = encontrar_zero(estado)
    
    movimentos = [
        (-1, 0, 'cima', 'baixo'),    # Movendo para cima, oposto é baixo
        (1, 0, 'baixo', 'cima'),     # Movendo para baixo, oposto é cima
        (0, -1, 'esquerda', 'direita'), # Movendo para esquerda, oposto é direita
        (0, 1, 'direita', 'esquerda')  # Movendo para direita, oposto é esquerda
    ]
    
    for mov in movimentos:
        novo_i, novo_j = i + mov[0], j + mov[1]
        
        if 0 <= novo_i < 3 and 0 <= novo_j < 3 and mov[3] != ultimo_movimento:
            novo_estado = [linha[:] for linha in estado]
            novo_estado[i][j], novo_estado[novo_i][novo_j] = novo_estado[novo_i][novo_j], novo_estado[i][j]
            sucessores.append((novo_estado, mov[2]))
    
    return sucessores

def print_estado(estado, nivel):
    print(f"\nNível {nivel}:")
    for linha in estado:
        print(linha)

def print_caminho(caminho):
    print("\nCaminho até a solução:")
    for passo, (estado, movimento) in enumerate(caminho):
        print(f"\nPasso {passo + 1} - Movimento: {movimento}")
        for linha in estado:
            print(linha)

def busca_em_largura(estado_inicial):
    inicio = time.time()
    fronteira = deque([(estado_inicial, None, 0, [])])
    explorados = set()
    max_fronteira = 0

    while fronteira:
        estado_atual, movimento_anterior, nivel, caminho = fronteira.popleft()
        max_fronteira = max(max_fronteira, len(fronteira))
        caminho_atualizado = caminho + [(estado_atual, movimento_anterior)]
        print_estado(estado_atual, nivel)

        if estado_igual(estado_atual, estado_final):
            fim = time.time()
            print("Solução encontrada!")
            print(f"Tempo de execução: {fim - inicio:.4f} segundos")
            
            print_caminho(caminho_atualizado)
            
            print(f"Tamanho máximo da fronteira: {max_fronteira}")
            return True
        
        explorados.add(tuple(map(tuple, estado_atual)))
        
        for sucessor, movimento in gerar_sucessores(estado_atual, movimento_anterior):
            if tuple(map(tuple, sucessor)) not in explorados:
                fronteira.append((sucessor, movimento, nivel + 1, caminho_atualizado))
    
    fim = time.time()
    print(f"Tempo de execução: {fim - inicio:.4f} segundos")
    print(f"Tamanho máximo da fronteira: {max_fronteira}")
    return False


def dfs_limitado(estado_atual, limite, nivel, caminho, movimento_anterior, explorados, fronteira, max_fronteira):
    print(f"\nExplorando estado no nível {nivel}:")
    print_estado(estado_atual, nivel)

    # Atualiza o tamanho máximo da fronteira (pilha recursiva)
    max_fronteira[0] = max(max_fronteira[0], len(fronteira))

    if estado_igual(estado_atual, estado_final):
        return caminho + [(estado_atual, movimento_anterior)], True

    if nivel >= limite:
        return None, False

    explorados.add(tuple(map(tuple, estado_atual)))

    for sucessor, movimento in gerar_sucessores(estado_atual, movimento_anterior):
        if tuple(map(tuple, sucessor)) not in explorados:
            fronteira.append(sucessor)  # Simulando a pilha de estados
            resultado, encontrado = dfs_limitado(sucessor, limite, nivel + 1, caminho + [(estado_atual, movimento)], movimento, explorados, fronteira, max_fronteira)
            fronteira.pop()  # Remover o estado depois da chamada recursiva
            if encontrado:
                return resultado, True

    return None, False

def busca_em_profundidade_iterativa(estado_inicial):
    limite = 0
    inicio = time.time()
    max_fronteira = [0]  # Usamos uma lista para que seja mutável dentro da recursão

    while True:
        explorados = set()
        fronteira = []  # Simulando a pilha de estados
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

# Executando a busca em profundidade iterativa
estado_inicial = [
    [1, 2, 3],
    [5, 0, 4],
    [7, 6, 8]
]

busca_em_profundidade_iterativa(estado_inicial)
