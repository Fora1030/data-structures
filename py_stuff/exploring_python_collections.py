import collections

def named_tuples():
    book : tuple = collections.namedtuple('book',['name', 'ISBN', 'quantity'])
    book_1 : tuple = book('Hands on data structures','9781788995573', '50')
    print(book)
    print(book_1)
    print(book_1.name)
    print(book_1[2])

def using_deque():
    d_linked_list = collections.deque()
    print(d_linked_list)
    d_linked_list.append("age")
    d_linked_list.appendleft("Name")
    d_linked_list.append('DOB')
    print(d_linked_list)
    print(d_linked_list.pop())
    print(d_linked_list)
    print(d_linked_list.popleft())
    print(d_linked_list)

if __name__ == "__main__":
    # named_tuples()
    using_deque()

    