class Scratchcard:
    winning_numbers: list[int]
    revealed_numbers: list[int]
    score: int

    def __init__(self, winning_numbers: list[int], revealed_numbers: list[int]):
        self.winning_numbers = winning_numbers
        self.revealed_numbers = revealed_numbers
        self.score = 0
    
    def check_winning_numbers(self) -> list[int]:
        matches = [number for number in self.revealed_numbers if number in self.winning_numbers]
        return matches

    def calculate_score(self) -> int:
        matches = self.check_winning_numbers()
        return 2**(len(matches)-1) if matches  else 0

class ScratchcardPile:
    def __init__(self, input_string: str):
        self.scratchcards: list[Scratchcard] = self._parse_input_string(input_string)

    def _parse_input_string(self, input_lines: str):
        cards_list: list[Scratchcard] = []
        for line in input_lines.split('\n'):
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

    def generate_copies(self):
        # TODO recursive function to get the count of matching numbers, multiplied by the count of
        # numbers underneath it. If 0, return 1 (the card itself)
        index = 0
        while index < len(self.scratchcards):
            winning_numbers_count = len(self.scratchcards[index].check_winning_numbers) 
            index += 1
