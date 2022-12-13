import unittest
from day5.Solution import Solution, CrateStack, Instruction


class test_day_5_solution(unittest.TestCase):
    def setUp(self) -> None:
        self.cratestack = CrateStack([
            'A',
            'B',
            'C',
            'D',
            'E'
        ])
        self.solution = Solution()
        self.solution.stack_list = {
            1: CrateStack(['A', 'B', 'C']),
            2: CrateStack(['D', 'E']),
            3: CrateStack(['F']),
            4: CrateStack(),
            5: CrateStack(['G', 'H', 'I', 'J', 'K', 'L']),
        }
        self.solution.procedure = [
            Instruction(1, 3, 2),
            Instruction(5, 5, 4),
            Instruction(1, 1, 1),
            Instruction(2, 2, 1)
        ]

        # Solution after instructions
        # 1 ['A', 'B', 'C', 'F', 'E']
        # 2 ['D']
        # 3 []
        # 4 ['L', 'K', 'J', 'I', 'H']
        # 5 ['G']

    def test_pickup_top(self):
        picked_crate = self.cratestack.pickup_top()
        self.assertEqual('E', picked_crate)
        self.assertEqual(['A', 'B', 'C', 'D'], self.cratestack.crate_stack)

    def test_place_new(self):
        self.cratestack.place_new('F')
        self.assertIn('F', self.cratestack.crate_stack)
        self.assertEqual(['A', 'B', 'C', 'D', 'E', 'F'], self.cratestack.crate_stack)

    def test_move_crates_one_box(self):
        instruction = self.solution.procedure[0]
        self.solution.move_crates(instruction.source, instruction.target, instruction.amount)
        self.assertEqual(['D', 'E', 'F'], self.solution.stack_list[2].crate_stack)

    def test_move_crates_many_boxes(self):
        instruction = self.solution.procedure[1]
        self.solution.move_crates(instruction.source, instruction.target, instruction.amount)
        self.assertEqual(['L', 'K', 'J', 'I', 'H'], self.solution.stack_list[4].crate_stack)
        self.assertEqual(['G'], self.solution.stack_list[5].crate_stack)

    def test_move_crates_saved_instructions(self):
        for instruction in self.solution.procedure:
            self.solution.move_crates(instruction.source, instruction.target, instruction.amount)
        self.assertEqual(['A', 'B', 'C', 'F', 'E'], self.solution.stack_list[1].crate_stack)
        self.assertEqual(['D'], self.solution.stack_list[2].crate_stack)
        self.assertEqual([], self.solution.stack_list[3].crate_stack)
        self.assertEqual(['L', 'K', 'J', 'I', 'H'], self.solution.stack_list[4].crate_stack)
        self.assertEqual(['G'], self.solution.stack_list[5].crate_stack)

    def test_get_top_crates_from_stack(self):
        self.assertEqual(['E'], self.cratestack.get_top_crates())
        self.assertEqual(['D', 'E'], self.cratestack.get_top_crates(2))

    def test_get_top_crates_from_all_stacks(self):
        top_crates = self.solution.get_all_top_crates()
        self.assertEqual('CEFL', top_crates)

if __name__ == '__main__':
    unittest.main()
