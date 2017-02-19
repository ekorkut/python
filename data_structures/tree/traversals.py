from node import Node
from collections import deque


one = Node(1, None, None)
four = Node(4, None, None)
six = Node(6, None, None)

five = Node(5, one, four)
two = Node(2, six, None)

three = Node(3, five, two)


def pre_order(n):
    print n.data
    if n.left is not None:
        pre_order(n.left)
    if n.right is not None:
        pre_order(n.right)


def post_order(n):
    if n.left is not None:
        post_order(n.left)
    if n.right is not None:
        post_order(n.right)
    print n.data


def in_order(n):
    if n.left is not None:
        in_order(n.left)
    print n.data
    if n.right is not None:
        in_order(n.right)


def level_order(n):
    q = deque()
    q.append(n)
    print n.data
    while len(q) > 0:
        n = q.popleft()

        if n.left is not None:
            print n.left.data
            q.append(n.left)
        if n.right is not None:
            print n.right.data
            q.append(n.right)

print 'Pre-order traversal:'
pre_order(three)
print 'Post-order traversal:'
post_order(three)
print "In-order traversal:"
in_order(three)
print "Level-order traversal:"
level_order(three)






