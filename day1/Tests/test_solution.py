import unittest
from day1.Solution import Solution

class test_day_1_solution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution("test_input.txt")
        self.solution.get_all_elves()

    def test_task_1(self):
        with open("task_1_expected_output.txt") as expected_output:
            expected_output = int(expected_output.readline().strip())
        actual_output = self.solution.get_highest_calorie_elves(1)[0].get_total_calories()
        self.assertEqual(expected_output, actual_output)

    def test_task_2(self):
        with open("task_2_expected_output.txt") as expected_output:
            expected_output = int(expected_output.readline().strip())
        actual_output = Solution.get_calories_of_elves(self.solution.get_highest_calorie_elves(3))
        self.assertEqual(expected_output, actual_output)

if __name__ == '__main__':
    unittest.main()
