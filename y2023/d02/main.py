#!/usr/bin/env python3

from dice_game import parse_games, check_games, find_color_max, find_cube_power


def part_one():
    with open('data/input') as f:
        lines = f.read()
    games_list = parse_games(lines.split('\n'))
    return check_games(games_list, {"red": 12, "green": 13, "blue": 14})

def part_two():
    with open('data/input') as f:
        lines = f.read()
    games_list = parse_games(lines.split('\n'))
    sum = 0
    for game in games_list:
        sum += find_cube_power(find_color_max(game))
    return sum

def main():
    print(f"Part 01: {part_one()}")
    print(f"Part 02: {part_two()}")

if __name__ == '__main__':
    main()