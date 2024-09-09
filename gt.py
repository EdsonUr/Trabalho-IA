import heapq
from utils import estado_igual, gerar_sucessores, print_estado, print_caminho
import time

# Estado final do quebra-cabeça de 15 peças
estado_final = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 0]
]

def busca_gulosa_com_fronteira(estado_inicial):
    inicio = time.time()
    
    # Inicializa a fronteira como uma fila de prioridade (min-heap)
    fronteira = []
    heapq.heappush(fronteira, (calcula_heuristica(estado_inicial), estado_inicial, None, []))
    
    explorados = set()  # Conjunto para armazenar os estados visitados
    max_fronteira = 0  # Para medir o tamanho máximo da fronteira

    while fronteira:
      
        # Pega o estado com a menor heurística da fronteira
        heuristica_atual, estado_atual, movimento_anterior, caminho = heapq.heappop(fronteira)

        print("\nExpansão do estado atual:")
        print_estado(estado_atual, len(caminho))

        # Verifica se o estado atual é o estado final
        if estado_igual(estado_atual, estado_final):
            fim = time.time()
            print("Solução encontrada!")
            print(f"Tempo de execução: {fim - inicio:.4f} segundos")
            
            # Imprime o caminho corretamente
            print_caminho(caminho)
            
            print(f"Tamanho máximo da fronteira: {max_fronteira}")
            return True

        # Marca o estado atual como visitado
        explorados.add(tuple(map(tuple, estado_atual)))

        # Gera os sucessores e adiciona os não explorados à fronteira
        sucessores = gerar_sucessores(estado_atual, movimento_anterior)
        for sucessor, movimento in sucessores:
            if tuple(map(tuple, sucessor)) not in explorados:
                nova_heuristica = calcula_heuristica(sucessor)
                # Apenas adiciona o movimento quando ele for válido
                novo_caminho = caminho + [(estado_atual, movimento)] if movimento is not None else caminho
                heapq.heappush(fronteira, (nova_heuristica, sucessor, movimento, novo_caminho))

        # Exibe a fronteira após expandir o estado atual e antes de atualizar o tamanho máximo
        print("\nFronteira atual:")
        print(f"Tamanho da fronteira: {len(fronteira)}")
        for f in fronteira:
            heuristica, estado, movimento, _ = f
            print(f"Heurística: {heuristica}, Movimento: {movimento}")
            print_estado(estado, len(_))

        # Atualiza o tamanho máximo da fronteira **depois** de adicionar sucessores
        max_fronteira = max(max_fronteira, len(fronteira))

    print("Não há solução possível")
    return False

def calcula_heuristica(estado):
    # Soma a heurística de Manhattan e o número de peças fora do lugar
    return heuristica_manhattan(estado) + heuristica_pecas_fora_do_lugar(estado)

def heuristica_manhattan(estado):
    distancia = 0
    for i in range(len(estado)):
        for j in range(len(estado[i])):
            valor = estado[i][j]
            if valor != 0:
                valor_i, valor_j = divmod(valor - 1, len(estado))
                distancia += abs(valor_i - i) + abs(valor_j - j)
    return distancia

def heuristica_pecas_fora_do_lugar(estado):
    fora_do_lugar = 0
    for i in range(len(estado)):
        for j in range(len(estado[i])):
            if estado[i][j] != 0 and estado[i][j] != estado_final[i][j]:
                fora_do_lugar += 1
    return fora_do_lugar

# Estado inicial de teste
estado_inicial = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 0, 10, 12],
    [13, 14, 11, 15]
]

print("Teste Busca Gulosa com Fronteira")
busca_gulosa_com_fronteira(estado_inicial)
