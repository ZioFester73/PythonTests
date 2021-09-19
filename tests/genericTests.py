import unittest

class genericFixture(unittest.TestCase):

    def setUp(self):
      pass

    def tearDown(self):
      pass

    def testFoo(self):
      self.assertEqual('foo'.upper(), 'FOO')

    def testBar(self):
      self.assertNotEqual('foo'.upper(), 'foo')

if __name__ == '__main__':
    unittest.main()



