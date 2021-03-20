import unittest
from main import LeetCodeSource


class TestTriangle(unittest.TestCase):
    def test_get_md_solution_link(self):
         first = LeetCodeSource("7. Reverse Integer", "problems/reverse-integer/", "ddddd")
         expect = "+[Reverse Integer](#reverse-integer)"

         result = first.get_md_solution_link()

         self.assertEqual(expect, result)


if __name__ == '__main__':
    unittest.main()