from utils import estado_igual, gerar_sucessores, print_estado, print_caminho
import time

# Estado final do quebra-cabeça de 15 peças
estado_final = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 0]
]

def subida_pela_encosta(estado_inicial):
    inicio = time.time()
    estado_atual = estado_inicial
    caminho = []  # Lista para armazenar os estados percorridos
    explorados = set()  # Conjunto para armazenar estados já visitados
    heuristica_atual = calcula_heuristica(estado_atual)  # Calcula a heurística inicial
    max_fronteira = 0  # Para medir o tamanho máximo da fronteira (estados explorados)
    
    while True:
        print_estado(estado_atual, len(caminho))

        # Verifica se o estado atual é o estado final
        if estado_igual(estado_atual, estado_final):
            fim = time.time()
            print("Solução encontrada!")
            print(f"Tempo de execução: {fim - inicio:.4f} segundos")
            print_caminho(caminho)  # Caminho correto
            print(f"Tamanho máximo da fronteira (estados explorados): {max_fronteira}")
            return True

        # Marca o estado atual como visitado
        explorados.add(tuple(map(tuple, estado_atual)))

        # Atualiza o tamanho máximo da fronteira
        max_fronteira = max(max_fronteira, len(explorados))

        sucessores = gerar_sucessores(estado_atual, None)  # Gera os sucessores

        # Encontra o sucessor com a menor heurística
        melhor_sucessor = None
        menor_heuristica = heuristica_atual
        melhor_movimento = None

        for sucessor, movimento in sucessores:
            if tuple(map(tuple, sucessor)) not in explorados:
                heuristica_sucessor = calcula_heuristica(sucessor)
                if heuristica_sucessor < menor_heuristica:
                    menor_heuristica = heuristica_sucessor
                    melhor_sucessor = sucessor
                    melhor_movimento = movimento

        # Se não houver sucessor com heurística menor, parar (chegou ao máximo local)
        if melhor_sucessor is None or menor_heuristica >= heuristica_atual:
            print("Máximo local encontrado, sem solução possível a partir daqui.")
            print(f"Tamanho máximo da fronteira (estados explorados): {max_fronteira}")
            return False

        # Atualiza o estado atual para o melhor sucessor
        estado_atual = melhor_sucessor
        heuristica_atual = menor_heuristica
        caminho.append((estado_atual, melhor_movimento))

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
            if estado[i][j] != 0 and estado[i][j] != estado_final[i][j]:  # Corrigido
                fora_do_lugar += 1
    return fora_do_lugar


# Estado inicial de teste
estado_inicial = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 0, 10, 12],
    [13, 14, 11, 15]
]

print("Teste Subida pela Encosta com Análise de Tamanho Máximo da Fronteira (Estados Explorados)")
subida_pela_encosta(estado_inicial)
