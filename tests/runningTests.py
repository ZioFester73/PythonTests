import unittest

class runningFixtures(unittest.TestCase):

  def setUp(self):
    pass

  def tearDown(self):
    pass

  def testRunningFromPy(self):
    import subprocess

    stdout = subprocess.check_output('python code/genericModule.py', shell=True)

    self.assertEqual(stdout, b'module running\n')

if __name__ == '__main__':
  unittest.main()

