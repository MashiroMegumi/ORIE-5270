# the node class for tree construction
class Node:
    def __init__(self, n):
        """
        param n: the value of the node
        """
        self.value = n  # set the node value, without specific left child and right child
        self.left = None
        self.right = None

    def addlc(self, l):  # the method to add a left child
        self.left = l

    def addrc(self, r):  # the method to add a right child
        self.right = r

    def getheight(self, node):
        if node is not None:
            return 1+max(self.getheight(node.left), self.getheight(node.right))
        else:
            return 0


# the binary tree class
class Btree(Node):
    def __init__(self, root):
        """
        root is a node with reference to its children
        """
        self.root = root
        self.height = self.getheight(root)  # get the tree height

        # initialize the matrix holding the results
        self.matrix = [["|" for i in range(2**self.height-1)] for j in range(self.height)]

    def ptree(self, node, l, r, h, matrix):
        '''
        node: a node with reference to its children
        l: the left boudnary
        r: the right boundary
        h: the current level
        matrix: the result matrix
        '''
        if node is not None:
            if h == self.height-1:
                index = (l+r)//2
                matrix[h][index] = node.value
            else:
                index = (l+r)//2
                matrix[h][index] = node.value
                self.ptree(node.left, l, index, h+1, matrix)
                self.ptree(node.right, index, r, h+1, matrix)

    def pring(self):
        self.ptree(self.root, 0, 2**self.height-1, 0, self.matrix)  # the default settings
        for i in self.matrix:
            print(i)
        return (self.matrix)
