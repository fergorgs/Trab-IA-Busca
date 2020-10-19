import numpy
from DFS import DFS_finder
from BFS import BFS_finder
from Best_first import Best_first_finder
from A_star import A_star_finder
from Hill_climbing import Hill_climbing_finder
from Map_generator import Map_generator

def map_gen():
    data = Map_generator().make_map()

    print('Mapa gerado:')
    for l in data[3]:
        for c in l:
            print(c, end='')
        print()

    return data[0], data[3]

def input_map():
    shape = input()
    shape = shape.split()
    shape[0] = int(shape[0])
    shape[1] = int(shape[1])

    
    char_map = [['' for __ in range(shape[1])] for _ in range(shape[0])]

    for i in range(shape[0]):
        line = input()
        for j, c in enumerate(line):
            char_map[i][j] = c

    return char_map

def convert_map_and_run(char_map, plot, heuristic):
    N = len(char_map)
    M = len(char_map[0])
    map = numpy.zeros((N, M))

    start_point = (0, 0)
    end_point = (0, 0)

    for i in range(N):
        for j, c in enumerate(char_map[i]):
            if(c == '*'):
                map[i, j] = 1
            if(c == '#'):
                map[i, j] = 1
                start_point = (i, j)
            if(c == '$'):
                map[i, j] = 1
                end_point = (i, j)

    
    found, path, tempo = DFS_finder(map).solve_map(start_point, end_point, plot=plot)
    if (found):
        print('Caminho da DFS:')
        print(path)
        print('Tempo:')
        print(tempo)
    else:
        print('DFS não achou caminho')
    
    found, path, tempo = BFS_finder(map).solve_map(start_point, end_point, plot=plot)
    if (found):
        print('Caminho da BFS:')
        print(path)
        print('Tempo:')
        print(tempo)
    else:
        print('BFS não achou caminho')
    
    found, path, tempo = A_star_finder(map).solve_map(start_point, end_point, plot=plot, h=heuristic)
    if (found):
        print('Caminho da A*:')
        print(path)
        print('Tempo:')
        print(tempo)
    else:
        print('A* não achou caminho')
    
    found, path, tempo = Best_first_finder(map).solve_map(start_point, end_point, plot=plot, h=heuristic)
    if (found):
        print('Caminho da Best-First:')
        print(path)
        print('Tempo:')
        print(tempo)
    else:
        print('Best-First não achou caminho')
    
    found, path, tempo = Hill_climbing_finder(map).solve_map(start_point, end_point, plot=plot, h=heuristic)
    if (found):
        print('Caminho da Hill-Climbing:')
        print(path)
        print('Tempo:')
        print(tempo)
    else:
        print('Hill-Climbing não achou caminho')

def main():
    opt = -1
    seed = ''
    gen_map = []
    inp_map = []
    h = 'm'
    plot = True

    while (int(opt) != 0):
        print('Selecione uma das opções abaixo:')
        print()
        print('1. Gerar um mapa')
        print('2. Entrar com mapa e usá-lo')
        
        if h == 'm':
            print('3. Trocar Heuristica para distância Euclidiana')
        elif h == 'e':
            print('3. Trocar Heuristica para distância Manhattan')
        
        if plot:
            print('4. Não usar plotagem (está usando atualmente)')
        elif not plot:
            print('4. Usar plotagem (não está usando atualmente)')
        
        if (seed != ''):
            print('5. Usar mapa gerado')

        print('0. Sair')

        opt = input()

        if int(opt) == 1:
            seed, gen_map = map_gen()
        elif int(opt) == 2:
            inp_map = input_map()
            convert_map_and_run(inp_map, plot, h)
        elif int(opt) == 3:
            if h == 'e':
                h = 'm'
            elif h == 'm':
                h = 'e'
        elif int(opt) == 4:
            plot = not plot
        elif int(opt) == 5:
            convert_map_and_run(gen_map, plot, h)




if __name__ == '__main__':
    main()