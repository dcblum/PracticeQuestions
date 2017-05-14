
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
    map_dict = dict()

    def map_tree(T, p):
        child_list = []
        for index in range(len(T[p])):
            if T[p][index] == 1:
                child_list.append(index)


        # If children were added map the children's children as well
        if child_list != []:
            map_dict[p] = child_list
            for child in child_list:
                map_tree(T, child)

    map_tree(T, r)

    lca = 'burger'

    def find_lowest_ancestor(map_dict, n1, n2):

        for key in map_dict:
            if n1 in map_dict[key]:
                p1 = key
            else:
                p1 = r
            if n2 in map_dict[key]:
                p2 = key
            else:
                p2 = r

        if n1 == n2:
            return n1
        else:
            return find_lowest_ancestor(map_dict, p1, p2)

    return find_lowest_ancestor(map_dict, n1, n2)


########################################################################
#
#                   TESTS
#
########################################################################



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
 0, 3, 4)

a3 = question4(
[[0, 1, 1, 0, 0, 0],
 [0, 0, 0, 1, 1, 0],
 [0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 1],
 [0, 0, 0, 0, 0, 0]],
 0, 5, 2)

a4 = question4(
[[0]],
 0, 0, 0)


print a1
# 3

print a2
# 1

print a3
# 0

print a4
# 0
