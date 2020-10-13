import numpy as np
import random

class Map_generator:
    
    def make_map(self, M=None, N=None, iterations=None, min_length_of_hallways=None, start_point=None, end_point=None, seed=None):

        if(M == None):
            M = random.randrange(5, 50)
        if(N == None):
            N = random.randrange(5, 50)
        if(iterations == None):
            iterations = (M*N)*(M*N)
        if(min_length_of_hallways == None):
            min_length_of_hallways = random.randrange(1, 5)
        if(seed == None):
            seed = str(random.randrange(1000000, 9999999)) + str(random.randrange(1000000, 9999999)) + str(random.randrange(1000000, 9999999))
        
        map = np.zeros((N, M))

        cur_i = int(N/2)
        cur_j = int(M/2)

        move_dir = int(seed[0])*int(seed[1])
        move_dir %= 4
        steps = min_length_of_hallways

        for x in range(iterations):

            map[cur_i][cur_j] = 1

            if(steps == 0):
                move_dir = int(seed[x % len(seed)])*int(seed[(x+1) % len(seed)])
                move_dir %= 4
                steps = min_length_of_hallways

            # 0 = cima / 1 = esquerda / 2 = baixo / 3 = direita
            if(move_dir == 0):
                if(cur_i - 1 >= 0):
                    cur_i -= 1
            
            elif(move_dir == 1):
                if(cur_j - 1 >= 0):
                    cur_j -= 1
            
            elif(move_dir == 2):
                if(cur_i + 1 < N):
                    cur_i += 1
            
            else:
                if(cur_j + 1 < M):
                    cur_j += 1

            steps -= 1

        if(start_point == None):

            t = 0
            i = -1
            j = -1

            while(True):
                i = int(seed[t % len(seed)]) * int(seed[(t+1) % len(seed)]) * int(seed[(t+2) % len(seed)])
                j = int(seed[(t+3) % len(seed)]) * int(seed[(t+4) % len(seed)]) * int(seed[(t+5) % len(seed)])

                i %= N
                j %= M


                if(map[i][j] == 1):
                    start_point = (i, j)
                    break

                t += 1

        if(end_point == None):

            t = 0
            i = -1
            j = -1

            while(True):
                i = (int(seed[t % len(seed)]) + int(seed[(t+1) % len(seed)])) * int(seed[(t+2) % len(seed)])
                j = (int(seed[(t+3) % len(seed)]) + int(seed[(t+4) % len(seed)])) * int(seed[(t+5) % len(seed)])

                i %= N
                j %= M

                if(map[i][j] == 1):
                    end_point = (i, j)
                    break

                t += 1

        char_map = [[str(s) for s in sublist] for sublist in map]

        for i in range(N):
            for j in range(M):

                if(map[i][j] == 1):
                    char_map[i][j] = '*'
                else:
                    char_map[i][j] = '-'

        char_map[start_point[0]][start_point[1]] = '#'
        char_map[end_point[0]][end_point[1]] = '$'

        with open('input.txt', 'w') as f:
            f.write(str(start_point[0]) + ' ' + str(start_point[1]) + '\n')
            f.write(str(end_point[0]) + ' ' + str(end_point[1]) + '\n')

            for sublist in char_map:
                line = ''
                for c in sublist:
                    line += c
                f.write(line + '\n')


        return start_point, end_point, char_map




    