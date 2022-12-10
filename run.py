from day3.Solution import Solution as Day3Solution

if __name__ == '__main__':
    print('-*-' * 25)
    print('Day 3')
    for key, value in Day3Solution("day3/input.txt").solve().items():
        print(f"{key}: {value}")