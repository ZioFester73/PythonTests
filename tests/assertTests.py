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
        funct = lambda x: 1 / x

        with self.assertRaises(Exception):
            funct(0)


if __name__ == '__main__':
    unittest.main()
