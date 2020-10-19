import numpy
import os
from DFS import DFS_finder
from BFS import BFS_finder
from Best_first import Best_first_finder
from A_star import A_star_finder
from Hill_climbing import Hill_climbing_finder
from Map_generator import Map_generator
import matplotlib
matplotlib.use('TkAgg')

def map_gen():
    data = Map_generator().make_map()

    print('Mapa gerado:')
    for l in data[3]:
        for c in l:
            print(c, end='')
        print()

    return data[0], data[3]

def input_map():
    error = True
    while error:
        error = False
        shape = input()
        shape = shape.split()
        if len(shape) != 2:
            print("Entre exatamente 2 numeros para o foramto do mapa")
            error = True
        else:
            try:
                shape = list(map(int, shape))
            except:
                print("Entre valores numericos para o formato")
                error = True
    
    char_map = [[''] * shape[1] for _ in range(shape[0])]
    # char_map = [['' for __ in range(shape[1])] for _ in range(shape[0])]

    for i in range(shape[0]):
        line = input()

        for j, c in enumerate(line):
            char_map[i][j] = c

    return char_map
    
def print_maps(path):
    dir_path = f'Inputs/{path}'
    files = os.listdir(dir_path)

    for i, f in enumerate(files):
        map_file = open(f'{dir_path}/{f}')
        N = int(map_file.readline().split()[0])

        print(f'{i + 1}.', end='')
        for _ in range(N):
            line = map_file.readline()
            print(f'\t{line}', end='')
        
        print()

        map_file.close()


    return files

def get_map_and_run(plot, heuristic):
    sizes = ['', 'small', 'medium', 'large']

    print('Selecione um tamanho de labirinto:')
    print('1. 10x10')
    print('2. 30x30')
    print('3. 50x50')
    print('4. Mapa da Especificação')
    while True:
        try:
            size = int(input())
            if size < 1 or size > 4:
                raise ValueError()
            break
        except KeyboardInterrupt:
            return
        except:
            print("Entre um valor numerico entre 1 e 4 (incluso)")
            continue

    if size == 4:
        m_file = open('Inputs/input.txt')

        shape = m_file.readline() 
        shape = shape.split()
        shape = list(map(int, shape))
        char_map = [[''] * shape[1] for _ in range(shape[0])]

        for i in range(shape[0]):
            line = m_file.readline().split('\n')[0] 
            for j, c in enumerate(line):
                char_map[i][j] = c

        m_file.close()

        convert_map_and_run(char_map, plot, heuristic)

        return 

    all_maps = 0
    all_maps = print_maps(sizes[size])

    while True:
        try:
            selected = int(input())
            if selected < 1 or selected > len(all_maps):
                raise ValueError()
            break
        except KeyboardInterrupt:
            return
        except:
            print(f"Entre um valor numerico entre 1 e {len(all_maps)} (incluso)")
            continue

    m_path = all_maps[selected - 1]
    m_file = open(f'Inputs/{sizes[size]}/{m_path}')

    shape = m_file.readline() 
    shape = shape.split()
    shape = list(map(int, shape))
    char_map = [[''] * shape[1] for _ in range(shape[0])]

    for i in range(shape[0]):
        line = m_file.readline().split('\n')[0] 
        for j, c in enumerate(line):
            char_map[i][j] = c

    m_file.close()

    convert_map_and_run(char_map, plot, heuristic)
    
    

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

    while (opt != 0):
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

        print('5. Rodar com mapa de exemplo')
        
        if (seed != ''):
            print('6. Usar mapa gerado')

        print('0. Sair')

        opt = input()

        try:
            opt = int(opt)
            if opt > 6 or opt < 0:
                raise ValueError()
        except:
            print("Entre um numero valido entre 0 - 6")
            continue

        if opt == 1:
            seed, gen_map = map_gen()
        elif opt == 2:
            inp_map = input_map()
            convert_map_and_run(inp_map, plot, h)
        elif opt == 3:
            if h == 'e':
                h = 'm'
            elif h == 'm':
                h = 'e'
        elif opt == 4:
            plot = not plot
        elif opt == 5:
            get_map_and_run(plot, h)
        elif opt == 6:
            convert_map_and_run(gen_map, plot, h)




if __name__ == '__main__':
    main()