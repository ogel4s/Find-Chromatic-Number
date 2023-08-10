

def one_step_evaluation(list_of_vertexs , graph , chromatic_number , start=0):
    """Assigning a chromatic number to qualified vertices"""

    if all(isinstance(i , tuple) for i in list_of_vertexs): # Checking the end of a round of evaluation for a chromatic number
        return [item if type(item[1]) == int else item[0] for item in list_of_vertexs] # Remove all crossed vertices at the end of each evaluation
    
    list_of_vertexs[start] = (list_of_vertexs[start] , chromatic_number) # Assigning a chromatic number to the qualified vertex

    for j in graph[list_of_vertexs[start][0]]:
        if not any((isinstance(i, tuple) and i[0] == j and (i[1] == '/' or isinstance(i[1], int))) for i in list_of_vertexs): # Checking if a vertex is crossed or not
            list_of_vertexs[list_of_vertexs.index(j)] = (j , '/') # Crossing a vertex that does not have conditions
    
    return one_step_evaluation(list_of_vertexs , graph , chromatic_number , next((ind for ind, vtx in enumerate(list_of_vertexs) if isinstance(vtx, str)), -1)) # Iterate the function along with starting from the empty vertex with conditions

def find_chromatic_number(list_of_vertexs , graph):
    """Find the chromatic number for a graph"""
    _chromatic_number = 1
    while not all(isinstance(item, tuple) and isinstance(item[1] , int) for item in list_of_vertexs): # Checking whether all vertices have numbers or not
        list_of_vertexs = one_step_evaluation(list_of_vertexs , graph , _chromatic_number , next((ind for ind, vtx in enumerate(list_of_vertexs) if isinstance(vtx, str)), -1))
        _chromatic_number += 1

    return list_of_vertexs , _chromatic_number - 1

def sort(graph):
    """Generate a list of vertices to reduce the number of evaluations"""
    return [i[0] for i in sorted(graph.items() , reverse=True)]



if __name__ == '__main__':

    graph = {

    'a': ['b', 'd', 'f'],
    'b': ['c', 'a', 'e'],
    'c': ['b', 'd', 'f'],
    'd': ['a', 'c', 'e'],
    'e': ['d', 'f', 'b'],
    'f': ['e', 'a', 'c']

    }

    vtxs = sort(graph)

    vtxs , cnumber = find_chromatic_number(vtxs , graph)

    print(f"\nPainted vertices -> {vtxs}")
    print(f"Chromatic number -> {cnumber}\n")
    