'''
Created on Oct 8, 2014

@author: junaed
'''
import sys


def get_node_weights(weights, links, N, start, color):
    color[start] = False
    for j in xrange(0, N):
        if  start == j:
            continue
        if links[start][j] == True and color[j] :
            weights[start] += get_node_weights(weights, links, N, j, color)
    return weights[start] 
                

if __name__ == '__main__':
    old_sys = sys.stdin
#     sys.stdin = open("treepruning.txt", "r")
    
    N_K = raw_input()
    N = int(N_K.split(" ")[0])
    K = int(N_K.split(" ")[1])
   
    weights = raw_input()
    weights = [int(x) for x in weights.split(" ")]
    
    links = [[False for i in xrange(0, N)] for j in xrange(0, N)]
    
    for i in xrange(0, N - 1):
        edges = raw_input()
        edges = edges.split(" ")
        source = int(edges[0])
        dest = int(edges[1])
    
        links[source - 1][dest - 1] = True
        links[dest - 1][source - 1] = True
    
    c_weights = list(weights)
    color = [True for i in xrange(0, N)]
    root_weight = get_node_weights(c_weights, links, N, 0, color)
#     print c_weights
    low_number = 99999999999
    k = K
    while k > 0:
        lowest = low_number
        l_index = -1
        for i in xrange(N - 1, -1, -1):
            if c_weights[i] < lowest:
                lowest = c_weights[i]
                l_index = i
#         print c_weights
#         print lowest, l_index
        if l_index != -1:
            weights[l_index] = 99999999999
            removed = []
            for i in xrange(0, N):
                if links[l_index][i] == True:
                    links[l_index][i] = False
                    links[i][l_index] = False
                    removed.append(i)
#                     print "Remove " + str(l_index) + "<-->" + str(i)
#             k -= len(removed)
            for i in removed:
                link_count = 0
                for j in xrange(0, N):
                    if links[i][j]:
                        link_count += 1
                        break
                if link_count == 0 and weights[i] < 0:
                    weights[i] = low_number
            color = [True for i in xrange(0, N)]
            c_weights = list(weights)
#             print c_weights
            t_weight = get_node_weights(c_weights, links, N, 0, color)
#             print c_weights
#             if t_weight > root_weight:
            root_weight = t_weight
            k -= 1
        
    sys.stdout.write(str(root_weight))
    sys.stdin = old_sys
