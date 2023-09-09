import unittest

class TestStringMethods(unittest.TestCase):
    # Ini adalah test case pertama (1)
    def test_strip(self):
        self.assertEqual('www.nicsprojects.com'.strip('c.mow'), 'nicsprojects')

    # Test case kedua (2)
    def test_isalnum(self):
        self.assertTrue('n1cs'.isalnum())
        self.assertFalse('n!cs'.isalnum())

    # Test case ketiga (3)
    def test_index(self):
        s = 'nicsprojects'
        self.assertEqual(s.index('nics'), 0)
        # cek s.index gagal ketika tidak ditemukan
        with self.assertRaises(ValueError):
            s.index('decode')


if __name__ == '__main__':
    # Test Runner
    unittest.main()
