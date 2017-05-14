
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
    '''Return the minimum spanning tree (msg) in G'''
    # make dict of weight (key) and edge (value)
    weight_dict = make_weight_dict(G)

    # Make list of sorted weights
    keylist = weight_dict.keys()
    keylist.sort()

    # initialize variables
    mst = dict()
    edges_list = []

    for weight in keylist:
        # Pick the next smallest edge from weight_dict
        for edge in weight_dict[weight]:
            # If a cycle is NOT created
            if not is_cycle(edges_list, edge):
                edges_list.append(edge)
                # Append to minimum spanning tree
                nodeA = edge[0]
                nodeB = edge[1]

                if nodeA not in mst:
                    mst[nodeA] = [(nodeB, weight)]
                else:
                    mst[nodeA].append((nodeB, weight))
                if nodeB not in mst:
                    mst[nodeB] = [(nodeA, weight)]
                else:
                    mst[nodeB].append((nodeA, weight))

    return mst



def is_cycle(edges_list, edge):
    '''Return True if including 'edge' in current edges list creates a cycle'''

    def generate_node_map(edges_list, node, confirmed_connections):
        '''Recursively updates connections to node from edges_list'''

        potential_connections = []

        # Add node to confirmed_connections
        for path in edges_list:
            if node in path:
                potential_node = path.replace(node, '')
                if potential_node not in confirmed_connections:
                    potential_connections.append(potential_node)

        # Add potential connections and check each of those
        if potential_connections != []:
            confirmed_connections += potential_connections
            for i in potential_connections:
                confirmed_connections += \
                generate_node_map(edges_list, i, confirmed_connections)

        return []

    nodeA = edge[0]
    nodeB = edge[1]
    node_map = [nodeA]

    generate_node_map(edges_list, nodeA, node_map)

    return nodeB in node_map

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

a2 = {
'A': [('C', 3),('D', 10), ('E', 2)],
'B': [('D', 6),('E', 1), ('Q', 10)],
'C': [('A', 3),('D', 4)],
'D': [('A', 10),('B', 6), ('C', 4), ('E', 4)],
'E': [('A', 2),('B', 1), ('D', 4)],
'F': [('D', 5), ('Q', 8)],
'Q': [('B', 10),('F', 8)]
}

a3 = {
'A': [('B', 2),('C', 6)],
'B': [('A', 2),('C', 5)],
'C': [('A', 6),('B', 5)],
'D': [('E', 4)],
'E': [('D', 4)]
}


print question3(a1)
# {'A': [('B', 2)],
# 'B': [('A', 2), ('C', 5)],
# 'C': [('B', 5)]}

print question3(a2)
# {
# 'A': [('E', 2), ('C', 3)],
# 'B': [('E', 1)],
# 'C': [('A', 3), ('D', 4)],
# 'D': [('C', 4), ('F', 5)],
# 'E': [('B', 1), ('A', 2)],
# 'F': [('D', 5), ('Q', 8)],
# 'Q': [('F', 8)]}
# }

print question3(a3)
# {
# 'A': [('B', 2)],
# 'C': [('B', 5)],
# 'B': [('A', 2), ('C', 5)],
# 'D': [('E', 4)],
# 'E': [('D', 4)]
# }
