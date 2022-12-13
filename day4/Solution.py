from typing import Tuple, List, IO


class Pair:
    def __init__(self, first_assignment: Tuple[int, int], second_assignment: Tuple[int, int]):
        self.first_assignment: Tuple[int, int] = first_assignment
        self.second_assignment: Tuple[int, int] = second_assignment

    def find_overlap(self) -> Tuple[int, int]:
        pass


class Solution:
    def __init__(self):
        self.pair_list: List[Pair] = []

    def get_all_pairs_from_file(self, file: IO) -> None:
        for line in file:
            line = line.split(',')
            assignments = []
            for item in line:
                temp = item.split('-')
                assignments.append((int(temp[0]), int(temp[1])))
            self.pair_list.append(Pair(assignments[0], assignments[1]))

    def get_all_pairs_from_data(self, data: Tuple[str, ...]) -> None:
        for item in data:
            item = item.split(',')
            assignments = []
            for item in line:
                temp = item.split('-')
                assignments.append((int(temp[0]), int(temp[1])))
            self.pair_list.append(Pair(assignments[0], assignments[1]))

    def find_all_overlaps(self) -> int:
        pass
