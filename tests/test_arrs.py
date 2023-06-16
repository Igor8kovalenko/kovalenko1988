import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):

        self.assertEqual(arrs.get([1, 2, 3],2 , "test"), 3)
        self.assertEqual(arrs.get([1], 0, "test"), 1)
        self.assertEqual(arrs.get([1, 2], -1, "test"), "test")
        self.assertEqual(arrs.get([0.2], 0, "test"), 0.2)
        self.assertEqual(arrs.get([1, 2, 3, 4], -2, "test"), "test")
        self.assertEqual(arrs.get([-1, -2, -3], -2, "test"), "test")
        self.assertEqual(arrs.get(["test", "qwe"], 1 ,"test"), "qwe")
        self.assertEqual(arrs.get([1, 2, 3], 2, "test"), 3)
        self.assertEqual(arrs.get(["test"], 0, "test"), "test")

    def test_slice(self):

        self.assertEqual(arrs.my_slice(([1, 2, 3, 4]), 5), [4])
        self.assertEqual(arrs.my_slice([1, 2, 3], 0), [1,2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4 ], 2), [3, 4])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 3), [4])
        self.assertEqual(arrs.my_slice([1, 2, 3, 6, 7, 8], 2), [3, 6, 7, 8])
        self.assertEqual(arrs.my_slice([9, 10],-1), [10])
        self.assertEqual(arrs.my_slice([4, 9, 10],-3, -1), [4, 9])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], -2), [3, 4])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 0, 1), [1])
        self.assertEqual(arrs.my_slice(['f', 'g'], 0), ['f', 'g'])
        self.assertEqual(arrs.my_slice([], 0), [])
        self.assertEqual(arrs.my_slice([-1], True), [])
        self.assertTrue(arrs.my_slice([-1], False), [-1])
        self.assertEqual(arrs.my_slice([-1]), [-1])
        self.assertNotEqual(arrs.my_slice([-1, -2, -3], -4), [-2])
        self.assertNotEqual(arrs.my_slice([1, 2, 3, 4]), [4])
        self.assertEqual(arrs.my_slice([1+2, 2+3], 0), [3, 5])


















