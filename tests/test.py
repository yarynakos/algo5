import unittest

from src.main import read_and_write


class Test(unittest.TestCase):
    def test_find_min_depth(self):
        read_and_write('career.in', 'career.out')
        with open('career.out', 'r') as file:
            lines = file.readlines()
            result = int(lines[0].strip())
            self.assertEqual(12, result)

        read_and_write('career1.in', 'career1.out')
        with open('career1.out', 'r') as file:
            lines = file.readlines()
            result = int(lines[0].strip())
            self.assertEqual(9999, result)

        read_and_write('career2.in', 'career2.out')
        with open('career2.out', 'r') as file:
            lines = file.readlines()
            result = int(lines[0].strip())
            self.assertEqual(3, result)
