from typing import List


class Solution:
    class Elf:
        def __init__(self, carried_food: List[int] = None):
            if carried_food is None:
                carried_food = [0]
            self.carried_food = carried_food

        def get_total_calories(self) -> int:
            return sum(self.carried_food)

    def __init__(self, input_file: str = 'input.txt'):
        self.input_file = input_file
        self.elves_list = []

    def get_all_elves(self) -> None:
        with open(self.input_file) as data:
            input_lines = data.readlines()
            input_lines.append('\n')
            food_list = []
            for line in input_lines:
                if line == '\n':
                    self.elves_list.append(Solution.Elf(food_list))
                    food_list = []
                else:
                    food_list.append(int(line.strip()))

    def get_highest_calorie_elves(self, amount: int) -> List[Elf]:
        highest_calorie_elves = []
        for elf in self.elves_list:
            if len(highest_calorie_elves) < amount:
                highest_calorie_elves.append(elf)
            else:
                highest_calorie_elves = Solution.compare_calories(highest_calorie_elves, elf)
        return highest_calorie_elves

    @staticmethod
    def compare_calories(elves_list: List[Elf], new_elf: Elf) -> List[Elf]:
        elves_list = sorted(elves_list, key=lambda elf: elf.get_total_calories())
        for i, listed_elf in enumerate(elves_list):
            if listed_elf.get_total_calories() < new_elf.get_total_calories():
                elves_list[i] = new_elf
                break
        return elves_list

    @staticmethod
    def get_calories_of_elves(elves_list: List[Elf]) -> int:
        total_calories = 0
        for elf in elves_list:
            total_calories += elf.get_total_calories()
        return total_calories

    def solve(self) -> dict:
        self.get_all_elves()
        answers = {"Task 1": self.get_highest_calorie_elves(1)[0].get_total_calories(),
                   "Task 2": Solution.get_calories_of_elves(self.get_highest_calorie_elves(3))}
        return answers
