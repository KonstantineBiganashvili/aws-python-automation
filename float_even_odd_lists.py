import argparse
import re

def extract_values(input_string):
    float_values = re.findall(r'\d+\.\d+', input_string)
    
    integers = re.findall(r'\d+', input_string)
    odd_list = []
    even_list = []
    for num in integers:
        if int(num) % 2 == 0:
            even_list.append(int(num))
        else:
            odd_list.append(int(num))
    
    return [float(value) for value in float_values], odd_list, even_list

def main():
    parser = argparse.ArgumentParser(description='Extract values from input string')
    parser.add_argument('input_string', type=str, help='Input string to extract values from')
    args = parser.parse_args()

    float_values, odd_list, even_list = extract_values(args.input_string)

    print(f'Extracted Float Values: {float_values}')
    print(f'Odd List: {odd_list}')
    print(f'Even List: {even_list}')

if __name__ == "__main__":
    main()
