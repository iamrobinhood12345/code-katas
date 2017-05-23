class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def length(node):
    if not node:
        return 0
    length = 1
    next = node
    while True:
        if next.next:
            length += 1
            next = next.next
        else:
            break
    return length


def count(node, data):
    if not node:
        return 0
    count = 0
    next = node
    while True:
        if next.data == data:
            count += 1
        if next.next:
            next = next.next
        else:
            break
    return count
