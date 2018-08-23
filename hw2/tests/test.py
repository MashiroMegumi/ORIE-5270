import unittest
from tree.tree import Node, Btree


class Test(unittest.TestCase):
    def setup(self):
        a = Node(1)
        import unittest
from tree.tree import Node, Btree


class Test(unittest.TestCase):
    
    def setup(self):
        # case 1
        a_1 = Node(1)
        tree_1 = Btree(a_1)
        answer_1 = [[1]]
        
        # case 2
        a_2 = Node(1)
        b_2 = Node(2)
        c_2 = Node(3)
        d_2 = Node(4)
        a_2.l = b_2
        b_2.l = c_2
        c_2.l = d_2
        tree_2 = Btree(a_2)
        answer_2 = [['|', '|', '|', '|', '|', '|', '|', 1, '|', '|', '|', '|', '|', '|', '|'],
                     ['|', '|', '|', 2, '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|'],
                     ['|', 3, '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|'],
                     [4, '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|']]
        
        # case 3
        a_3 = Node(1)
        b_3 = Node(2)
        c_3 = Node(3)
        d_3 = Node(4)
        a_3.l = b_3
        b_3.r = c_3
        c_3.l = d_3
        tree_3 = Btree(a_3)
        answer_3 = [['|', '|', '|', '|', '|', '|', '|', 1, '|', '|', '|', '|', '|', '|', '|'],
                     ['|', '|', '|', 2, '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|'],
                     ['|', '|', '|', '|', '|', 3, '|', '|', '|', '|', '|', '|', '|', '|', '|'],
                     ['|', '|', '|', '|', 4, '|', '|', '|', '|', '|', '|', '|', '|', '|', '|']]
        
        # case 4
        a_4 = Node(1)
        b_4 = Node(2)
        c_4 = Node(3)
        d_4 = Node(4)
        e_4 = Node(5)
        f_4 = Node(6)
        a_4.l = b_4
        a_4.r = c_4
        b_4.l = d_4
        b_4.r = e_4
        c_4.r = f_4
        tree_4 = Btree(a_4)
        answer_4 = [['|', '|', '|', 1, '|', '|', '|'],
                     ['|', 2, '|', '|', '|', 3, '|'],
                     [4, '|', 5, '|', '|', '|', 6]]
        
        def test_1(self):
            assert tree_1.pring() == answer_1
        def test_2(self):
            assert tree_2.pring() == answer_2
        def test_3(self):
            assert tree_3.pring() == answer_3
        def test_4(self):
            assert tree_4.pring() == answer_4
