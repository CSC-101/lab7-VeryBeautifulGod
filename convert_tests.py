import convert
import unittest

class TestCases(unittest.TestCase):

    def test_valid_float_string(self):
        result = convert.str_to_float("3.14")
        self.assertIsNotNone(result)
        self.assertEqual(result, 3.14)


    def test_invalid_float_string(self):
        result = convert.str_to_float("abc")
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
