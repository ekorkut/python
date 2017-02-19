from node import Node

nine = Node(9, None, None)
eight = Node(8, None, None)
four = Node(4, None, None)
six = Node(6, Node, Node)

one = Node(1, None, nine)
seven = Node(7, eight, None)

five = Node(5, one, four)
two = Node(2, six, seven)

three = Node(3, five, two)


def print_left(n):
    if n.left is not None:
        print_left(n.left)
    print n.data


def print_right(n):
    print n.data
    if n.right is not None:
        print_right(n.right)



def top_view(n):
    if n.left is not None:
        print_left(n.left)
    print_right(n)


print 'Top view:'
top_view(three)