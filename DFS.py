import numpy


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

        self.cache_map[start_point[0]][start_point[1]] = 2

        if self.plot:
            self.ax.matshow(self.cache_map)
            self.fig.canvas.draw()

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
        self.fig = plt.figure()
        self.ax = fig.add_subplot()
        self.plot = plot
        path = self.__find_path(start_point, end_point, [])
        if self.plot:
            self.cache_map[end_point[0]][end_point[1]] = 4

            for self.p in path:
                self.cache_map[p[0]][p[1]] = 4
                self.ax.matshow(self.cache_map)
                self.fig.canvas.draw()

                self.fig.show()

                plt.pause(0.0001)
        return path
