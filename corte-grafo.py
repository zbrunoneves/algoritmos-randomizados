# algoritmo randomizado Las Vegas que encontra (em tempo aleatorio) um corte de tamanho pelo menos m/2 em um
# grafo G com n vertices e m arestas

# os vertices do grafo sao comprimidos 2 a 2 ate que restem apenas dois vertices
# as arestas restantes representam o corte encontrado

from random import randint

# numero de execucoes do algoritmo
t = 1

while True:
    # aqui precisam ser definidas as arestas
    G = [('a', 'b'), ('b', 'd'), ('a', 'c'),  ('c', 'd'),  ('a', 'e'),  ('e', 'c'),  ('e', 'd'), ('a', 'f')]

    # inicializa cada vertice em sua propria particao unica
    particoes = {}
    for (x, y) in G:
        particoes[x] = x
        particoes[y] = y

    n = len(particoes)  # vertices
    m = len(G)          # arestas
    corte = int(m / 2)  # corte minimo desejado

    print(f'Tentativa #{t} de encontrar um corte de tamanho pelo menos', corte, '...')
    t += 1

    # comprimir todos os vertices em apenas 2
    for _ in range(n-2):
        # seleciona uma aresta aleatoriamente
        x, y = G[randint(0, len(G)-1)]

        # contrai todas as arestas de x para y e de y para x
        G = [aresta for aresta in G if (aresta != (x, y) and aresta != (y, x))]

        # agrupa as particoes de x e y
        particao_anterior_y = particoes[y]
        for k, v in particoes.items():
            if v == particao_anterior_y:
                particoes[k] = particoes[x]

        # atualiza arestas de G para novo vertice x+y
        for index, (a, b) in enumerate(G):
            aresta = list((a, b))
            if aresta[0] == y:
                aresta[0] = x
            if aresta[1] == y:
                aresta[1] = x
            G[index] = tuple(aresta)

    # arestas restantes = tamanho do corte
    if len(G) >= corte:
        print('Achei!')
        break

# estrutura o resultado na biparticao final (A, B)
biparticao = {}
for k, v in particoes.items():
    if v in biparticao:
        biparticao[v].append(k)
    else:
        biparticao[v] = [k]

print('Tamanho do Corte =', len(G))
print('Bipartição =', list(biparticao.values()))
