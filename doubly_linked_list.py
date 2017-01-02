"""

Doubly Linked List


Doubly_Linked_List([1, 2, 3])

The Doubly Linked List has a head and tail.
Push push(val) Node objects onto the head of a Doubly Linked
List. Pop pop() Node objects off of the head of a Doubly
Linked List. Append append(val) Node objects on the tail of a
Doubly Linked List. Shift shift() Node objects off the tail
of a Doubly Linked List. Remove remove() Node objects from 
the Doubly Linked List.


"""

class Doubly_Linked_List(object):
    """Doubly Linked List constructor."""

    def __init__(self, *val):
        """Initialize Doubly Linked List."""
        self.head = None
        self.tail = None
        for each in val:
            self.push(each)


    def push(self, val):
        """Insert 'val' at head as Node object."""
        if not self.head:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.head = Node(val, self.head)
            self.head.tail_neighbor.head_neighbor = self.head


    def append(self, val):
        """Append 'val' at tail as Node object."""
        if not self.head:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail = Node(val, head_neighbor=self.tail)
            self.tail.head_neighbor.tail_neighbor = self.tail


    def pop(self):
        """Pop head off the Doubly Linked List
        and return value of the Node."""
        if self.head is None:
            raise IndexError('Cannot pop from an empty Doubly Linked List.')
        popped_val = self.head.val
        if self.head is self.tail:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            self.head = self.head.tail_neighbor
            self.head.head_neighbor = None
        return popped_val


    def shift(self):
        """Shift tail off the Doubly Linked list
        and return the value of the Node."""
        if self.tail is None:
            raise IndexError('Cannot shift from an empty Doubly Linked List')
        shifted_val = self.tail.val
        if self.head is self.tail:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            self.tail = self.tail.head_neighbor
            self.tail.tail_neighbor = None
        return shifted_val


    def remove(self, val):
        """Remove the Node with value val from the
        Doubly Linked List."""
        search_node = self.head
        while True:
            if search_node.val == val:
                if search_node is self.tail and search_node is self.head:
                    self.head = None
                    self.tail = None
                    break
                elif search_node is self.tail:
                    self.tail = search_node.head_neighbor
                    search_node.head_neighbor.tail_neighbor = None
                    break
                elif search_node is self.head:
                    self.head = search_node.tail_neighbor
                    search_node.tail_neighbor.head_neighbor = None
                    break
                else:
                    search_node.head_neighbor.tail_neighbor = search_node.tail_neighbor
                    search_node.tail_neighbor.head_neighbor = search_node.head_neighbor
                    break
            elif search_node is self.tail:
                raise ValueError('Value not found in Doubly Linked List')
            else:
                search_node = search_node.tail_neighbor


class Node(object):
    """Node object constructor."""

    def __init__(self, val= None, tail_neighbor=None, head_neighbor=None):
        """Initalize Node."""
        self.val = val
        self.tail_neighbor = tail_neighbor
        self.head_neighbor = head_neighbor
