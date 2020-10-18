import sys
import numpy
from DFS import DFS_finder
from BFS import BFS_finder
from Best_first import Best_first_finder
from A_star import A_star_finder
from Hill_climbing import Hill_climbing_finder
from Map_generator import Map_generator


#GETTING INPUT---------------------------------------
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


# Map Generator

gen = Map_generator()
seed, start, end, map = gen.make_map(N=20, M=20, iterations=100000, min_length_of_hallways=5)

for line in map:
    for c in line:
        print(c, end='')
    print('')

# DFS-------------------------------------------------

# dsf = DFS_finder(map)
# res, path = dsf.solve_map(start_point, end_point, plot=True)
# 
# print(res)
# print(path)

# BFS-------------------------------------------------

# bsf = BFS_finder(map)
# res, path = bsf.solve_map(start_point, end_point, plot=True)
# 
# print(res)
# print(path)

# Best_first----------------------------------------------

# best_first = Best_first_finder(map)
# res, path = best_first.solve_map(start_point, end_point, plot=True)
# 
# print(res)
# print(path)

# A_star----------------------------------------------

# a_star = A_star_finder(map)
# res, path = a_star.solve_map(start_point, end_point, plot=True)
# print(res)
# print(path)

# Hill_Climbing----------------------------------------------

# hill_climbing = Hill_climbing_finder(map)
# res, path = hill_climbing.solve_map(start_point, end_point, plot=True)

# print(res)
# print(path)