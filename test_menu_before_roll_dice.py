from unittest import TestCase
from yahtzee import menu_before_roll_dice
from unittest.mock import patch
import io


class TestMenuBeforeRollDice(TestCase):
    @patch('builtins.input', side_effect=['1'])
    def test_menu_before_roll_dice_1(self, mock_input):
        expected = 1
        actual = menu_before_roll_dice()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['Q'])
    def test_menu_before_roll_dice_Q(self, mock_input):
        expected = False
        expected2 = 'Quit program! Bye!'
        actual = menu_before_roll_dice()
        self.assertEqual(expected, actual)