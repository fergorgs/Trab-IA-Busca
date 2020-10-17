import numpy
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

class Hill_climbing_finder:
    
    def __init__(self):
        self.map = None
        self.cache_map = None


    def __init__(self, map):
        self.map = map
        self.cache_map = None


    def set_map(self, map):
        self.map = map


    def __find_path(self, start_point, end_point, plot):
        cmap = ListedColormap(['#000000', '#eeeeee', '#9999ee', '#4444ff', '#44ff44', '#ff4444'])
        fig = plt.figure()
        ax = fig.add_subplot()

        self.cache_map = self.map.copy()

        self.cache_map[end_point] = 5
        img_data = ax.matshow(self.cache_map, cmap=cmap)
        fig.canvas.draw()

        self.cache_map[end_point] = 1
        
        path = []
        cur_pos = start_point
        cur_cost = abs(end_point[0] - cur_pos[0]) + abs(end_point[1] - cur_pos[1])

        while(cur_pos != None):

            path.append(cur_pos)

            if(cur_pos == end_point):
                if plot:
                    self.cache_map[end_point] = 5

                    for p in path:
                        self.cache_map[p] = 4

                        bg = fig.canvas.copy_from_bbox(ax.bbox)

                        img_data.set_data(self.cache_map)

                        fig.canvas.restore_region(bg)
                        ax.draw_artist(img_data)
                        fig.canvas.blit(ax.bbox)

                        fig.show()

                        plt.pause(0.0001)

                return True, path

            next_pos = None

            #Ordem de chamada: cima, esquerda, baixo, direita
            if(cur_pos[0]-1 >= 0 and self.cache_map[cur_pos[0]-1][cur_pos[1]] == 1):            # se existe e é viavel
                new_cost = abs(end_point[0] - (cur_pos[0]-1)) + abs(end_point[1] - cur_pos[1])  # calcula o novo custo
                if(new_cost <= cur_cost):                                                       # se é melhor ou igual ao atual
                    cur_cost = new_cost                                                         # atualiza o custo atual
                    next_pos = (cur_pos[0]-1, cur_pos[1])                                       # atualiza a posição atual
                    # self.cache_map[cur_pos[0]-1][cur_pos[1]] = 3                                # torna a posição invalida

            if(cur_pos[1]-1 >= 0 and self.cache_map[cur_pos[0]][cur_pos[1]-1] == 1):
                new_cost = abs(end_point[0] - cur_pos[0]) + abs(end_point[1] - (cur_pos[1]-1))
                if(new_cost <= cur_cost):
                    cur_cost = new_cost
                    next_pos = (cur_pos[0], cur_pos[1]-1)
                    # self.cache_map[cur_pos[0]][cur_pos[1]-1] = 3

            if(cur_pos[0]+1 < self.map.shape[0] and self.cache_map[cur_pos[0]+1][cur_pos[1]] == 1):
                new_cost = abs(end_point[0] - (cur_pos[0]+1)) + abs(end_point[1] - cur_pos[1])
                if(new_cost <= cur_cost):
                    cur_cost = new_cost
                    next_pos = (cur_pos[0]+1, cur_pos[1])
                    # self.cache_map[cur_pos[0]+1][cur_pos[1]] = 3

            if(cur_pos[1]+1 < self.map.shape[1] and self.cache_map[cur_pos[0]][cur_pos[1]+1] == 1):
                new_cost = abs(end_point[0] - cur_pos[0]) + abs(end_point[1] - (cur_pos[1]+1))
                if(new_cost <= cur_cost):
                    cur_cost = new_cost
                    next_pos = (cur_pos[0], cur_pos[1]+1)
                    # self.cache_map[cur_pos[0]][cur_pos[1]+1] = 3

            self.cache_map[next_pos] = 3

            if plot:
                bg = fig.canvas.copy_from_bbox(ax.bbox)

                img_data.set_data(self.cache_map)

                fig.canvas.restore_region(bg)
                ax.draw_artist(img_data)
                fig.canvas.blit(ax.bbox)

                fig.show()

                plt.pause(0.0001)
            
            cur_pos = next_pos


        return False, path


    def solve_map(self, start_point, end_point, plot=False):

        return self.__find_path(start_point, end_point, plot)
