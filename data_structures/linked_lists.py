import time

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
        current = self.head
        prev = self.head
        node = Node(data)
        count = 1
        while current:
            if current.next is None:
                node.next = current
                self.head = node
                print(count)
                return
            elif index == count:
                node.next = current
                prev.next = node
                return
            count += 1
            prev = current
            current = current.next
            if count < index:
                print("The list has less number of elements")


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

words.append_at_a_location('new', 3)

current = words.head
while current:
    print(current.data)
    current = current.next