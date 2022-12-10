from typing import Tuple, List


class Round:
    MOVE_BEATS = {
        'A': 'Z',
        'B': 'X',
        'C': 'Y',
        'X': 'C',
        'Y': 'A',
        'Z': 'B',
    }

    RESULT_MEANING = {
        'X': -1,
        'Y': 0,
        'Z': 1
    }

    MOVE_POINTS = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }

    RESULT_POINTS = {
        -1: 0,
        0: 3,
        1: 6
    }

    def __init__(self, opponent_move, my_move=None, required_result=None):
        self.opponent_move = opponent_move
        if my_move is not None:
            self.my_move = my_move
            self.check_winner()
        elif required_result is not None:
            self.required_result = Round.RESULT_MEANING[required_result]
            self.deduct_my_move()
        else:
            self.my_move = None
            self.required_result = None

    def check_winner(self) -> None:
        if Round.MOVE_BEATS[self.opponent_move] == self.my_move:
            self.required_result = -1
        elif Round.MOVE_BEATS[self.my_move] == self.opponent_move:
            self.required_result = 1
        else:
            self.required_result = 0

    def deduct_my_move(self) -> None:
        if self.required_result == -1:
            self.my_move = Round.MOVE_BEATS[self.opponent_move]
        elif self.required_result == 1:
            for key in Round.MOVE_BEATS:
                if Round.MOVE_BEATS[key] == self.opponent_move:
                    self.my_move = key
                    break
        else:
            for key in Round.MOVE_BEATS:
                if key in ['A', 'B', 'C']:
                    continue
                if Round.MOVE_BEATS[key] == self.opponent_move:
                    continue
                if Round.MOVE_BEATS[self.opponent_move] == key:
                    continue
                self.my_move = key
                break

    def calculate_points(self) -> int:
        return Round.MOVE_POINTS[self.my_move] + Round.RESULT_POINTS[self.required_result]


class Solution:

    def __init__(self, input_file: str = 'input.txt'):
        self.input_file: str = input_file
        self.round_list: List[Round] = []

    def load_rounds_with_moves(self) -> None:
        self.round_list = []
        with open(self.input_file) as data:
            for line in data:
                opponent_move = line.split(" ")[0].strip()
                my_move = line.split(" ")[1].strip()
                self.round_list.append(Round(opponent_move, my_move=my_move))

    def load_rounds_with_results(self) -> None:
        self.round_list = []
        with open(self.input_file) as data:
            for line in data:
                opponent_move = line.split(" ")[0].strip()
                required_result = line.split(" ")[1].strip()
                self.round_list.append(Round(opponent_move, required_result=required_result))

    def get_final_result(self) -> int:
        total_points = 0
        for game_round in self.round_list:
            total_points += game_round.calculate_points()
        return total_points

    def solve(self) -> dict:
        answers = {}
        self.load_rounds_with_moves()
        answers["Task 1"] = self.get_final_result()
        self.load_rounds_with_results()
        answers["Task 2"] = self.get_final_result()
        return answers
