from unittest import TestCase
from yahtzee import roll_dice
from unittest.mock import patch
import io


class TestRollDice(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.choices', return_value=['1', '2', '3', '4', '5'])
    def test_roll_dice_new(self, mock_input, mock_output):
        expected = ['1', '2', '3', '4', '5']
        expected2 = 'Your Dice : 1 2 3 4 5\n'
        actual = roll_dice()
        self.assertEqual(expected, actual)
        self.assertEqual(expected2, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.int', side_effect=['1', '2', '4', '5'])
    def test_roll_dice_saved_dice_one(self, mock_input, mock_output):
        dice = ['1', '2', '3', '*4', '5']
        expected = ['1', '2', '4', '4', '5']
        expected2 = 'Your Dice : 1 2 4 4 5\n'
        actual = roll_dice(dice)
        self.assertEqual(expected, actual)
        self.assertEqual(expected2, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.int', side_effect=['1', '2', '3'])
    def test_roll_dice_saved_dice_two(self, mock_input, mock_output):
        dice = ['2', '3', '*4', '*4', '5']
        expected = ['1', '2', '4', '4', '3']
        expected2 = 'Your Dice : 1 2 4 4 3\n'
        actual = roll_dice(dice)
        self.assertEqual(expected, actual)
        self.assertEqual(expected2, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.int', side_effect=['1', '5'])
    def test_roll_dice_saved_dice_three(self, mock_input, mock_output):
        dice = ['4', '*2', '*3', '*4', '3']
        expected = ['1', '2', '3', '4', '5']
        expected2 = 'Your Dice : 1 2 4 4 5\n'
        actual = roll_dice(dice)
        self.assertEqual(expected, actual)
        self.assertEqual(expected2, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.int', return_value='5')
    def test_roll_dice_saved_dice_four(self, mock_input, mock_output):
        dice = ['*1', '*2', '*3', '*4', '6']
        expected = ['1', '2', '3', '4', '5']
        expected2 = 'Your Dice : 1 2 3 4 5\n'
        actual = roll_dice(dice)
        self.assertEqual(expected, actual)
        self.assertEqual(expected2, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.choices', side_effect=['6', '6', '6', '6', '6'])
    def test_roll_dice_all_change(self, mock_input, mock_output):
        dice = ['1', '2', '3', '4', '6']
        expected = ['6', '6', '6', '6', '6']
        expected2 = 'Your Dice : 6 6 6 6 6\n'
        actual = roll_dice(dice)
        self.assertEqual(expected, actual)
        self.assertEqual(expected2, mock_output.getvalue())

