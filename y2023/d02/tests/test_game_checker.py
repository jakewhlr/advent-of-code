import unittest
from dice_game import find_color_max, find_color_min, game_is_possible

class TestGameChecker(unittest.TestCase):
    def test_find_color_max(self):
        self.assertEqual(find_color_max("3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"), {"blue": 6, "red": 4, "green": 2})
        self.assertEqual(find_color_max("1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"), {"blue": 4, "green": 3, "red": 1})

    def test_game_is_possible(self):
        self.assertTrue(game_is_possible("3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", {"red": 12, "green": 13, "blue": 14}))
        self.assertFalse(game_is_possible("8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", {"red": 12, "green": 13, "blue": 14}))

if __name__ == '__main__':
    unittest.main()






