import unittest
from code import reportExpert

class reportFixtures(unittest.TestCase):

  def testEmptyReport(self):
    
    outputReport = reportExpert.getReport()
    
    self.assertEqual(outputReport, 'column1|column2|column3', 'Show only column header for no value')