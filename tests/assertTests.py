import unittest

class assertFixture(unittest.TestCase):

    def setUp(self):
      pass

    def tearDown(self):
      pass

    def testEqual(self):
      self.assertEqual(1, 1)

    def testNotEqual(self):
      self.assertNotEqual(1, '1')

    def testRaiseException(self):
        with self.assertRaises(Exception):
            x = 1/0

if __name__ == '__main__':
    unittest.main()



