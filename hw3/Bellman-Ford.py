def negative_circle(txt):
    """
    params:
    txt: the text file with desired format for negative circle detection
    """
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
    
    #  detection for the negative circle
    negative_circle_list = set()    
    
    for v_1 in graph.keys():
        for v_2 in graph.keys():
            if (bellman(graph,len(graph.keys()),v_1,v_2) < bellman(graph,len(graph.keys())-1,v_1,v_2)
                #  this condition checks the existence of negative circle
                and bellman(graph,len(graph.keys()),v_1,v_1) < 0
                and bellman(graph,len(graph.keys()),v_2,v_2) < 0):
                #  this condition makes sure that the vertices in negative circle are recurrent
                negative_circle_list.add(v_1)
                negative_circle_list.add(v_2)

    if len(negative_circle_list) != 0:
        print("there exists negative circle with corresponding vertices:", negative_circle_list)
    else:
        print("there does not exist negative circle")

# the bellman-Ford algo

def bellman(graph,max_v,start,end):
    """
    params:
    graph: the graph dictionary
    max_v: the max number of vertices can be used
    start: the staring point
    end: the ending point
    """
    if max_v == 0:
        if start != end:
            return float("inf")
        else:
            return 0
    elif max_v == 1:
        for pair in graph[start]:
            if end == int(pair[1]):
                if pair[3] == "-":
                    return(-int(pair[4]))
                else:
                    return(int(pair[3]))
        return float("inf")
    else:
        alternative_list = []
        for vertex in graph.keys():
            if vertex in [int(i[1]) for i in graph[start]]: #  if this vertex is a nb of the start point
                for pair in graph[start]:
                    if vertex == int(pair[1]):
                        if pair[3] == "-":
                            alternative = bellman(graph,max_v-1,vertex,end) - int(pair[4])
                        else:
                            alternative = bellman(graph,max_v-1,vertex,end) + int(pair[3])
            else:
                alternative = float("inf")
            alternative_list.append(alternative)
        return(min(bellman(graph,max_v-1,start,end),min(alternative_list)))
