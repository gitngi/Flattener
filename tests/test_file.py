import unittest
from scripts.flattener import Flattener


class TestMyFlatten(unittest.TestCase):
    def test_my_flat_1(self):
        dic = {
            "a": 1,
            "b": 2,
            "c": [{"d": [2, 3, 4], "e": [{"f": 1, "g": 2}]}]}

        expected = {'a': 1,
                    'b': 2,
                    'c.0.d.0': 2,
                    'c.0.d.1': 3,
                    'c.0.d.2': 4,
                    'c.0.e.0.f': 1,
                    'c.0.e.0.g': 2}

        real = Flattener.my_flatten(dic)
        self.assertEqual(real, expected)

    def test_my_flat_2(self):
        dic = {
            "a": 1,
            "b": 2,
            "c": [{"d": [2, 3, 4], "e": [{"f": 1, "g": 2}]}]}

        expected = {'a': 1,
                    'b': 2,
                    'c.d.0': 2,
                    'c.d.1': 3,
                    'c.d.2': 4,
                    'c.e.f': 1,
                    'c.0.e.0.g': 2}

        real = Flattener.my_flatten(dic)
        self.assertNotEqual(real, expected)

    def test_my_flat_3(self):
        dic = {
            "a": 1,
            "b": 4,
            "c": {"d": 3,
                  "e": 'test'
                  }
        }

        expected = {'a': 1,
                    'b': 4,
                    'c.d': 3,
                    'c.e': 'test',
                    }

        real = Flattener.my_flatten(dic)
        self.assertEqual(real, expected)


if __name__ == '__main__':
    unittest.main()
