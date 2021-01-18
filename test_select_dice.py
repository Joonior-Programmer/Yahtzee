from unittest import TestCase
from yahtzee import select_dice
from unittest.mock import patch


class TestSelectDice(TestCase):
    @patch('builtins.input', side_effect=['1'])
    def test_select_dice_select_one(self, mock_input):
        dice = ['3', '5', '5', '5', '5']
        expected = ['*3', '5', '5', '5', '5']
        actual = select_dice(dice)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['1'])
    def test_select_dice_select_cancel_one(self, mock_input):
        dice = ['*3', '5', '5', '5', '5']
        expected = ['3', '5', '5', '5', '5']
        actual = select_dice(dice)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['2'])
    def test_select_dice_select_two(self, mock_input):
        dice = ['3', '5', '5', '5', '5']
        expected = ['3', '*5', '5', '5', '5']
        actual = select_dice(dice)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['2'])
    def test_select_dice_select_cancel_two(self, mock_input):
        dice = ['3', '*5', '5', '5', '5']
        expected = ['3', '5', '5', '5', '5']
        actual = select_dice(dice)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['3'])
    def test_select_dice_select_three(self, mock_input):
        dice = ['3', '5', '*5', '5', '5']
        expected = ['3', '5', '5', '5', '5']
        actual = select_dice(dice)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['3'])
    def test_select_dice_select_cancel_three(self, mock_input):
        dice = ['3', '5', '*5', '5', '5']
        expected = ['3', '5', '5', '5', '5']
        actual = select_dice(dice)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['4'])
    def test_select_dice_select_four(self, mock_input):
        dice = ['3', '5', '5', '*5', '5']
        expected = ['3', '5', '5', '5', '5']
        actual = select_dice(dice)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['4'])
    def test_select_dice_select_cancel_four(self, mock_input):
        dice = ['3', '5', '5', '*5', '5']
        expected = ['3', '5', '5', '5', '5']
        actual = select_dice(dice)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['5'])
    def test_select_dice_select_five(self, mock_input):
        dice = ['3', '5', '5', '5', '5']
        expected = ['3', '5', '5', '5', '*5']
        actual = select_dice(dice)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['5'])
    def test_select_dice_select_cancel_five(self, mock_input):
        dice = ['3', '5', '5', '5', '*5']
        expected = ['3', '5', '5', '5', '5']
        actual = select_dice(dice)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['1'])
    def test_select_dice_select_multiple(self, mock_input):
        dice = ['3', '5', '*5', '*5', '5']
        expected = ['*3', '5', '*5', '*5', '5']
        actual = select_dice(dice)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['1'])
    def test_select_dice_select_cancel_multiple(self, mock_input):
        dice = ['*3', '5', '5', '*5', '*5']
        expected = ['3', '5', '5', '*5', '*5']
        actual = select_dice(dice)
        self.assertEqual(expected, actual)