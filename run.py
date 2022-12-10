from day2.Solution import Solution as Day2Solution

if __name__ == '__main__':
    print('-*-' * 25)
    print('Day 2')
    for key, value in Day2Solution("day2/input.txt").solve().items():
        print(f"{key}: {value}")