from day1.Solution import Solution as Day1Solution

if __name__ == '__main__':
    print('-*-'*25)
    print('Day 1')
    for key, value in Day1Solution("day1/input.txt").solve().items():
        print(f"{key}: {value}")