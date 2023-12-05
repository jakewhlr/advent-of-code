#!/usr/bin/env python3

from scratchcards import Scratchcard

def card_parser(card_lines: list[str]) -> list[Scratchcard]:
    cards_list: list[Scratchcard] = []
    for line in card_lines:
        winning_numbers: list[int] = []
        revealed_numbers: list[int] = []
        split_line = line.split(': ')[1].split(' | ')
        for number in split_line[0].split(' '):
            if number.strip().isnumeric():
                winning_numbers.append(int(number))
        for number in split_line[1].split(' '):
            if number.strip().isnumeric():
                revealed_numbers.append(int(number))
        cards_list.append(Scratchcard(winning_numbers, revealed_numbers))
    return cards_list
        

def part_one():
    with open('data/input') as f:
        lines = f.read()
    scratchcards = card_parser(lines.split('\n'))
    total = 0
    for card in scratchcards:
        total += card.calculate_score()
    return total

def part_two():
    with open('data/input') as f:
        lines = f.read()
    return 0

def main():
    print(f"Part 01: {part_one()}")
    print(f"Part 02: {part_two()}")

if __name__ == '__main__':
    main()
