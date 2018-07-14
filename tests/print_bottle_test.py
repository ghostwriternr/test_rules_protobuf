import unittest

class PrintBottleTest(unittest.TestCase):
    def check_string(self):
        self.assertEqual(print_bottle('Ahoy!'), 'Ahoy!')

if __name__ == '__main__':
    unittest.main()
