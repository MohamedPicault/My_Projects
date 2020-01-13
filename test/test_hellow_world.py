import unittest
from main_source import Hello_World as hello

class MyTestCase(unittest.TestCase):
    def test_message(self):
        self.assertEqual('Hello' , hello.message())


if __name__ == '__main__':
    unittest.main()
