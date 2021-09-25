import unittest
from code import reportExpert

class reportFixtures(unittest.TestCase):

  def testEmptyReport(self):
    
    outputReport = reportExpert.getReport()
    
    self.assertEqual(outputReport, 'column1|column2|column3', 'Show only column header for no value')

  @unittest.skip("Need before a db")
  def testARowFromDb(self):

    dbContains('data1|data2|data3')

    outputReport = reportExpert.getReport()

    expected = ['column1|column2|column3', 'data1|data2|data3']
    self.assertEqual(outputReport, expected, 'One line from db')


def dbContains(aRow):
  pass