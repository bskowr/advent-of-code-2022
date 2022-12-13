from typing import List, Dict


class CrateStack:
    def __init__(self, crate_stack: List[chr] = None):
        if crate_stack is None:
            self.crate_stack: List[chr] = []
        else:
            self.crate_stack: List[chr] = crate_stack

    def place_new(self, crate: chr) -> None:
        self.crate_stack.append(crate)

    def pickup_top(self) -> chr:
        return self.crate_stack.pop()

    def get_top_crates(self, amount: int = 1) -> List[chr]:
        return self.crate_stack[amount * -1:]


class Instruction:
    INSTRUCTION_TYPES = {
        'move': 0
    }

    def __init__(self, amount: int, source: int, target: int, instruction_type: str = 'move'):
        self.amount = amount
        self.source = source
        self.target = target
        self.instruction_type = Instruction.INSTRUCTION_TYPES[instruction_type]


class Solution:
    def __init__(self, input_file: str = 'input.txt'):
        self.input_file: str = input_file
        self.stack_list: Dict[int, CrateStack] = {}
        self.procedure: List[Instruction] = []

    def load_stack_data(self) -> None:
        self.stack_list.clear()
        input_data: List[str] = []
        with open(self.input_file) as data:
            for line in data:
                if line == '\n':
                    break
                if line.find('[') != -1:
                    input_data.append(line)
                else:
                    for number in line.strip().split():
                        self.stack_list[int(number)] = CrateStack()
        for i in range(1, len(input_data) + 1):
            self.stack_list[i] = CrateStack()
        for line in reversed(input_data):
            i = 0
            while i < len(line):
                if line[i] == '[' and line[i + 2] == ']':
                    stack_number = i // 4 + 1
                    crate = line[i + 1]
                    self.stack_list[stack_number].place_new(crate)
                i += 4

    def load_procedure(self) -> None:
        self.procedure: List[Instruction] = []
        with open(self.input_file) as data:
            instructions_started = False
            for line in data:
                if instructions_started:
                    instruction_type, amount, _, source, _, target = line.strip().split()
                    amount = int(amount)
                    source = int(source)
                    target = int(target)
                    self.procedure.append(Instruction(amount, source, target, instruction_type))
                elif line == '\n':
                    instructions_started = True

    def load_all_data(self) -> None:
        self.load_stack_data()
        self.load_procedure()

    def move_crates(self, source: int, target: int, amount: int = 1) -> None:
        while amount > 0:
            moved_crate = self.stack_list[source].pickup_top()
            self.stack_list[target].place_new(moved_crate)
            amount -= 1

    def execute_procedure(self) -> None:
        for instruction in self.procedure:
            self.move_crates(instruction.source, instruction.target, instruction.amount)

    def get_all_top_crates(self) -> str:
        all_top_crates: str = ''
        for stack in self.stack_list:
            stack_top_crates = ''.join(self.stack_list[stack].get_top_crates())
            all_top_crates += stack_top_crates
        return all_top_crates

    def solve(self) -> dict:
        self.load_all_data()
        self.execute_procedure()
        answers = {
            "Task 1": self.get_all_top_crates(),
            "Task 2": ''
        }
        return answers
