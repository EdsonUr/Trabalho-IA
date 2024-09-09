from utils import estado_igual, gerar_sucessores, print_estado, print_caminho
from collections import deque
import time

estado_final = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5],
]

def busca_em_largura(estado_inicial):
    inicio = time.time()
    fronteira = deque([(estado_inicial, None, 0, [])])
    explorados = set()
    max_fronteira = 0

    while fronteira:
        estado_atual, movimento_anterior, nivel, caminho = fronteira.popleft()
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
            
        max_fronteira = max(max_fronteira, len(fronteira))
        
    
    fim = time.time()
    print(f"Tempo de execução: {fim - inicio:.4f} segundos")
    print(f"Tamanho máximo da fronteira: {max_fronteira}")
    return False

estado_inicial = [
    [8, 1, 3],
    [7, 2, 4],
    [6, 0, 5],
]

busca_em_largura(estado_inicial)