import unittest
import psycopg2


class dbFixture(unittest.TestCase):

    def testConnection(self):
        psycopg2.connect(
            host="127.0.0.1",
            database="postgres",
            user="postgres",
            password="abcd1234")
