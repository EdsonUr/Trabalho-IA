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