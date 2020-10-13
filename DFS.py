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

        self.cache_map[start_point[0]][start_point[1]] = 0

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



    def solve_map(self, start_point, end_point):

        self.cache_map = self.map.copy()
        return self.__find_path(start_point, end_point, [])
