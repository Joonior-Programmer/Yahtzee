from unittest import TestCase
from yahtzee import menu_before_roll_dice
from unittest.mock import patch
import io


class TestMenuBeforeRollDice(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['1'])
    def test_menu_before_roll_dice_1(self, mock_input, mock_output):
        expected = '1'
        expected2 = 'Start to roll dice!'
        actual = menu_before_roll_dice()
        self.assertEqual(expected, actual)
        self.assertEqual(expected2, mock_output.getValue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['Q'])
    def test_menu_before_roll_dice_Q(self, mock_input, mock_output):
        expected = False
        expected2 = 'Quit program! Bye!'
        actual = menu_before_roll_dice()
        self.assertEqual(expected, actual)
        self.assertEqual(expected2, mock_output.getValue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['2'])
    def test_menu_before_roll_dice_wrong_number(self, mock_input, mock_output):
        expected = 'Please write right numbers or Q'
        menu_before_roll_dice()
        self.assertEqual(expected, mock_output.getValue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['w'])
    def test_menu_before_roll_dice_wrong_letter(self, mock_input, mock_output):
        expected = 'Please write right numbers or Q'
        menu_before_roll_dice()
        self.assertEqual(expected, mock_output.getValue())
