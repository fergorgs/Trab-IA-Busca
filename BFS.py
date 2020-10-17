import numpy
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


class BFS_finder:
    

    def __init__(self):
        self.map = None
        self.cache_map = None


    def __init__(self, map):
        self.map = map
        self.cache_map = None


    def set_map(self, map):
        self.map = map


    def __find_path(self, start_point, end_point, plot):   
        cmap = ListedColormap(['#000000', '#eeeeee', '#9999ee', '#4444ff', '#44ff44'])
        fig = plt.figure()
        ax = fig.add_subplot()

        queue = []
        hash_map = {}
        self.cache_map = self.map.copy()

        queue.append(start_point)
        self.cache_map[start_point[0], start_point[1]] = 0
        hash_map[(start_point)] = (-1, -1)

        cur_pos = (-1, -1)
        found = False

        while queue:

            cur_pos = queue.pop(0)

            if(cur_pos == end_point):
                found = True
                break
            
            #Ordem de chamada: cima, esquerda, baixo, direita
            if(cur_pos[0]-1 >= 0 and self.cache_map[cur_pos[0]-1][cur_pos[1]] == 1):    # se existe e é viavel
                queue.append((cur_pos[0]-1, cur_pos[1]))                                # add a proxima posição na fina
                self.cache_map[cur_pos[0]-1][cur_pos[1]] = 0                            # torna a proxima posição invalida
                hash_map[(cur_pos[0]-1, cur_pos[1])] = (cur_pos[0], cur_pos[1])         # add a tupla ao dict

            if(cur_pos[1]-1 >= 0 and self.cache_map[cur_pos[0]][cur_pos[1]-1] == 1):
                queue.append((cur_pos[0], cur_pos[1]-1))                           
                self.cache_map[cur_pos[0]][cur_pos[1]-1] = 0
                hash_map[(cur_pos[0], cur_pos[1]-1)] = (cur_pos[0], cur_pos[1]) 

            if(cur_pos[0]+1 < self.map.shape[0] and self.cache_map[cur_pos[0]+1][cur_pos[1]] == 1):
                queue.append((cur_pos[0]+1, cur_pos[1]))                           
                self.cache_map[cur_pos[0]+1][cur_pos[1]] = 0
                hash_map[(cur_pos[0]+1, cur_pos[1])] = (cur_pos[0], cur_pos[1])

            if(cur_pos[1]+1 < self.map.shape[1] and self.cache_map[cur_pos[0]][cur_pos[1]+1] == 1):
                queue.append((cur_pos[0], cur_pos[1]+1))                           
                self.cache_map[cur_pos[0]][cur_pos[1]+1] = 0
                hash_map[(cur_pos[0], cur_pos[1]+1)] = (cur_pos[0], cur_pos[1])
            
            if plot:
                ax.matshow(self.cache_map, cmap=cmap)
                fig.canvas.draw()

                fig.show()

                plt.pause(0.0001)

        if(not found):
            return False, None

        path = []
        
        while(cur_pos != (-1, -1)):
            
            path.insert(0, cur_pos)
            cur_pos = hash_map[cur_pos]            
        
        if plot:
            self.cache_map[end_point[0]][end_point[1]] = 4

            for p in path:
                self.cache_map[p[0]][p[1]] = 4
                ax.matshow(self.cache_map, cmap=cmap)
                fig.canvas.draw()

                fig.show()

                plt.pause(0.0001)
        
        return True, path


    def solve_map(self, start_point, end_point, plot=False):

        return self.__find_path(start_point, end_point, plot)
