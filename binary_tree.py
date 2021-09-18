from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    """
    Traversal depth-first:
    in-order, pre-order, post-order
    """

    """
    Traversal breadth-first
    """


class Tree:
    root_order: Node

    def __init__(self):
        self.root_node = None

    def inorder(self, root_node: Node):
        # infix notation / reverse polish notation
        current = root_node
        if current is None:
            return []
        return (self.inorder(current.left_child) +
                [current.data] +
                self.inorder(current.right_child))

    def traverse(self, order='preorder'):
        orders = {
            'preorder': self.preorder,
            'inorder': self.inorder,
            'postorder': self.postorder,
            'preorder_iter': self.preorder_iter
        }
        return orders[order](self.root_node)

    def preorder(self, root_node: Node):
        # prefix notation / polish notation
        current = root_node
        if current is None:
            return []
        return (
                [current.data] +
                self.preorder(current.left_child) +
                self.preorder(current.right_child)
        )

    def postorder(self, root_node: Node):
        # postfix notation / reverse polish notation
        current = root_node
        if current is None:
            return []
        return (self.postorder(current.left_child) +
                self.postorder(current.right_child) +
                [current.data])

    def preorder_iter(self, root_node: Node):
        if root_node is None:
            return []
        stack = deque()
        stack.append(root_node)
        retval = []
        while stack:
            current = stack.pop()
            retval.append(current.data)
            if current.right_child:
                stack.append(current.right_child)
            if current.left_child:
                stack.append(current.left_child)
        return retval

    def insert(self, data):
        node = Node(data)
        if self.root_node is None:
            self.root_node = node
            return
        current = self.root_node
        while True:
            parent = current
            if data < parent.data:
                current = current.left_child
                if current is None:
                    parent.left_child = node
                    return
            else:
                current = current.right_child
                if current is None:
                    parent.right_child = node
                    return

    def delete(self, data):
        parent, node = self.get_node_with_parent(data)

        if node is None:
            return False

        children = 0

        if node.left_child:
            children += 1
        if node.right_child:
            children += 1

        if not children:
            if parent:
                if parent.left_child is node:
                    parent.left_child = None
                else:
                    parent.right_child = None
            else:
                self.root_node = None

        elif children == 1:
            next_node = node.left_child or node.right_child
            if parent:
                if parent.left_child is node:
                    parent.left_child = next_node
                else:
                    parent.right_child = next_node
            else:
                self.root_node = next_node
        else:
            parent_of_leftmost_node = node
            leftmost_node = node.right_child
            while leftmost_node.left_child:
                parent_of_leftmost_node = leftmost_node
                leftmost_node = parent_of_leftmost_node.left_child
            node.data = leftmost_node.data
            if parent_of_leftmost_node.left_child is leftmost_node:
                parent_of_leftmost_node.left_child = leftmost_node.right_child
            else:
                parent_of_leftmost_node.right_child = leftmost_node.right_child

    def get_node_with_parent(self, data):
        parent = None
        current = self.root_node
        if current is None:
            return parent, None
        while True:
            if current is None:
                return None, None
            if current.data == data:
                return parent, current
            elif current.data > data:
                parent = current
                current = parent.left_child
            else:
                parent = current
                current = parent.right_child

    def min(self):
        current = self.root_node
        while current.left_child:
            current = current.left_child
        return current.data

    def max(self):
        current = self.root_node
        while current.right_child:
            current = current.right_child
        return current.data

    def search(self, data):
        current = self.root_node
        while True:
            if current is None:
                return None
            elif data == current.data:
                return data
            elif data < current.data:
                current = current.left_child
            else:
                current = current.right_child

    def breadth_first_traversal(self):
        list_of_nodes = []
        traversal_queue = deque([self.root_node])
        while len(traversal_queue) > 0:
            node = traversal_queue.popleft()
            list_of_nodes.append(node.data)
            if node.left_child:
                traversal_queue.append(node.left_child)
            if node.right_child:
                traversal_queue.append(node.right_child)
        return list_of_nodes

    def display_nodes(self, node: Node, space='\t', level=0):
        if node is None:
            print(space * level + '∅')
            return
        if node.left_child is None and node.right_child is None:
            print(space * level + str(node.data))
            return
        self.display_nodes(node.right_child, space, level + 1)
        print(space * level + str(node.data))
        self.display_nodes(node.left_child, space, level + 1)

    def display_tree(self):
        self.display_nodes(self.root_node)


def main():
    tree = Tree()
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.insert(1)

    # tree.insert(5)
    tree.insert(15)
    tree.insert(-1)
    tree.insert(10)

    tree.delete(5)
    print(tree.traverse(order='preorder'))
    print(tree.traverse(order='preorder_iter'))
    tree.display_tree()
    # tree.root_node = node_1
    # node_1.left_child = node_2
    # node_1.right_child = node_3
    # node_2.left_child = node_4


if __name__ == '__main__':
    main()
