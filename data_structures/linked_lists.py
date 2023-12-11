class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        print(self.tail)
        if self.tail:
            print(f"self tail: {self.tail}")
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node

    def append_at_a_location(self, data, index):
        ...
        
    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val
    
words = SinglyLinkedList()
words.append('One')
words.append('Two')
words.append('Three')

current = words.head
while current:
    print(current.data)
    current = current.next