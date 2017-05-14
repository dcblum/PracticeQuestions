# Given two strings s and t, determine whether some anagram of t is a substring
# of s. For example: if s = "udacity" and t = "ad", then the function returns
# True. Your function definition should look like: question1(s, t) and return a
# boolean True or False.

def question1(s,t):
    '''Checks if all characters in t are also in s'''
    if t in s:
        return True
    for i in range(len(s)):
        t_list = list(t)
        for j in s[i:]:
            if j in t_list:
                t_list.remove(j)
                if t_list == []:
                    return True

    return False


###############################################################################
###############################################################################

# Given a string a, find the longest palindromic substring contained in a. Your
# function definition should look like question2(a), and return a string.

def question2(a):

    longest = ''

    # Remove all unwanted characters from a; this list can be extended
    string = a
    chars = [' ', ',',':',';','.','!']
    for i in chars:
        string = string.replace(i, '')

    # Generate a list of character forwards and backwards
    a_nospaces = string.lower()
    a_back_nospaces =  a_nospaces[::-1]

    # Strings of < 2 characters are automatically palindromes as well as
    # strings that are already palindromes
    if len(a_nospaces) < 2:
        return a
    if a_back_nospaces == a_nospaces:
        return a

    # Shorten
    for i in range(len(a_nospaces)):
        for j in range(i,len(a_nospaces)):
            if a_nospaces[i:j+1] in a_back_nospaces:
                if len(a_nospaces[i:j+1]) > len(longest):
                    longest = a_nospaces[i:j+1]


    return longest


###############################################################################
###############################################################################


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

        # Check if the node has a path to unseen nodes and put them in a list
        for path in edges_list:
            if node in path:
                potential_node = path.replace(node, '')
                if potential_node not in confirmed_connections:
                    potential_connections.append(potential_node)

        # Add unseen nodes and check each of those
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


###############################################################################
###############################################################################


'''

 Find the least common ancestor between two nodes on a binary search tree. The
 least common ancestor is the farthest node from the root that is an ancestor of
 both nodes. For example, the root is a common ancestor of all nodes on the
 tree, but if both nodes are descendents of the root's left child, then that
 left child might be the lowest common ancestor. You can assume that both nodes
 are in the tree, and the tree itself adheres to all BST properties. The
 function definition should look like question4(T, r, n1, n2), where T is the
 tree represented as a matrix, where the index of the list is equal to the
 integer stored in that node and a 1 represents a child node, r is a
 non-negative integer representing the root, and n1 and n2 are non-negative
 integers representing the two nodes in no particular order. For example, one
 test case might be

question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)
and the answer would be 3.

'''

def question4(T,r,n1,n2):
    '''Return least common ancestor in Tree T with root r and through n1 and
    n2'''

    def map_tree(T, p):
        '''generate easier to understand tree'''
        # fill child_list if children of parent exist
        child_list = []
        for index in range(len(T[p])):
            if T[p][index] == 1:
                child_list.append(index)

        # If children were added map the children's children as well
        if child_list != []:
            map_dict[p] = child_list
            for child in child_list:
                map_tree(T, child)

    def map_parents_of_leaf(map_dict, n1):
        '''Map parents of the first node up to root'''
        n1_parents = []

        for key in map_dict:
            if n1 in map_dict[key]:
                n1 = key
                n1_parents.append(n1)

        if n1_parents != []:
            return map_parents_of_leaf(map_dict, n1) + n1_parents
        else:
            return []

    def map_parents_and_compare(map_dict, n2, n1_parents):
        '''Compare n1_parents map with n2; return first common n2 parent'''

        for key in map_dict:
            if n2 in map_dict[key]:
                n2 = key

        if n2 in n1_parents:
            return n2
        else:
            return map_parents_and_compare(map_dict, n2, n1_parents)


    map_dict = dict()
    map_tree(T, r)
    n1_map = map_parents_of_leaf(map_dict, n1)

    if n1_map == []:
        return r
    else:
        return map_parents_and_compare(map_dict, n2, n1_map)


###############################################################################
###############################################################################


'''
 Find the element in a singly linked list that's m elements from the end. For
 example, if a linked list has 5 elements, the 3rd element from the end is the
 3rd element. The function definition should look like question5(ll, m), where
 ll is the first node of a linked list and m is the "mth number from the end".
 You should copy/paste the Node class below to use as a representation of a node
 in the linked list. Return the value of the node at that position.

class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None


'''


class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None


def question5(ll, m):
    current_node = ll
    nodes = [current_node]

    # Make list of all nodes
    while(current_node.next):
        current_node = current_node.next
        nodes.append(current_node)

    # If m is too large nodes[:-m] generates an empty list
    # The boolean of an empty list is False
    if nodes[:-m]:
        return nodes[-m].data
    else:
        return None

###############################################################################
###############################################################################



########################################################################
#
#                   TEST Question1
#
########################################################################

print "Test Question 1: "

s1 = 'supercalifragilisticexpialidocious'
t1 = 'codious'

s2 = '1'
t2 = ''

s3 = 'abc123'
t3 = 'abc456'

s4 = ''
t4 = ''

print question1(s1,t1)
# True

print question1(s2,t2)
# True

print question1(s3,t3)
# False

print question1(s4,t4)
# True


########################################################################
#
#                   TEST Question2
#
########################################################################

print "\nTest Question 2: "

a0 = 'burgeregrub'
a1 = 'muzzle velocity'
a2 = ''
a3 = '1'
a4 = 'my favorite sport involves racecars'
a5 = 'There was a man, a plan, a canal: Panama'

print question2(a0)
# 'burgeregrub'

print question2(a1)
# 'level'

print question2(a2)
# ''

print question2(a3)
# '1'

print question2(a4)
# 'sracecars'

print question2(a5)
# 'amanaplanacanalpanama'



########################################################################
#
#                   TEST Question3
#
########################################################################

print "\nTest Question 3: "

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

a4 = {}

a5 = {
'A': []
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

print question3(a4)
# {}

print question3(a5)
# {}


########################################################################
#
#                   TEST Question4
#
########################################################################

print "\nTest Question 4: "


a1 = question4(
[[0, 1, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [1, 0, 0, 0, 1],
 [0, 0, 0, 0, 0]],
 3, 1, 4)

a2 = question4(
[[0, 1, 1, 0, 0],
 [0, 0, 0, 1, 1],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0]],
 0, 0, 4)

a3 = question4(
[[0, 1, 1, 0, 0, 0],
 [0, 0, 0, 1, 1, 0],
 [0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 1],
 [0, 0, 0, 0, 0, 0]],
 0, 5, 3)

a4 = question4(
[[0]],
 0, 0, 0)

a5 = question4(
 [[0, 1, 1, 0, 0],
  [0, 0, 0, 1, 1],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0]],
  0, 4, 4)


print a1
# 3

print a2
# 0

print a3
# 1

print a4
# 0

print a5
# 1


########################################################################
#
#                   TEST Question5
#
########################################################################

print "\nTest Question 5: "

A = Node(1)
B = Node(2)
C = Node(3)
D = Node(4)
E = Node(5)
F = Node(6)
G = Node(7)
H = Node(8)
I = Node(9)
J = Node(10)

X = Node(7)

A.next = B
B.next = C
C.next = D
D.next = E
E.next = F
F.next = G
G.next = H
H.next = I
I.next = J

print question5(A, 5)
# 6

print question5(F, 3)
# 8

print question5(I, 10)
# None

print question5(A, 0)
# None
