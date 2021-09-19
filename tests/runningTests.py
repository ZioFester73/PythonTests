import unittest

class runningFixtures(unittest.TestCase):

  def setUp(self):
    pass

  def tearDown(self):
    pass

  def testVerify(self):
    self.assertEqual(1,1)

if __name__ == '__main__':
  unittest.main()

