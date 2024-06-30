class Node():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.right = right
        self.left = left


class Tree():
    def __init__(self):
        pass

    def add_node(self, data):
        return Node(data)

    def add_left(self, parent: Node, data):
        node = Node(data)
        parent.left = node
        return node

    def add_right(self, parent: Node, data):
        node = Node(data)
        parent.right = node
        return node
    
    def print_in_order(self, node: Node):
        if not node:
            return
        # print left
        self.print_in_order(node.left)
        # print node.data
        print(node.data)
        # print right
        self.print_in_order(node.right)
    
    def print_pre_order(self, node: Node):
        if not node:
            return
        print(node.data)
        self.print_pre_order(node.left)
        self.print_pre_order(node.right)

    def print_post_order(self, node: Node):
        if not node:
            return 
        # First recur on left subtree
        self.print_post_order(node.left)
    
        # Then recur on right subtree
        self.print_post_order(node.right)
        print(node.data)
    

    def _show_prefix(self, path: list, v):
        prefix = [p + "    " for p in path[:-1]]
        print("".join(prefix) + "|--- " + v)
        

    def show(self, node: Node, path: list, i=0):
        if not node:
            return
        if i > 0:
            self._show_prefix(path, str(node.data))
        else:
            print(node.data)
        self.show(node.left, path + ["|"], i + 1)
        if not node.left and node.right:
            self._show_prefix(path + ["|"], "None")
        self.show(node.right, path + [" "], i + 1)
        if node.left and not node.right:
            self._show_prefix(path + [" "], "None") 