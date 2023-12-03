#!/usr/bin/env python3

from gear_ratios import parse_schematic_string, find_part_numbers, condense_numbers

example_string = """467..114..
                    ...*......
                    ..35..633.
                    ......#...
                    617*......
                    .....+.58.
                    ..592.....
                    ......755.
                    ...$.*....
                    .664.598.."""

def part_one():
    with open('data/input') as f:
        lines = f.read()
    return (sum(find_part_numbers(parse_schematic_string(lines))))

def part_two():
    with open('data/input') as f:
        lines = f.read()
    return 0 

def main():
    print(f"Part 01: {part_one()}")
    print(f"Part 02: {part_two()}")

if __name__ == '__main__':
    main()