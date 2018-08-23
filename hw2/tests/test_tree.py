import unittest
from tree.tree import Node, Btree


class Test(unittest.TestCase):

    def setup(self):
        # case 1
        self.answer_1 = [[1]]

        # case 2
        self.answer_2 = [['|', '|', '|', '|', '|', '|', '|', 1, '|', '|', '|', '|', '|', '|', '|'],
                     ['|', '|', '|', 2, '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|'],
                     ['|', 3, '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|'],
                     [4, '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|']]

        # case 3
        self.answer_3 = [['|', '|', '|', '|', '|', '|', '|', 1, '|', '|', '|', '|', '|', '|', '|'],
                     ['|', '|', '|', 2, '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|'],
                     ['|', '|', '|', '|', '|', 3, '|', '|', '|', '|', '|', '|', '|', '|', '|'],
                     ['|', '|', '|', '|', 4, '|', '|', '|', '|', '|', '|', '|', '|', '|', '|']]

        # case 4
        self.answer_4 = [['|', '|', '|', 1, '|', '|', '|'],
                     ['|', 2, '|', '|', '|', 3, '|'],
                     [4, '|', 5, '|', '|', '|', 6]]

    def test_1(self):
        a_1 = Node(1)
        tree_1 = Btree(a_1)
        assert tree_1.pring() == self.answer_1
        
    def test_2(self):
        a_2 = Node(1)
        b_2 = Node(2)
        c_2 = Node(3)
        d_2 = Node(4)
        a_2.left = b_2
        b_2.left = c_2
        c_2.left = d_2
        tree_2 = Btree(a_2)
        assert tree_2.pring() == self.answer_2
        
    def test_3(self):
        a_3 = Node(1)
        b_3 = Node(2)
        c_3 = Node(3)
        d_3 = Node(4)
        a_3.left = b_3
        b_3.right = c_3
        c_3.left = d_3
        tree_3 = Btree(a_3)
        assert tree_3.pring() == self.answer_3
        
    def test_4(self):
        a_4 = Node(1)
        b_4 = Node(2)
        c_4 = Node(3)
        d_4 = Node(4)
        e_4 = Node(5)
        f_4 = Node(6)
        a_4.left = b_4
        a_4.right = c_4
        b_4.left = d_4
        b_4.right = e_4
        c_4.right = f_4
        tree_4 = Btree(a_4)
        assert tree_4.pring() == self.answer_4
            
