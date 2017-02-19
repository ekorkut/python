from node import Node
from collections import deque


def print_levels(root):
    q = deque()
    q.append(root)
    while len(q) > 0:
        nodes = []
        while len(q) > 0:
            nodes.append(q.popleft())
        s = ""
        for n in nodes:
            s += str(n.data) + " "
            if n.left is not None:
                q.append(n.left)
            if n.right is not None:
                q.append(n.right)
        print s


def tree_to_sorted_list(root, out=[]):
    if root is None:
        return out
    if root.left is not None:
        return tree_to_sorted_list(root.left, out)
    out.append(root.data)
    if root.right is not None:
        return tree_to_sorted_list(root.right, out)
    return out


def insert(root, data):
    n = Node(data, None, None)
    if root is None:
        return n

    prev = root
    while True:
        if data < prev.data:
            next_node = prev.left
        else:
            next_node = prev.right
        if next_node is None:
            break
        else:
            prev = next_node
    if data < prev.data:
        prev.left = n
    else:
        prev.right = n

    return root

one = Node(1, None, None)
three = Node(3, None, None)
six = Node(6, None, None)

two = Node(2, one, three)
seven = Node(7, six, None)

four = Node(4, two, seven)

print "Original tree"
print_levels(four)

print "After inserting 8,9,10,11 without balancing"
insert(four, 8)
insert(four, 9)
insert(four, 10)
insert(four, 11)
print_levels(four)







