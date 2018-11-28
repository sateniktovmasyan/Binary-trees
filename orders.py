# Only one class can be used
class EveryNode:
    def __init__(self, nodevalue):
        self.left = None
        self.right = None
        
        self.nodevalue = nodevalue

    def insert(self, nodevalue):
        if self.nodevalue:
            if nodevalue < self.nodevalue:
                if self.left is None:
                    self.left = EveryNode(nodevalue)
                else:
                    self.left.insert(nodevalue)
            elif nodevalue > self.nodevalue:
                if self.right is None:
                    self.right = EveryNode(nodevalue)
                else:
                    self.right.insert(nodevalue)
        else:
            self.nodevalue = nodevalue

    # Binary tree traverse preorder
    def preorder(self, root):
        array = []
        if root:
            array.append(root.nodevalue)
            array = array + self.preorder(root.left)
            array = array + self.preorder(root.right)
        return array

    # Binary tree traverse inorder
    def inorder(self, root):
        array = []
        if root:
            array = self.inorder(root.left)
            array.append(root.nodevalue)
            array = array + self.inorder(root.right)
        return array

    # Binary tree traverse postorder
    def postorder(self, root):
        array = []
        if root:
            array = self.postorder(root.left)
            array = array + self.postorder(root.right)
            array.append(root.nodevalue)
        return array

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.nodevalue)
        if self.right:
            self.right.PrintTree()


def main():
    tree = EveryNode(8)
    tree.insert(24)
    tree.insert(38)
    tree.insert(22)
    tree.insert(48)
    tree.insert(51)
    tree.insert(72)
    tree.insert(18)
    tree.insert(37)
    print("Preorder ")
    print(tree.preorder(tree))
    print("*" * 40)
    print("Inorder ")
    print(tree.inorder(tree))
    print("*" * 40)
    print("postorder ")
    print(tree.postorder(tree))
    print("*" * 40)


main()
