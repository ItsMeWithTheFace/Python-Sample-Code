# Rakin Uddin

import unittest
from heaps import *

class TestHeapMethods(unittest.TestCase):

    def test_init(self):
        # Check if the heap is initialized properly
        test_heap = Heap([1, 2, 3, 4])
        self.assertEqual(test_heap._heap, [4, 3, 2, 1])
        # Heap is empty when initializing it with an input list
        # Heap incorrectly adding items to list

    def test_insert(self):
        # Check if .insert method is adding objects properly to heap
        test_heap = Heap([])
        test_heap._heap = [4, 2, 1, 3]
        test_heap.insert(5)
        self.assertEqual(test_heap._heap, [5, 4, 1, 3, 2])
        # .insert is concatenating an int with a list

    def test_bubble_up_middle_index(self):
        # Check if ._bubble_up method is properly percolating values at indices
        # that are not 0 or (len(list) - 1)
        test_heap = Heap([1, 4, 2, 3])
        test_heap._bubble_up(2)
        self.assertEqual(test_heap._heap, [4, 3, 2, 1])
        # Index of parent is not an int

    def test_remove_top_empty(self):
        # Check that an exception is being raised if the heap is empty
        test_heap = Heap([])
        with self.assertRaises(HeapEmptyError):
            test_heap.remove_top()
            # remove_top does not raise an error
            # Exception is named incorrectly

    def test_is_empty(self):
        # See if is_empty is correctly returning True for an empty list and
        # vice versa
        test_heap = Heap([])
        self.assertTrue(test_heap.is_empty())
        test_heap = Heap([1, 2, 3, 4])
        self.assertFalse(test_heap.is_empty())
        # is_empty returning NoneType instead of bool

    def test_violates_no_children(self):
        # Check if a tree has no children, .violates returns True
        test_heap = Heap([1])
        self.assertFalse(test_heap._violates(0))
        # Comparing differing types (int vs list)

    def test_bubble_down_one_child(self):
        # Check if heap is properly bubbled down with root > left child
        test_heap = Heap([1, 2])
        test_heap._bubble_down(0)
        self.assertEqual(test_heap._heap, [2, 1])
        # Goes into endless recursion by bubbling down from same position, not
        # recursively decomposing properly

    def test_remove_top_full_list(self):
        # See if heap.remove_top removes the first element in a list and
        # properly bubbles down the last element after replacing the removed
        # element
        test_heap = Heap([])
        test_heap._heap = [4, 2, 3, 1]
        test_heap.remove_top()
        self.assertEqual(test_heap._heap, [3, 2, 1])

    def test_bubble_up_first(self):
        # Bubbling up the first element should not change the list
        test_heap = Heap([])
        test_heap._heap = [1, 4, 2, 3]
        test_heap._bubble_up(0)
        self.assertEqual(test_heap._heap, [1, 4, 2, 3])

    def test_bubble_up_last(self):
        # Test to see if last element is bubbled up properly
        test_heap = Heap([])
        test_heap._heap = [1, 3, 2, 4]
        test_heap._bubble_up(3)
        self.assertEqual(test_heap._heap, [4, 1, 2, 3])
        # Bubble up was percolating the child node instead of the parent node







if(__name__ == '__main__'):
    unittest.main(exit=False)

