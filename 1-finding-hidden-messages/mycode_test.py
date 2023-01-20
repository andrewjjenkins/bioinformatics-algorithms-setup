import mycode
import unittest

class ReverseComplement(unittest.TestCase):
    
    def test_stepik_example(self):
        self.assertEqual(mycode.ReverseComplement('AAAACCCGGT'), 'ACCGGGTTTT')

if __name__ == "__main__":
    unittest.main()
