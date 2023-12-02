#!/usr/bin/env python3

from calibration_recovery import recover_total_calibration

def part_one():
    """Run with input data w/o support for 'string' numbers"""
    with open('data/input') as f:
        lines = f.read()
    print("Part 01:", recover_total_calibration(lines.split('\n')))

def part_two():
    """Run with input data w/support for 'string' numbers"""
    with open('data/input') as f:
        lines = f.read()
    print("Part 02:", recover_total_calibration(lines.split('\n'), string_support=True))    

def main():
    part_one()
    part_two()

if __name__ == '__main__':
    main()