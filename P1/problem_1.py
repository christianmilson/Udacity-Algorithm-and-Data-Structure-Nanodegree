class Node:
    def __init__(self, value):
        self.value      = value
        self.previous   = None
        self.next       = None

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cache = {}
        self.capacity = self.validateCapacity(capacity)
        self.length = 0
        self.tail = None
        self.head = None

    def validateCapacity(self, value):
        if value > 0:
            return value

        raise ValueError('Capcity must be greater than zero')

    def get(self, key):
        if (key in self.cache):
            node = self.cache[key]
            self.removeNode(node)
            self.add(node)

            return node.value
        else:
            return -1

    def set(self, key, value):
        if (key not in self.cache):
            if (self.length == self.capacity):
                del self.cache[self.pop()]
            node = Node(value)
            self.cache[key] = node
            self.add(node)
        else:
            node = self.cache[key]
            self.removeNode(node)
            self.add(node)
            return

    def add(self, node):
        if (self.head is None):
            self.head = node
            self.tail = self.head
        elif (self.length == 1):
            node.next = self.head
            self.head.previous = node
            self.head = node
            self.tail.previous = self.head
        else:
            node.next = self.head
            self.head.previous = node
            self.head = node

        self.length += 1

    def pop(self):
        val = self.tail.value
        newTail = self.tail.previous
        newTail.next = None
        self.tail.previous = None
        self.tail = newTail

        self.length = self.length - 1
        return val

    def removeNode(self, node):
        if (node is self.head):
            newHead = node.next
            newHead.previous = None
            self.head.next = None
            self.head = newHead
        elif (node is self.tail):
            newTail = node.previous
            newTail.next = None
            self.tail.previous = None
            self.tail = newTail
        else:
            before = node.previous
            after = node.next
            before.next = after
            after.previous = before
            node.previous = None
            node.next = None

        self.length = self.length - 1

    def print(self):
        node = self.head
        while (node is not None):
            print(node.value)
            node = node.next
        

try :
    our_cache = LRU_Cache(5)
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    print(our_cache.get(1))  # returns 1
    print(our_cache.get(2))  # returns 2
    print(our_cache.get(9))  # returns -1
    our_cache.set(5, 5)
    our_cache.set(6, 6)
    print(our_cache.get(3))  # returns -1 because key 3 was thrown out
    our_cache.set(7, 7)
    print(our_cache.get(4))  # 4 is thrown out
except ValueError as e:
    print(e)

try :
    our_cache = LRU_Cache(0)
except ValueError as e:
    print(e)