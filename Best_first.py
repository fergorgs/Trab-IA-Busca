import numpy
from heapq import heappush, heappop
import matplotlib.pyplot as plt

directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]

class Best_first_finder:
    

    def __init__(self):
        self.map = None
        self.cache_map = None


    def __init__(self, map):
        self.map = map
        self.cache_map = None


    def set_map(self, map):
        self.map = map


    def __find_path(self, start_point, end_point, plot):

        fig = plt.figure()
        ax = fig.add_subplot()

        prior_queue = []
        parent_nodes = {}
        self.cache_map = self.map.copy()
        heappush(prior_queue, [0, start_point, (-1, -1)])
        found = False

        while prior_queue:

            cur_state = heappop(prior_queue)

            [cost, cur_pos, parent_pos] = cur_state

            if self.cache_map[cur_pos] == 3:
                continue

            self.cache_map[cur_pos] = 3
            parent_nodes[cur_pos] = parent_pos

            if cur_pos == end_point:
                found = True
                break
            
            #Ordem de chamada: cima, esquerda, baixo, direita
            for d in directions:
                next_pos = (cur_pos[0] + d[0], cur_pos[1] + d[1])

                if next_pos[0] < 0 or next_pos[1] < 0 or next_pos[0] >= self.map.shape[0] or next_pos[1] >= self.map.shape[1] or not self.cache_map[next_pos] or self.cache_map[next_pos] == 3:
                    continue
                
                next_cost = abs(end_point[0] - next_pos[0]) + abs(end_point[1] - next_pos[1])
                heappush(prior_queue, [next_cost, next_pos, cur_pos])
                self.cache_map[next_pos] = 2
            
                if plot:
                    ax.matshow(self.cache_map)
                    fig.canvas.draw()

                    fig.show()

                    plt.pause(0.0001)

        
        if(not found):
            return False, None

        path = []
        
        while(cur_pos != (-1, -1)):
            
            path.insert(0, cur_pos)
            cur_pos = parent_nodes[cur_pos]

        if plot:
            self.cache_map[end_point[0]][end_point[1]] = 4

            for p in path:
                self.cache_map[p[0]][p[1]] = 4
                ax.matshow(self.cache_map)
                fig.canvas.draw()

                fig.show()

                plt.pause(0.0001)

        return True, path


    def solve_map(self, start_point, end_point, plot=False):

        return self.__find_path(start_point, end_point, plot)
