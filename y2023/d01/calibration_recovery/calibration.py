NUMBER_STRINGS = (
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
)

def recover_calibration_value(new_calibration_string: str, string_support: bool = False):
    string_prefixes = NUMBER_STRINGS if string_support else ()
    first_digit = _find_first_number_recursive(new_calibration_string, string_prefixes)
    last_digit = _find_first_number_recursive(new_calibration_string[::-1], [x[::-1] for x in string_prefixes])

    digits = int(f"{first_digit}{last_digit}")
    return digits

def recover_total_calibration(calibration_values: list[str], string_support: bool = False) -> int:
    total = 0
    for line in calibration_values:
        calibration_value = recover_calibration_value(line, string_support) 
        total += calibration_value
    return total

def _find_first_number_recursive(calibration_substring: str, number_strings: list[str]) -> int:
    if(len(calibration_substring) == 0):
        return 0
    elif calibration_substring[0].isnumeric():
        return int(calibration_substring[0])
    numeric_prefix = _find_prefix(calibration_substring, number_strings)
    if numeric_prefix:
        return numeric_prefix
    return(_find_first_number_recursive(calibration_substring[1:], number_strings))
    
def _find_prefix(input_string: str, prefixes: list[str]) -> int:
    for index, prefix in enumerate(prefixes):
        if input_string.startswith(prefix):
            return index+1
    return None
