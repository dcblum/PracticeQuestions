
'''
Given an undirected graph G, find the minimum spanning tree within G. A minimum
spanning tree connects all vertices in a graph with the smallest possible total
weight of edges. Your function should take in and return an adjacency list
structured like this:

{'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)],
 'C': [('B', 5)]}

Vertices are represented as unique strings. The function definition should be
question3(G)
'''


def question3(G):
    # make dict of weight (key) and edge (value)
    weight_dict = make_weight_dict(G)

    # Make list of sorted weights
    keylist = weight_dict.keys()
    keylist.sort()

    # initialize variables for 'while' loop
    mst = dict()
    edges = 0
    vertices = len(G)
    edges_list = []


    # Stop when (#edges) = (#vertices - 1)
    #while (edges < vertices):
        # Pick the next smallest edge from weight_dict


        # Check if next weight and edge pair would create a cycle

    return edges_list


    return mst


def is_cycle5(edges_list, edge):
    '''Return True if including 'edge' in dict 'G' creates a cycle'''

    def generate_node_map(edges_list, node, confirmed_connections):

        potential_connections = []

        # Add node to confirmed_connections
        for path in edges_list:
            if node in path:
                potential_node = path.replace(node, '')
                if potential_node not in confirmed_connections:
                    potential_connections.append(potential_node)

        # if there are potential connections
        if potential_connections != []:
            confirmed_connections += potential_connections
            for i in potential_connection:
                return generate_node_map(edges_list, i, confirmed_connections)

    nodeA = edge[0]
    nodeB = edge[1]

    connections = []

    if nodeB in generate_node_map(edges_list, nodeA, connections):
        return True
    else:
        return False


def make_weight_dict(G):

    # sort all edges (value) by weight (key)
    weight_dict = {}
    for nodeA in G:
        for pair in G[nodeA]:
            nodeB = pair[0]
            weight = pair[1]

            # sort nodes alphabtically then assign to edge
            if nodeA < nodeB:
                edge = nodeA + nodeB
            else:
                edge = nodeB + nodeA

            # Assign edge if weight not in the dictionary
            if weight not in weight_dict:
                weight_dict[weight] = [edge]
            # Append edge if it's not already in the list
            elif edge not in weight_dict[weight]:
                weight_dict[weight].append(edge)

    return weight_dict

########################################################################
#
#                   TESTS
#
########################################################################

a1 = {
'A': [('B', 2),('C', 6)],
'B': [('A', 2),('C', 5)],
'C': [('A', 6),('B', 5)]
}

# {'A': [('B', 2)],
# 'B': [('A', 2), ('C', 5)],
# 'C': [('B', 5)]}

print question3(a1)
