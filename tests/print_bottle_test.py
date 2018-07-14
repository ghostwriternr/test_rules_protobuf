import unittest
from src.py_health import health

class PrintBottleTest(unittest.TestCase):

    def testString(self):
        self.assertEqual(health.print_bottle('Ahoy!'), '\n\x05Ahoy!')

if __name__ == '__main__':
    unittest.main(verbosity=2)
