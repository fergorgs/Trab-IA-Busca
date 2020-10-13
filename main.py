import sys
import numpy
from DFS import DFS_finder
from BFS import BFS_finder
from Map_generator import Map_generator


#GETTING INPUT---------------------------------------
# shape = input()
# shape = shape.split()
# shape[0] = int(shape[0])
# shape[1] = int(shape[1])

# map = numpy.zeros((shape[0], shape[1]))

# start_point = (0, 0)
# end_point = (0, 0)

# for i in range(shape[0]):
#     try:
#         line = input()
#         for j, c in enumerate(line):
#             if(c == '*'):
#                 map[i, j] = 1
#             if(c == '#'):
#                 map[i, j] = 1
#                 start_point = (i, j)
#             if(c == '$'):
#                 map[i, j] = 1
#                 end_point = (i, j)
#     except e:
#         break


# DFS-------------------------------------------------

# dsf = DFS_finder(map)
# res, path = dsf.solve_map(start_point, end_point)

# print(res)
# print(path)

# BFS-------------------------------------------------

# bsf = BFS_finder(map)
# res, path = bsf.solve_map(start_point, end_point)

# print(res)
# print(path)

genr = Map_generator()

s, e, m = genr.make_map()

# print(s)
# print(e)
# print(m)
