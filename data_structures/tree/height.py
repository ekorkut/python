from node import Node

seven = Node(7, None, None)
one = Node(1, None, None)
four = Node(4, None, None)

six = Node(6, seven, None)

two = Node(2, one, None)
five = Node(5, four, six)

three = Node(3, two, five)


def height(n):
    left_height = height(n.left) if n.left is not None else 0
    right_height = height(n.right) if n.right is not None else 0
    return max(left_height, right_height) + 1

print 'Height of the tree is:'
print height(three)



