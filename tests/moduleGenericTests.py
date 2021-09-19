import unittest

class genericFixture(unittest.TestCase):

    def setUp(self):
      print('setUp')

    def tearDown(self):
      print('tearDown')

    def testFoo(self):
        print('testing')
        self.assertEqual('foo'.upper(), 'FOO')

    def testBar(self):
        print('testing')
        self.assertNotEqual('foo'.upper(), 'foo')

if __name__ == '__main__':
    unittest.main()



