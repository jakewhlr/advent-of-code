def find_color_max(game_string: str) -> dict:
    max_colors = {}
    pulls = game_string.split(';')
    for pull in pulls:
        colors = pull.strip().split(', ')
        for color in colors:
            parsed_color = color.split(' ')
            number = int(parsed_color[0])
            color = parsed_color[1]
            if color not in max_colors.keys():
                max_colors[color] = number
            else:
                if number > max_colors[color]:
                    max_colors[color] = number
    return max_colors

def game_is_possible(game_string: str, dice_totals: dict) -> bool:
    max_colors = find_color_max(game_string)
    for color, number in max_colors.items():
        if number > dice_totals[color]:
            return False
    return True

def parse_games(game_strings: list[str]) -> list[str]:
    game_list = [line.split(': ')[1].strip() for line in game_strings]
    return game_list

def check_games(games_list: list[str], dice_totals: dict) -> int:
    total = 0
    for id, game in enumerate(games_list):
        if game_is_possible(game, dice_totals):
            total += id+1
    return total