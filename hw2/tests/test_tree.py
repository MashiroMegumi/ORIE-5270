import unittest


class Test(unittest.TestCase):
    
    def setup(self):
        # case 1
        self.a_1 = Node(1)
        self.tree_1 = Btree(a_1)
        self.answer_1 = [[1]]
        
        # case 2
        self.a_2 = Node(1)
        self.b_2 = Node(2)
        self.c_2 = Node(3)
        self.d_2 = Node(4)
        self.a_2.l = self.b_2
        self.b_2.l = self.c_2
        self.c_2.l = self.d_2
        self.tree_2 = Btree(a_2)
        self.answer_2 = [['|', '|', '|', '|', '|', '|', '|', 1, '|', '|', '|', '|', '|', '|', '|'],
                     ['|', '|', '|', 2, '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|'],
                     ['|', 3, '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|'],
                     [4, '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|']]
        
        # case 3
        self.a_3 = Node(1)
        self.b_3 = Node(2)
        self.c_3 = Node(3)
        self.d_3 = Node(4)
        self.a_3.l = self.b_3
        self.b_3.r = self.c_3
        self.c_3.l = self.d_3
        self.tree_3 = Btree(a_3)
        self.answer_3 = [['|', '|', '|', '|', '|', '|', '|', 1, '|', '|', '|', '|', '|', '|', '|'],
                     ['|', '|', '|', 2, '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|'],
                     ['|', '|', '|', '|', '|', 3, '|', '|', '|', '|', '|', '|', '|', '|', '|'],
                     ['|', '|', '|', '|', 4, '|', '|', '|', '|', '|', '|', '|', '|', '|', '|']]
        
        # case 4
        self.a_4 = Node(1)
        self.b_4 = Node(2)
        self.c_4 = Node(3)
        self.d_4 = Node(4)
        self.e_4 = Node(5)
        self.f_4 = Node(6)
        self.a_4.l = self.b_4
        self.a_4.r = self.c_4
        self.b_4.l = self.d_4
        self.b_4.r = self.e_4
        self.c_4.r = self.f_4
        self.tree_4 = Btree(a_4)
        self.answer_4 = [['|', '|', '|', 1, '|', '|', '|'],
                     ['|', 2, '|', '|', '|', 3, '|'],
                     [4, '|', 5, '|', '|', '|', 6]]
        
        def test_1(self):
            assert self.tree_1.pring() == self.answer_1
        def test_2(self):
            assert self.tree_2.pring() == self.answer_2
        def test_3(self):
            assert self.tree_3.pring() == self.answer_3
        def test_4(self):
            assert self.tree_4.pring() == self.answer_4
            
