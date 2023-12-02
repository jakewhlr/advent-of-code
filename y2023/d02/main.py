#!/usr/bin/env python3

from dice_game import parse_games, check_games


def part_one():
    with open('data/input') as f:
        lines = f.read()
    games_list = parse_games(lines.split('\n'))
    print(check_games(games_list, {"red": 12, "green": 13, "blue": 14}))

def main():
    part_one()

if __name__ == '__main__':
    main()