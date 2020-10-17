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

    return data[0]

def input_map():
    shape = input()
    shape = shape.split()
    shape[0] = int(shape[0])
    shape[1] = int(shape[1])

    map = numpy.zeros((shape[0], shape[1]))

    start_point = (0, 0)
    end_point = (0, 0)

    for i in range(shape[0]):
        try:
            line = input()
            for j, c in enumerate(line):
                if(c == '*'):
                    map[i, j] = 1
                if(c == '#'):
                    map[i, j] = 1
                    start_point = (i, j)
                if(c == '$'):
                    map[i, j] = 1
                    end_point = (i, j)
        except e:
            break


def main():
    opt = -1
    seed = ''
    while (opt != 0):
        print('Selecione uma das opções abaixo:')
        print()
        print('1. Gerar um mapa')
        print('2. Entrar com mapa')

        if (seed != ''):
            print('3. Usar mapa gerado')

        opt = input()

        if int(opt) == 1:
            seed = map_gen()
        elif int(opt) == 2:
            




    return


if __name__ == '__main__':
    main()