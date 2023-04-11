from parameterized import parameterized, parameterized_class
import unittest
from palindrome import palindromeit, palindromerec
class Mytest(unittest.TestCase):
    @parameterized.expand([
        ("neuquen",True),
        ("ama",True),
        ("radar",True)

    ])
    def test(self, palabra, boo):
        self.assertEqual(palindromeit(palabra),boo)

class Mytest(unittest.TestCase):
    @parameterized.expand([
        ("neuquen",True),
        ("ama",True),
        ("radar",True)

    ])
    def test(self, palabra, boo):
        self.assertEqual(palindromerec(palabra),boo)

if __name__ == '__main__':
    unittest.main()