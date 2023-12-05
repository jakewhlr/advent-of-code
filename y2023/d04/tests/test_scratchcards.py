import unittest
from scratchcards import *

class TestScratchcards(unittest.TestCase):
    def setUp(self):
        self.scratchcards = [
            Scratchcard([48, 83, 86, 17], [83, 86, 6, 31, 17, 9, 48, 53]),
            Scratchcard([13, 32, 20, 16, 61], [61, 30, 68, 82, 17, 32, 24, 19]),
            Scratchcard([1, 21, 53, 59, 44], [69, 82, 63, 72, 16, 21, 14, 1]),
            Scratchcard([41, 92, 73, 84, 69], [59, 84, 76, 51, 58, 5, 54, 83]),
            Scratchcard([87, 83, 26, 28, 32], [88, 30, 70, 12, 93, 22, 82, 36]),
            Scratchcard([31, 18, 13, 56, 72], [74, 77, 10, 23, 35, 67, 36, 11])
        ]

    def test_calculate_score(self):
        self.assertEqual(self.scratchcards[0].calculate_score(), 8)
        self.assertEqual(self.scratchcards[1].calculate_score(), 2)
        self.assertEqual(self.scratchcards[2].calculate_score(), 2)
        self.assertEqual(self.scratchcards[3].calculate_score(), 1)
        self.assertEqual(self.scratchcards[4].calculate_score(), 0)
        self.assertEqual(self.scratchcards[5].calculate_score(), 0)
        self.assertEqual(sum([x.calculate_score() for x in self.scratchcards]), 13)

if __name__ == '__main__':
    unittest.main()
