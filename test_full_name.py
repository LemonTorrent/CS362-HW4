import unittest
import full_name

class testCaseAdd(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(full_name.get_Full("fred", "green"), "fred green")

    def test_capitalization(self):
        self.assertEqual(full_name.get_Full("bEnnY", "BeAVer"), "bEnnY BeAVer")

    def test_format_int(self):
        self.assertEqual(full_name.get_Full(23, 42), "23 42")

    def test_format_float(self):
        self.assertEqual(full_name.get_Full(5.6, 90.2), "5.6 90.2")

if __name__ == '__main__':
    unittest.main()
