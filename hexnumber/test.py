import unittest
from hexnumber.hexnum import HexNumber


class testing(unittest.TestCase):
    def test_add_common(self):
        num1 = HexNumber("310")
        num2 = HexNumber("120")
        expect = "430"
        result = str(num1.add(num2))
        self.assertEqual(expect, result)

    def test_add_complicated(self):
        num1 = HexNumber("B55")
        num2 = HexNumber("730")
        expect = "1285"
        result = str(num1.add(num2))
        self.assertEqual(expect, result)

    def test_add_different_len(self):
        num1 = HexNumber("11")
        num2 = HexNumber("1111")
        expect = "1122"
        result = str(num1.add(num2))
        self.assertEqual(expect, result)


if __name__ == '__main__':
    unittest.main()