from day5.Solution import Solution as Day5Solution

if __name__ == '__main__':
    print('-*-' * 25)
    print('Day 5')
    for key, value in Day5Solution("day5/input.txt").solve().items():
        print(f"{key}: {value}")