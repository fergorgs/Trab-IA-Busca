import numpy
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


class DFS_finder:
    

    def __init__(self):
        self.map = None
        self.cache_map = None


    def __init__(self, map):
        self.map = map
        self.cache_map = None


    def set_map(self, map):
        self.map = map


    def __find_path(self, start_point, end_point, old_path):

        path = old_path.copy()
        path.append(start_point)

        if(start_point == end_point):
            return True, path

        self.cache_map[start_point[0]][start_point[1]] = 3

        if self.plot:
            bg = self.fig.canvas.copy_from_bbox(self.ax.bbox)
            
            self.img_data.set_data(self.cache_map)

            self.fig.canvas.restore_region(bg)
            self.ax.draw_artist(self.img_data)
            self.fig.canvas.blit(self.ax.bbox)

            self.fig.show()

            plt.pause(0.0001)

        #Ordem de chamada: cima, esquerda, baixo, direita
        if(start_point[0]-1 >= 0 and self.cache_map[start_point[0]-1][start_point[1]] == 1):
            res, final_path = self.__find_path((start_point[0]-1, start_point[1]), end_point, path)
            if(res):
                return True, final_path

        if(start_point[1]-1 >= 0 and self.cache_map[start_point[0]][start_point[1]-1] == 1):
            res, final_path = self.__find_path((start_point[0], start_point[1]-1), end_point, path)
            if(res):
                return True, final_path

        if(start_point[0]+1 < self.map.shape[0] and self.cache_map[start_point[0]+1][start_point[1]] == 1):
            res, final_path = self.__find_path((start_point[0]+1, start_point[1]), end_point, path)
            if(res):
                return True, final_path

        if(start_point[1]+1 < self.map.shape[1] and self.cache_map[start_point[0]][start_point[1]+1] == 1):
            res, final_path = self.__find_path((start_point[0], start_point[1]+1), end_point, path)
            if(res):
                return True, final_path

        return False, None



    def solve_map(self, start_point, end_point, plot=False):
        self.cache_map = self.map.copy()
        cmap = ListedColormap(['#000000', '#eeeeee', '#9999ee', '#4444ff', '#44ff44', '#ff4444'])
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot()

        self.cache_map[end_point] = 5
        self.img_data = self.ax.matshow(self.cache_map, cmap=cmap)
        self.fig.canvas.draw()

        self.cache_map[end_point] = 1

        self.plot = plot

        found, path = self.__find_path(start_point, end_point, [])

        if self.plot and found:
            self.cache_map[end_point] = 5

            for p in path:
                self.cache_map[p] = 4
                bg = self.fig.canvas.copy_from_bbox(self.ax.bbox)
                
                self.img_data.set_data(self.cache_map)

                self.fig.canvas.restore_region(bg)
                self.ax.draw_artist(self.img_data)
                self.fig.canvas.blit(self.ax.bbox)

                self.fig.show()

                plt.pause(0.0001)

        if (plot):
            plt.show()
        return found, path
