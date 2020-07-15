class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def union(self, llist):
        dict = {}
        arr = []

        last = self.head
        while (last):
            if last.value not in dict:
                dict[last.value] = True
                arr.append(last.value)
            last = last.next

        last = llist.head
        while (last):
            if last.value not in dict:
                dict[last.value] = True
                arr.append(last.value)
            last = last.next

        return arr

    def intersection(self, llist):
        arr = []
        dict = {}
        head = self.head
        while (head):
            llist1 = llist.head
            present = False
            while (llist1):
                if (head.value == llist1.value and head.value not in dict):
                    present = True
                    dict[head.value] = True
                    break
                llist1 = llist1.next
            if (present):
                arr.append(head.value)
            head = head.next

        return arr



# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

assert linked_list_1.union(linked_list_2) == [3, 2, 4, 35, 6, 65, 21, 32, 9, 1, 11]
assert linked_list_1.intersection(linked_list_2) == [4, 6, 21]

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)


assert linked_list_3.union(linked_list_4) == [3, 2, 4, 35, 6, 65, 23, 1, 7, 8, 9, 11, 21]
assert linked_list_3.intersection(linked_list_4) == []
