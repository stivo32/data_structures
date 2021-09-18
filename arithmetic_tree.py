from collections import deque


class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None


def calc(node: TreeNode):
    if node.data == '+':
        return calc(node.left) + calc(node.right)
    if node.data == '-':
        return calc(node.left) - calc(node.right)
    if node.data == '*':
        return calc(node.left) * calc(node.right)
    if node.data == '/':
        return calc(node.left) / calc(node.right)
    return node.data


def create_tree(expr: list):
    stack = deque()
    operators = '+-/*'

    for term in expr:
        if term in operators:
            node = TreeNode(term)
            node.right = stack.pop()
            node.left = stack.pop()
        else:
            node = TreeNode(int(term))
        stack.append(node)
    return stack.pop()


def main():
    expr = '4 5 + 5 3 - *'  .split()
    tree = create_tree(expr)
    print(tree.data)
    print(calc(tree))




if __name__ == '__main__':
    main()