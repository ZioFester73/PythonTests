import unittest

class TestStringMethods(unittest.TestCase):

    def testVerify(self):
        print('testing')
        self.assertEqual('foo'.upper(), 'FOO')

    def setUp(self):
      print('setUp')

    def tearDown(self):
      print('tearDown')

if __name__ == '__main__':
    unittest.main()



