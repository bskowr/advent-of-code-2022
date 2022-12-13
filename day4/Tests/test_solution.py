import unittest
from typing import Tuple

from day4.Solution import Pair


class test_day_4_solution(unittest.TestCase):
    def test_find_overlap(self, expected_output: Tuple[int, int] = None, test_pair: Pair = None):
        if expected_output is None or test_pair is None:
            expected_output = (4, 7)
            test_pair = Pair(
                first_assignment=(1, 7),
                second_assignment=(4, 20)
            )
        self.assertEqual(expected_output, test_pair.find_overlap())

    def test_get_all_pairs(self):
        expected_output = [

        ]

    def test_find_all_overlaps(self):
        pass

    def test_task_1_solution(self):
        pass

if __name__ == '__main__':
    unittest.main()
