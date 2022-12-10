from typing import List


class Rucksack:
    def __init__(self, contents: str):
        split_point = int(len(contents) / 2)
        self.first_compartment = contents[:split_point]
        self.second_compartment = contents[split_point:]

    def find_duplicate(self) -> chr:
        for item in self.first_compartment:
            if item in self.second_compartment:
                return item

    @staticmethod
    def calculate_priority(item: chr) -> int:
        priority = 0
        if ord('a') <= ord(item) <= ord('z'):
            priority = ord(item) - ord('a') + 1
        elif ord('A') <= ord(item) <= ord('Z'):
            priority = ord(item) - ord('A') + 26 + 1
        return priority


class Solution:
    def __init__(self, input_file: str = 'input.txt'):
        self.input_file: str = input_file
        self.rucksack_list: List[Rucksack] = []

    def load_all_rucksacks(self) -> None:
        self.rucksack_list = []
        with open(self.input_file) as data:
            for item_list in data:
                self.rucksack_list.append(Rucksack(item_list.strip()))

    def calculate_total_priority(self) -> int:
        total_priority = 0
        for rucksack in self.rucksack_list:
            total_priority += Rucksack.calculate_priority(rucksack.find_duplicate())
        return total_priority

    def solve(self) -> dict:
        answers = {}
        self.load_all_rucksacks()
        answers["Task 1"] = self.calculate_total_priority()
        answers["Task 2"] = ''
        return answers
