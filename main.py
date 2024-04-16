class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def pop(self):
        if not self.head:
            return None
        elif not self.head.next:
            val = self.head.data
            del(self.head)
            self.head = None
            return val
        else:
            current = self.head
            while current.next.next:
                current = current.next
                val = current.next.data
                del (current.next)
                current.next = None
                return val

            def __repr__(self):
                current = self.head
                nodes = []
                while current:
                    nodes.append(current.data)
                    current = current.next
                return f"<SinglyLinkedList: {nodes}>"


        list = SinglyLinkedList()
        for i in 'abc':
            list.append(i)
        val = list.pop()
        print(val, list)
