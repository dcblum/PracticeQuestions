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


########################################################################
#
#                   TESTS
#
########################################################################

A = Node(4)
B = Node(7)
C = Node(8)
D = Node(20)
E = Node(17)
F = Node(2)
G = Node(10)
H = Node(11)
I = Node(12)
J = Node(13)

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
# 2

print question5(F, 3)
# 11

print question5(I, 10)
# None
