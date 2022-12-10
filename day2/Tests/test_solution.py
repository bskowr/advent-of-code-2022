import unittest
from day2.Solution import Solution

class test_day_2_solution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution("test_input.txt")

    def test_task_1(self):
        with open("task_1_expected_output.txt") as expected_output:
            expected_output = int(expected_output.readline().strip())
        self.solution.load_rounds_with_moves()
        actual_output = self.solution.get_final_result()
        self.assertEqual(expected_output, actual_output)

    def test_task_2(self):
        with open("task_2_expected_output.txt") as expected_output:
            expected_output = int(expected_output.readline().strip())
        self.solution.load_rounds_with_results()
        actual_output = self.solution.get_final_result()
        self.assertEqual(expected_output, actual_output)

if __name__ == '__main__':
    unittest.main()
