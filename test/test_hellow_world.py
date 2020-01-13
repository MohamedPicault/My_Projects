import unittest
from main_source import Hello_World


class MyTestCase(unittest.TestCase):
    def test_message(self):
        self.assertEqual('Hello!', Hello_World.message())


if __name__ == '__main__':
    unittest.main()
