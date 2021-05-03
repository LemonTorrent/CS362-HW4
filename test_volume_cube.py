import unittest
import volume_cube

class testCaseAdd(unittest.TestCase):
    def test_pass2(self):
        self.assertEqual(volume_cube.calcVolume(2), 8)
        #self.assertEqual(volume_cube.calcVolume(2), 8.0)

    def test_pass3_5(self):
        self.assertEqual(volume_cube.calcVolume(3.5), 42.875)

    def test_fail4(self):
        self.assertEqual(volume_cube.calcVolume(4), 1)

    def test_fail2_1(self):
        self.assertEqual(volume_cube.calcVolume(2.1), 10)

    def test_fail_inputstr(self):
        self.assertEqual(volume_cube.calcVolume("abc"), 2)

    def test_fail_inputchar(self):
        self.assertEqual(volume_cube.calcVolume('z'), 2)

if __name__ == '__main__':
    unittest.main()
