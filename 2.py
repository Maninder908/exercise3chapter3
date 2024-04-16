class ListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'<ListNode: {self.data}>'


class SinglyLinkedList:
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
        return f'<SinglyLinkedList ({self._size} element{plural}): [{values.lstrip(", ")}]>'

    def __len__(self):
        return self._size

    def append(self, value):
        new_node = ListNode(value)
        if not self._tail:
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
                current = self._head
                while current.next != self._tail:
                    current = current.next
                val = self._tail.data
                del self._tail
                current.next = None
                self._tail = current
                self._size -= 1
                return val

            list = SinglyLinkedList()
            for i in 'abc':
                list.append(i)
            val = list.pop()
            print(val, list)