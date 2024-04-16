class ListNode:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self):
        return f'<ListNode: {self.data}>'

    def __str__(self):
        return str(self.data)


class DoublyLinkedList:
    def __init__(self):
        self._head = self._tail = None
        self._size = 0

    def __repr__(self):
        current_node = self._head
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        plural = '' if self._size == 1 else 's'
        return f'<DoublyLinkedList ({self._size} element{plural}): [{values.lstrip(", ")}]>'

    def __len__(self):
        return self._size

    def __iter__(self):
        self._iter_index = self._head
        return self

    def __next__(self):
        if self._iter_index:
            value = self._iter_index.data
            self._iter_index = self._iter_index.next
            return value
        else:
            raise StopIteration

    def append(self, value):
        new_node = ListNode(value, next=None, prev=self._tail)
        if self._head is None:
            self._head = self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1

    def pop(self):
        if not self._head:
            return None
        elif self._head == self._tail:
            val = self._head.data
            del self._head
            self._head = self._tail = None
            self._size = 0
            return val
        else:
            val = self._tail.data
            self._tail = self._tail.prev
            del self._tail.next
            self._tail.next = None
            self._size -= 1
            return val

        def contains(self, value):
            for node_value in self:
                if value == node_value:
                    return True
            return False

        def clear(self):
            current_node = self._head
            while current_node:
                next_node = current_node.next
                del current_node
                current_node = next_node
            self._head = self._tail = None
            self._size = 0

        def insert(self, index, value):
            if index < 0 or index > self._size:
                raise ValueError("Index out of bounds")

            new_node = ListNode(value)

            if index == 0:
                new_node.next = self._head
                if self._head:
                    self._head.prev = new_node
                    self._head = new_node
                    if self._tail is None:
                        self._tail = new_node
                elif index == self._size:
                    new_node.prev = self._tail
                    self._tail.next = new_node
                    self._tail = new_node
                else:
                    current_node = self._head
                    for _ in range(index - 1):
                        current_node = current_node.next
                    new_node.prev = current_node
                    new_node.next = current_node.next
                    current_node.next.prev = new_node
                    current_node.next = new_node

                self._size += 1
                