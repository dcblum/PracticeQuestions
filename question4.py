
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
        '''generate map of all parents with child_list'''
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
        '''Map parents of the first node'''
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
