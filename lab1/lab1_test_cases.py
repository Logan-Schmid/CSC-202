import unittest
from lab1 import max_list_iter, reverse_rec, bin_search, reverse_list_mutate

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):
    TEST_LIST = [-1, 2, 4, 5, 6, 8, 9, 19, 29, 30]
    test_list_reverse = TEST_LIST.copy()
    test_list_reverse.reverse()

    def test_max_list_iter(self):
        # typical case & max last case
        self.assertEqual(30, max_list_iter(self.TEST_LIST))
        
        # empty list case
        self.assertIsNone(max_list_iter([]))

        # None case
        with self.assertRaises(ValueError):
            max_list_iter(None)
        self.assertRaises(ValueError, max_list_iter, None)

        # duplicate of max in list case
        self.assertEqual(25, max_list_iter([1,5,25,25,1]))
        
        # max first case
        self.assertEqual(25, max_list_iter([25,1,5,1]))

        # all negative ints case
        self.assertEqual(-6, max_list_iter([-10,-6,-7]))

    def test_reverse_rec(self):
        # simple case
        self.assertListEqual(reverse_rec([1,2,3]), [3,2,1])

        # typical case with TEST_LIST
        reversed_test_list = self.TEST_LIST.copy()
        reversed_test_list.reverse()
        self.assertListEqual(reverse_rec(self.TEST_LIST), reversed_test_list)

        # None list edge case
        with self.assertRaises(ValueError):
            reverse_rec(None)
        self.assertRaises(ValueError, reverse_rec, None)

        # empty list edge case
        self.assertListEqual(reverse_rec([]), [])

        # list length 1 edge case
        self.assertListEqual(reverse_rec([1]), [1])

        # mixed types case
        self.assertListEqual(reverse_rec(['a','b',3]), [3,'b','a'])

        # identical entries case
        self.assertListEqual(reverse_rec([0,0,0]), [0,0,0])

    def test_bin_search(self):
        # target is median of even list case
        self.assertEqual(bin_search(target=7, low=0, high=len(self.TEST_LIST)-1, int_list=self.TEST_LIST), None)
        
        # target is first left of median of even list case
        self.assertEqual(bin_search(target=6, low=0, high=len(self.TEST_LIST)-1, int_list=self.TEST_LIST), 4)

        # target is first right of median of even list case
        self.assertEqual(bin_search(target=8, low=0, high=len(self.TEST_LIST)-1, int_list=self.TEST_LIST), 5)

        # target is first entry in even list
        self.assertEqual(bin_search(target=-1, low=0, high=len(self.TEST_LIST)-1, int_list=self.TEST_LIST), 0)
        
        # target is last entry in even list
        self.assertEqual(bin_search(target=30, low=0, high=len(self.TEST_LIST)-1, int_list=self.TEST_LIST), 9)
        
        # target is less than first entry of list
        self.assertEqual(bin_search(target=-5, low=0, high=len(self.TEST_LIST)-1, int_list=self.TEST_LIST), None)
        
        # target is greater than last entry of list
        self.assertEqual(bin_search(target=35, low=0, high=len(self.TEST_LIST)-1, int_list=self.TEST_LIST), None)
        
        odd_list = [1, 3, 5, 6, 10]
        # target is median of odd list
        self.assertEqual(bin_search(target=5, low=0, high=len(odd_list)-1, int_list=odd_list), 2)
        
        # target is just left of odd list median
        self.assertEqual(bin_search(target=3, low=0, high=len(odd_list)-1, int_list=odd_list), 1)
        
        # empty list edge case
        self.assertEqual(bin_search(3,0,0,[]), None)

        # 1 entry target present edge case
        self.assertEqual(bin_search(1,0,0,[1]), 0)

        # 1 entry target not present edge case
        self.assertEqual(bin_search(2,0,0,[1]), None)

        # None list edge case
        with self.assertRaises(ValueError):
            bin_search(1, 0, 0, None)
        self.assertRaises(ValueError, bin_search, None, 1, 0, 0)

        # None target edge case
        with self.assertRaises(ValueError):
            bin_search(None, 0, 2, [1,2,3])
        self.assertRaises(ValueError, bin_search, None, 1, 0, 0)

    def test_reverse_list_mutate(self):
        # even num elements list case
        test_list_copy = self.TEST_LIST.copy()
        reverse_list_mutate(test_list_copy)
        self.assertListEqual(test_list_copy, self.test_list_reverse)

        # odd num elements list case
        rev_list_1 = [1,2,3,4,5]
        reverse_list_mutate(rev_list_1)
        self.assertListEqual(rev_list_1, [5,4,3,2,1])

        # empty list edge case
        rev_list_2 = []
        reverse_list_mutate(rev_list_2)
        self.assertListEqual(rev_list_2, [])

        # 1 entry list edge case
        rev_list_3 = [1]
        reverse_list_mutate(rev_list_3)
        self.assertListEqual(rev_list_3, [1])

        # None list edge case
        with self.assertRaises(ValueError):
            reverse_list_mutate(None)
        self.assertRaises(ValueError, reverse_list_mutate, None)

if __name__ == "__main__":
        unittest.main()

    
