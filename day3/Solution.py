from typing import List


class Rucksack:
    def __init__(self, contents: str):
        split_point = int(len(contents) / 2)
        self.first_compartment = contents[:split_point]
        self.second_compartment = contents[split_point:]

    def get_all_contents(self) -> str:
        return self.first_compartment + self.second_compartment

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

    @staticmethod
    def find_badge(rucksacks: List[Rucksack]) -> chr:
        source_rucksack = rucksacks.pop()
        for item in source_rucksack.get_all_contents():
            is_badge = True
            for rucksack in rucksacks:
                if item not in rucksack.get_all_contents():
                    is_badge = False
                    break
            if is_badge:
                return item
        return None

    def make_groups(self) -> List[List[Rucksack]]:
        groups = []
        for i in range(0, len(self.rucksack_list) - 2, 3):
            group = [
                self.rucksack_list[i],
                self.rucksack_list[i+1],
                self.rucksack_list[i+2],
            ]
            groups.append(group)
        return groups

    def find_all_badges(self) -> List[chr]:
        badge_list = []
        groups = self.make_groups()
        for group in groups:
            badge_list.append(self.find_badge(group))
        return badge_list

    def load_all_rucksacks(self) -> None:
        self.rucksack_list = []
        with open(self.input_file) as data:
            for item_list in data:
                self.rucksack_list.append(Rucksack(item_list.strip()))

    @staticmethod
    def calculate_priority_of_duplicates(rucksack_list: List[Rucksack]) -> int:
        total_priority = 0
        for rucksack in rucksack_list:
            total_priority += Rucksack.calculate_priority(rucksack.find_duplicate())
        return total_priority

    @staticmethod
    def calculate_priority_of_badges(badge_list: List[chr]) -> int:
        total_priority = 0
        for badge in badge_list:
            total_priority += Rucksack.calculate_priority(badge)
        return total_priority

    def solve(self) -> dict:
        answers = {}
        self.load_all_rucksacks()
        answers["Task 1"] = Solution.calculate_priority_of_duplicates(self.rucksack_list)
        answers["Task 2"] = Solution.calculate_priority_of_badges(self.find_all_badges())
        return answers
