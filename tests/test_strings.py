import unittest
from blackleg import strings


class TestStrings(unittest.TestCase):

    def test_empty(self):
        self.assertTrue(strings.empty(None))
        self.assertTrue(strings.empty(""))
        self.assertFalse(strings.empty("  "))
        self.assertFalse(strings.empty("Not Empty"))


if __name__ == '__main__':
    unittest.main()
