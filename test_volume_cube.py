import unittest
import volume_cube

class testCaseAdd(unittest.TestCase):
    def test_add(self):
        #result = volume_cube.calcVolume(2)
        #self.assertEqual(result, 8.0)
        self.assertEqual(volume_cube.calcVolume(2), 8.0)
        self.assertEqual(volume_cube.calcVolume(2), 8.0)
        #self.assertEqual(volume_cube.calcVolume(2), 4.0)
        #self.assertEqual(volume_cube.calcVolume(2), 6.0)

if __name__ == '__main__':
    unittest.main()
