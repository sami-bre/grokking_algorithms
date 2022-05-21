"""Dijkstra's algorithm is used to find the single source shortest path between to nodes
on a DAG (Directed acyclic graph). It is not used if the graph contains negative weights.
for graphs with negative weights, use the Bellman-ford algorithm. for unweighted graphs, use
BFS (breadth first search)"""

# make the graph
graph = dict()
graph["a"] = [("b", 5), ('c', 2)]
graph['b'] = [('d', 4), ('e', 2)]
graph['c'] = [('b', 8), ('e', 7)]
graph['d'] = [('f', 3), ('e', 6)]
graph['e'] = [('f', 1)]
graph['f'] = []

# make a list of all the nodes
nodes = ['a', 'b', 'c', 'd', 'e', 'f']


def dijkstra(graph, all_nodes, start, end):

    # setting up the costs hash table
    costs = {node:float("inf") for node in all_nodes}
    # the parents hash table
    parents = dict()
    # chores ... 
    nodes_left = all_nodes
    costs[start] = 0

    while nodes_left:
        # get the chepest node
        cheapest = costs[nodes_left[-1]]
        node_to_process = nodes_left[-1]
        for node in nodes_left:
            if costs[node] < cheapest:
                node_to_process = node
                cheapest = costs[node]
        
        # update adjecent costs
        for item in graph[node_to_process]:
            if costs[node_to_process] + item[1] < costs[item[0]]:
                costs[item[0]] = costs[node_to_process] + item[1]
                parents[item[0]] = node_to_process
        
        # remove the node from nodes_left
        nodes_left.remove(node_to_process)


    result = end
    point = end
    while True:
        point = parents[point]
        result = point + " -> " + result
        if point == start:
            break

    return result + "  with weight: {}".format(costs[end])

print(dijkstra(graph, nodes, "a", "f"))
