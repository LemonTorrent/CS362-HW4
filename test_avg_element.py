import unittest
import avg_element

class testCaseAdd(unittest.TestCase):
    def test_pass(self):
        self.assertEqual(avg_element.list_avg([1, 2, 3]), 2)

    def test_float(self):
        self.assertEqual(avg_element.list_avg([3.0, 1.2, 9.3]), 4.5)

    def test_0(self):
        self.assertEqual(avg_element.list_avg([]), 0)

if __name__ == '__main__':
    unittest.main()
