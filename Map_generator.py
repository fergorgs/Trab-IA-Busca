import numpy as np
import random

class Map_generator:
    
    def make_map(self, M=None, N=None, iterations=None, min_length_of_hallways=None, start_point=None, end_point=None, seed=None, create_file=False):

        if(seed == None):
            seed = str(random.randrange(1000000, 9999999)) + str(random.randrange(1000000, 9999999)) + str(random.randrange(1000000, 9999999))
        if(M == None):
            M = 0
            for x in range(10):
                M += int(seed[x])
            M *= (45/210)
            M += 5
            M = int(M)
        if(N == None):
            N = 0
            for x in range(10):
                N += int(seed[x+5])
            N *= (45/210)
            N += 5
            N = int(N)
        if(iterations == None):
            iterations = (M*N)*(M*N)
        if(min_length_of_hallways == None):
            min_length_of_hallways = 0
            for x in range(10):
                min_length_of_hallways += int(seed[x+10])
            min_length_of_hallways *= (5/210)
            min_length_of_hallways += 1
            min_length_of_hallways = int(min_length_of_hallways)
        
        map = np.zeros((N, M))

        cur_i = int(N/2)
        cur_j = int(M/2)

        move_dir = int(seed[0])*int(seed[1])
        move_dir %= 4
        steps = min_length_of_hallways
        viable_positions = []

        # for x in range(iterations):
        x = 0
        y = 0
        coming_from_dir = (move_dir+2) % 4
        prevent_stuck = 0
        prev_pos = (cur_i, cur_j)
        while(x < iterations):
            
            if((cur_i, cur_j) == prev_pos):
                prevent_stuck += 1
                if(prevent_stuck == 4):
                    cur_i = int(N/2)
                    cur_j = int(M/2)
                    prevent_stuck = 0
            else:
                prevent_stuck = 0

            prev_pos = (cur_i, cur_j)
                    
            # print((cur_i, cur_j))
            map[cur_i][cur_j] = 1
            if((cur_i, cur_j) not in viable_positions):
                viable_positions.append((cur_i, cur_j))

            if(steps == 0):
                move_dir = int(seed[y % len(seed)])*int(seed[(y+1) % len(seed)])
                move_dir %= 4
                if(move_dir == coming_from_dir):
                    move_dir += 1
                    move_dir %= 4
                coming_from_dir = (move_dir+2) % 4
                steps = min_length_of_hallways
                y += 1

            # 0 = cima / 1 = esquerda / 2 = baixo / 3 = direita
            if(move_dir == 0):
                if(cur_i - 1 >= 0):
                    cur_i -= 1
                else:
                    steps = 0
                    x -= 1
                    continue
            
            elif(move_dir == 1):
                if(cur_j - 1 >= 0):
                    cur_j -= 1
                else:
                    steps = 0
                    x -= 1
                    continue
            
            elif(move_dir == 2):
                if(cur_i + 1 < N):
                    cur_i += 1
                else:
                    steps = 0
                    x -= 1
                    continue
            
            else:
                if(cur_j + 1 < M):
                    cur_j += 1
                else:
                    steps = 0
                    x -= 1
                    continue

            steps -= 1

            x += 1

        if(start_point == None):
            aux = int(seed[10])*int(seed[11])*int(seed[12])
            aux %= len(viable_positions)
            start_point = viable_positions[aux]
            viable_positions.pop(aux)

        print(viable_positions)
        if(end_point == None):
            # dist_to_end = -100
            # for pos in viable_positions:
            #     dist = abs(start_point[0] - pos[0]) + abs(start_point[1] - pos[1])
            #     if(dist > dist_to_end):
            #         dist_to_end = dist
            #         end_point = pos
            aux = int(seed[12])*int(seed[13])*int(seed[14])
            aux %= len(viable_positions)
            end_point = viable_positions[aux]

        char_map = [[str(s) for s in sublist] for sublist in map]

        for i in range(N):
            for j in range(M):

                if(map[i][j] == 1):
                    char_map[i][j] = '*'
                    
                else:
                    char_map[i][j] = '-'
                    

        char_map[start_point[0]][start_point[1]] = '#'
        char_map[end_point[0]][end_point[1]] = '$'
        
        if create_file:
            with open(f'Inputs/{seed}.txt', 'w') as f:
                # f.write(str(start_point[0]) + ' ' + str(start_point[1]) + '\n')
                # f.write(str(end_point[0]) + ' ' + str(end_point[1]) + '\n')
                f.write(f'{str(N)} {str(M)}\n')
                for sublist in char_map:
                    line = ''
                    for c in sublist:
                        line += c
                    f.write(line + '\n')


        return seed, start_point, end_point, char_map





    