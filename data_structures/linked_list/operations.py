from node import Node

two = Node(2)


def print_elements(head):
    while head is not None:
        print head.data
        head = head.next


def insert_tail(head, data):
    while head.next is not None:
        head = head.next
    head.next = Node(data)


def insert_head(head, data):
    n = Node(data, head)
    return n


def insert_nth(head, data, position):

    if position == 0:
        new_node = Node(data, head)
        return new_node
    ct = 1
    before = head
    after = head.next
    while ct < position:
        before = before.next
        after = after.next
        ct += 1
    new_node = Node(data, after)
    before.next = new_node

    return head


def delete(head, position):
    if position == 0:
        return head.next
    if head is None:
        return None
    ct = 1
    before = head
    while ct < position:
        before = before.next
        ct += 1

    before.next = before.next.next

    return head

print 'Beginning'
print_elements(two)
insert_tail(two, 3)
print 'After inserting 3 at tail'
print_elements(two)
n = insert_head(two, 1)
print 'After inserting 1 at the head'
print_elements(n)

n = insert_nth(n, 3.5, 3)
print 'After inserting 3.5 at position 3'
print_elements(n)
print 'After deleting 2 at position 1'
n = delete(n, 1)
print_elements(n)


