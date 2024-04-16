class SinglyLinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = self.Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = self.Node(data)

    def pop(self):
        if not self.head:
            raise Exception("List is empty")
        current = self.head
        prev = None
        while current.next:
            prev = current
            current = current.next
        if prev:
            prev.next = None
        else:
            self.head = None
        return current.data


my_list = SinglyLinkedList()
for i in 'abc':
    my_list.append(i)
val = my_list.pop()
print(val, my_list)
