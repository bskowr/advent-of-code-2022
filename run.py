from day1.Solution import Solution as Day1Solution
from day2.Solution import Solution as Day2Solution
from day3.Solution import Solution as Day3Solution

if __name__ == '__main__':
    print('-*-'*25)
    print('Day 1')
    for key, value in Day1Solution("day1/input.txt").solve().items():
        print(f"{key}: {value}")
    print('-*-' * 25)
    print('Day 2')
    for key, value in Day2Solution("day2/input.txt").solve().items():
        print(f"{key}: {value}")
    print('-*-' * 25)
    print('Day 3')
    for key, value in Day3Solution("day3/input.txt").solve().items():
        print(f"{key}: {value}")