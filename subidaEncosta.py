from utils import estado_igual, gerar_sucessores, print_estado, print_caminho
import time

estado_final = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5],
]

def subida_pela_encosta(estado_inicial):
    inicio = time.time()
    estado_atual = estado_inicial
    caminho = [] 
    explorados = set() 
    heuristica_atual = calcula_heuristica(estado_atual)
    max_fronteira = 0 
    
    while True:
        print_estado(estado_atual, len(caminho))

        if estado_igual(estado_atual, estado_final):
            fim = time.time()
            print("Solução encontrada!")
            print(f"Tempo de execução: {fim - inicio:.4f} segundos")
            print_caminho(caminho) 
            print(f"Tamanho máximo da fronteira (estados explorados): {max_fronteira}")
            return True
        
        explorados.add(tuple(map(tuple, estado_atual)))

        max_fronteira = max(max_fronteira, len(explorados))
        sucessores = gerar_sucessores(estado_atual, None)

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

        if melhor_sucessor is None or menor_heuristica >= heuristica_atual:
            print("Máximo local encontrado, sem solução possível a partir daqui.")
            print(f"Tamanho máximo da fronteira (estados explorados): {max_fronteira}")
            return False

        estado_atual = melhor_sucessor
        heuristica_atual = menor_heuristica
        caminho.append((estado_atual, melhor_movimento))

def calcula_heuristica(estado):
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


estado_inicial = [
    [8, 1, 3],
    [7, 2, 4],
    [6, 0, 5],
]

print("Teste Subida pela Encosta com Análise de Tamanho Máximo da Fronteira (Estados Explorados)")
subida_pela_encosta(estado_inicial)
