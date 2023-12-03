def parse_schematic_string(schematic_string: str) -> list[list]:
    return [list(line.strip()) for line in schematic_string.split('\n')]

def find_part_numbers(schematic: list[list]) -> list[int]:
    condensed_schematic = []
    for line in schematic:
        condensed_schematic.append(condense_numbers(line))
    parts = []
    for line_number, line in enumerate(condensed_schematic):
        for index, part in enumerate(line):
            if part.isnumeric():
               for i in range(-1, 2):
                    for j in range(-1, 2):
                        if (line_number+i >= len(condensed_schematic)) or (line_number+i < 0):
                            continue
                        if (index+j >= len(line)) or (index+j < 0):
                            continue
                        if i == j == 0:
                            continue 
                        if condensed_schematic[line_number+i][index+j] == '.':
                            continue
                        if not condensed_schematic[line_number+i][index+j].isalnum():
                            parts.append(int(part))
                            k = 0
                            while condensed_schematic[line_number][index-k].isnumeric():
                                condensed_schematic[line_number][index-k] = '.'
                                k += 1
                                if index - k < 0:
                                    break
                            k = 1
                            while condensed_schematic[line_number][index+k].isnumeric():
                                condensed_schematic[line_number][index+k] = '.'
                                k += 1
                                if index + k >= len(condensed_schematic[line_number]):
                                    break
    return parts

def condense_numbers(schematic_line: list[str]) -> list[str]:
    new_line = []
    line_iter = enumerate(schematic_line)
    number_indexes = []
    for index, item in line_iter:
        if len(number_indexes) > 1:
            number_indexes.pop()
            continue
        number_indexes = []
        if item.isnumeric():
            new_index = index
            digits = []
            while new_index < len(schematic_line):
                if schematic_line[new_index].isnumeric():
                    digits.append(schematic_line[new_index])
                    number_indexes.append(new_index)
                else:
                    break
                new_index += 1
            for i in number_indexes:
                new_line.append(f"{''.join(digits)}")
        else:
            new_line.append(item)
    return new_line
            