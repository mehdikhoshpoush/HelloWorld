import unittest
from app import hello_world

class TestApp(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "Compose Edited Hello World!")

if __name__ == "__main__":
    unittest.main()

