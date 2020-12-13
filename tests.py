import unittest

class test_sample(unittest.TestCase):

    def test_sample_1(self):
        expected_result = 6

        self.assertEqual(expected_result, 6)

    def test_sample_2(self):
        expected_result = 6

        self.assertNotEqual(expected_result, 4)

    def test_sample_3(self):
        expected_result = False
        self.assertFalse(expected_result)