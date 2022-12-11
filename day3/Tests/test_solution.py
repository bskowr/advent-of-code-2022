import unittest
from day3.Solution import Solution, Rucksack


class test_day_3_solution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution("test_input.txt")
        self.solution.load_all_rucksacks()

    def test_task_1(self):
        with open("task_1_expected_output.txt") as expected_output:
            expected_output = int(expected_output.readline().strip())
        actual_output = self.solution.calculate_priority_of_duplicates(self.solution.rucksack_list)
        self.assertEqual(expected_output, actual_output)

    def test_task_2(self):
        with open("task_2_expected_output.txt") as expected_output:
            expected_output = int(expected_output.readline().strip())
        actual_output = self.solution.calculate_priority_of_badges(self.solution.find_all_badges())
        self.assertEqual(expected_output, actual_output)

    def test_find_badge(self):
        rucksack_list = [
            self.solution.rucksack_list[0],
            self.solution.rucksack_list[1],
            self.solution.rucksack_list[2],
        ]
        badge = self.solution.find_badge(rucksack_list)
        self.assertEqual('r', badge)
        rucksack_list = [
            self.solution.rucksack_list[3],
            self.solution.rucksack_list[4],
            self.solution.rucksack_list[5],
        ]
        badge = self.solution.find_badge(rucksack_list)
        self.assertEqual('Z', badge)

    def test_calculate_priority(self):
        priority = Rucksack.calculate_priority('Z')
        self.assertEqual(52, priority)
        priority = Rucksack.calculate_priority('r')
        self.assertEqual(18, priority)

    def test_make_groups(self):
        expected_groups = [
            [
                self.solution.rucksack_list[0],
                self.solution.rucksack_list[1],
                self.solution.rucksack_list[2],
            ],
            [
                self.solution.rucksack_list[3],
                self.solution.rucksack_list[4],
                self.solution.rucksack_list[5],
            ]
        ]
        found_groups = self.solution.make_groups()
        self.assertEqual(expected_groups, found_groups)

if __name__ == '__main__':
    unittest.main()
