from unittest import TestCase
from yahtzee import menu_after_roll_dice
from unittest.mock import patch
import io


class TestMenuAfterRollDice(TestCase):
    @patch('builtins.input', side_effect=['1'])
    def test_menu_after_roll_dice_1(self, mock_input):
        expected = 1
        actual = menu_after_roll_dice()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['2'])
    def test_menu_after_roll_dice_2(self, mock_input):
        expected = 2
        actual = menu_after_roll_dice()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['3'])
    def test_menu_after_roll_dice_3(self, mock_input):
        expected = 3
        actual = menu_after_roll_dice()
        self.assertEqual(expected, actual)
