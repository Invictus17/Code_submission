import collections

class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root):
        self.root = root
        self.queue = collections.deque([self.root])

    def __iter__(self):
        val = self.trav()
        if val:
            return val
        raise StopIteration

    def  trav(self):
        while self.queue:

            node = self.queue.pop()

            if node.right:
                self.queue.append(node.right)
            if node.left:
                self.queue.append(node.left)
            yield node.data



n1 = Tree(1)
n2 = Tree(2)
n3 = Tree(3)
n4 = Tree(4)
n5 = Tree(5, n1, n2)
n6 = Tree(6, n3, n4)
n7 = Tree(7, n5, n6)

results = BinaryTree(n7)

for res in results:
    print(res)
