import argparse

def is_armstrong(num):
    num_str = str(num)
    power = len(num_str)
    return num == sum(int(digit) ** power for digit in num_str)

def recursive_sum(numbers, index = 0):
    if index == len(numbers):
        return 0
    return numbers[index] + recursive_sum(numbers, index + 1)

def find_armstrong_numbers(start, end):
    return [num for num in range(start, end + 1) if is_armstrong(num)]

def main():
    parser = argparse.ArgumentParser(description="Find Armstrong numbers and calculate their sum")
    parser.add_argument("start", type=int, help="Start of the range")
    parser.add_argument("end", type=int, help="End of the range")
    args = parser.parse_args()

    armstrong_numbers = find_armstrong_numbers(args.start, args.end)
    armstrong_sum = recursive_sum(armstrong_numbers)
    
    print(f"Armstrong numbers between {args.start} and {args.end}:")
    for armstrong_num in armstrong_numbers:
        print(armstrong_num)
    print("\nSum of Armstrong numbers calculated recursively:", armstrong_sum)

if __name__ == "__main__":
    main()
