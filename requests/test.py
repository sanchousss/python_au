import unittest
from main import check_prefixes
from main import get_all_user_prs
from main import get_all_commits
from main import send_pr_comment
from main import verify_pr

class TestVerifier(unittest.TestCase):
    def test_check_prefixes(self):
         first = 'HEXNUMBER-1022 Added verifier'
         result = check_prefixes(first)
         expect = 'OK'
         self.assertEqual(expect, result)

if __name__ == '__main__':
    unittest.main()