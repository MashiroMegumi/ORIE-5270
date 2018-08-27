import heapq as hp

def find_shortest_path(txt, start, end):
    '''
    params:
    txt is the txt file to be read with desired format
    start is the starting vertex
    end is the end vertex
    '''
    
    #  read in the text file
    graph = {}
    file = open(txt,"r")
    for line in file:
        if len(line) == 2:
            vertex = int(line)
            graph[vertex] = None
        else:
            for key, value in graph.items():
                if value == None:
                    graph[key] = line.split()
    
    # the Dijkstra’s algorithm
    d = dict.fromkeys(graph.keys()) # the distance dictionary
    d[start] = 0
    
    path = dict.fromkeys(graph.keys()) # the path dictionary
    for key in path.keys():
        path[key] = []
    path[start] = [start]
    
    
    S = []
    F = []
    hp.heappush(F,(d[start],start))
    while len(F) != 0:
        f = hp.heappop(F)
        S.append(f[1])
                
        if graph[f[1]] != []:  # if the neighbors exist
            for neighbor in graph[f[1]]:
                v_name = int(neighbor[1])
                v_weight = int(neighbor[3])
                if v_name not in S and v_name not in [i[1] for i in F]:
                    d[v_name] = d[f[1]] + v_weight
                    hp.heappush(F,(d[v_name],v_name))
                    path[v_name] = path[f[1]]+[v_name]
                else:
                    if d[f[1]] + v_weight < d[v_name]:
                        d[v_name] = d[f[1]] + v_weight
                        path[v_name] = path[f[1]]+[v_name]
    
    print("the shortest distance is :", d[end], " the corresponding path is :", path[end])

