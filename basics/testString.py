import unittest

class StringTest(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO', 'FOO is upper of foo')
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        string = 'test split'
        self.assertEqual(string.split(), ['test', 'split'])
        with self.assertRaises(TypeError):
            string.split(2)

if __name__ == '__main__':
    unittest.main()

