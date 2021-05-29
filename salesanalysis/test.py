import unittest
from main import *


class testing(unittest.TestCase):
    def test_list_dict(self):
        result = list_dict('test.csv')
        print(result)
        expect = [{'date': '2020-1', 'resource': '1', 'count': '45'}, {'date': '2020-2', 'resource': '1', 'count': '49'}, {'date': '2020-3', 'resource': '1', 'count': '31'}, {'date': '2020-4', 'resource': '1', 'count': '11'}, {'date': '2020-5', 'resource': '1', 'count': '14'}, {'date': '2020-6', 'resource': '1', 'count': '41'}]
        self.assertEqual(expect, result)

if __name__ == '__main__':
    unittest.main() 