


class BinarySearchThree(object):

    class __Node(object):
        def __init__(
                self, 
                key,
                data,
                left=None,
                right = None
        ):
            self.key = key
            self.data = data
            self.left_child = left
            self.right_child = right
            
        def __str__(self) -> str:
            return "{"+str(self.key)+", "+str(self.data)+"}"

    def __init__(self) -> None:
        self.__root = None
    
    def __find(self, goal):
        current = self.__root
        parent = self
        while (current and goal != current.key):
            parent = current
            current = (current.left_child if goal < current.key else current.right_child)
        
        return (current, parent)
    def is_empty(self):
        return self.__root is None

    def root(self):
        if self.is_empty():
            raise Exception("No root node is empty tree")
        return (self.__root.data, self.__root.key)
    
    def search(self, goal):
        node, p = self.__find(goal)
        return node.data if node else None


# if __name__ == "__main__":
    # bst = BinarySearchThree()
    # bst_node = bst.__Node(5, "Franklin", None, None)
    # print(bst_node.__str__())