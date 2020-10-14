import numpy

class A_star_finder:
    

    def __init__(self):
        self.map = None
        self.cache_map = None


    def __init__(self, map):
        self.map = map
        self.cache_map = None


    def set_map(self, map):
        self.map = map


    def __find_path(self, start_point, end_point):

        prior_queue = []
        g_costs = {}
        parent_nodes = {}
        self.cache_map = self.map.copy()

        prior_queue.append(start_point)
        g_costs[(start_point)] = 0
        parent_nodes[(start_point)] = (-1, -1)
        self.cache_map[start_point[0], start_point[1]] = 0

        cur_pos = (-1, -1)
        found = False

        while prior_queue:

            # selects the node with smallest cost from the queue
            min_cost = 100000000
            for i, node in enumerate(prior_queue):
                cost = g_costs[node] + abs(end_point[0] - node[0]) + abs(end_point[1] - node[1])
                if(cost < min_cost):
                    min_cost = cost
                    cur_pos = prior_queue.pop(i)


            if(cur_pos == end_point):
                found = True
                break

            # print('hey')
            
            #Ordem de chamada: cima, esquerda, baixo, direita
            if(cur_pos[0]-1 >= 0 and self.cache_map[cur_pos[0]-1][cur_pos[1]] == 1):    # se existe e é viavel
                prior_queue.append((cur_pos[0]-1, cur_pos[1]))                                # add a proxima posição na fila
                self.cache_map[cur_pos[0]-1][cur_pos[1]] = 0                            # torna a proxima posição invalida
                parent_nodes[(cur_pos[0]-1, cur_pos[1])] = (cur_pos[0], cur_pos[1])     # registra a tupla no dict de pais
                g_costs[(cur_pos[0]-1, cur_pos[1])] = min_cost+1                        # registra a tupla no dict de custos
                # print('added: ' + str((cur_pos[0]-1, cur_pos[1])))                

            if(cur_pos[1]-1 >= 0 and self.cache_map[cur_pos[0]][cur_pos[1]-1] == 1):
                prior_queue.append((cur_pos[0], cur_pos[1]-1))                           
                self.cache_map[cur_pos[0]][cur_pos[1]-1] = 0
                parent_nodes[(cur_pos[0], cur_pos[1]-1)] = (cur_pos[0], cur_pos[1])
                g_costs[(cur_pos[0], cur_pos[1]-1)] = min_cost+1
                # print('added: ' + str((cur_pos[0], cur_pos[1]-1)))

            if(cur_pos[0]+1 < self.map.shape[0]):
                # print('pass 1')
                if(self.cache_map[cur_pos[0]+1][cur_pos[1]] == 1):
                    # print('pass 2')
                    prior_queue.append((cur_pos[0]+1, cur_pos[1]))                           
                    self.cache_map[cur_pos[0]+1][cur_pos[1]] = 0
                    parent_nodes[(cur_pos[0]+1, cur_pos[1])] = (cur_pos[0], cur_pos[1])
                    g_costs[(cur_pos[0]+1, cur_pos[1])] = min_cost+1
                    # print('added: ' + str((cur_pos[0]+1, cur_pos[1])))

            if(cur_pos[1]+1 < self.map.shape[1] and self.cache_map[cur_pos[0]][cur_pos[1]+1] == 1):
                prior_queue.append((cur_pos[0], cur_pos[1]+1))                           
                self.cache_map[cur_pos[0]][cur_pos[1]+1] = 0
                parent_nodes[(cur_pos[0], cur_pos[1]+1)] = (cur_pos[0], cur_pos[1])
                g_costs[(cur_pos[0], cur_pos[1]+1)] = min_cost+1
                # print('added: ' + str((cur_pos[0], cur_pos[1]+1)))

        
        if(not found):
            return False, None

        path = []
        
        while(cur_pos != (-1, -1)):
            
            path.insert(0, cur_pos)
            cur_pos = parent_nodes[cur_pos]

        return True, path


    def solve_map(self, start_point, end_point):

        return self.__find_path(start_point, end_point)
