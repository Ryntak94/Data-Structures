class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def get_next(self):
        return self.next

    def set_next(self, node):
        self.next = node



class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def add_to_head(self, value):
        # 2 operations
        # Create a new node
        new_head = Node(value)
        new_head.set_next(self.head)
        if(self.head == None):
            self.tail = new_head
        self.head = new_head

    def add_to_tail(self, value):
        # 2 operations
        # Create a new node
        new_tail = Node(value)
        self.tail.set_next(new_tail)
        self.tail = new_tail

    def delete_from_head(self):
        self.head = self.head.get_next()

    def length(self):
        count = 0
        cur = self.head
        while cur != None:
            count += 1
            cur = cur.get_next()

        return count
