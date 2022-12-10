import unittest
from day3.Solution import Solution

class test_day_3_solution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution("test_input.txt")

    def test_task_1(self):
        with open("task_1_expected_output.txt") as expected_output:
            expected_output = int(expected_output.readline().strip())
        self.solution.load_all_rucksacks()
        actual_output = self.solution.calculate_total_priority()
        self.assertEqual(expected_output, actual_output)

if __name__ == '__main__':
    unittest.main()
