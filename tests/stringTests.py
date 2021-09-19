import unittest


class stringFixture(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEmptySubstringByArrayIndexRaiseError(self):
        with self.assertRaises(IndexError):
            y = ''[0]

    def testEmptySubstringByIndexesReturnEmpty(self):
        self.assertEqual(''[0:], '')


if __name__ == '__main__':
    unittest.main()
