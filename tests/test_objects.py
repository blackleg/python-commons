import unittest
from blackleg import objects


class TestStrings(unittest.TestCase):

    def test_empty(self):
        self.assertTrue(objects.isnull(None))
        self.assertFalse(objects.isnull(self))


if __name__ == '__main__':
    unittest.main()
