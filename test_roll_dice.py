from unittest import TestCase
from yahtzee import roll_dice
from unittest.mock import patch


class TestRollDice(TestCase):
    @patch('random.sample', side_effect=[1, 2, 3, 4, 5])
    def test_roll_dice_new(self):
        expected = ['1', '2', '3', '4', '5']
        actual = roll_dice()
        self.assertEqual(expected, actual)

    @patch('random.int', side_effect=[1, 2, 4, 5])
    def test_roll_dice_saved_dice_one(self):
        dice = ['1', '2', '3', '*4', '5']
        expected = ['1', '2', '4', '4', '5']
        actual = roll_dice(dice)
        self.assertEqual(expected, actual)

    @patch('random.sample', side_effect=[1, 2, 3])
    def test_roll_dice_saved_dice_two(self):
        dice = ['2', '3', '*4', '*4', '5']
        expected = ['1', '2', '4', '4', '3']
        actual = roll_dice(dice)
        self.assertEqual(expected, actual)

    @patch('random.sample', side_effect=[1, 5])
    def test_roll_dice_saved_dice_three(self):
        dice = ['4', '*2', '*3', '*4', '3']
        expected = ['1', '2', '3', '4', '5']
        actual = roll_dice(dice)
        self.assertEqual(expected, actual)

    @patch('random.sample', side_effect=[6])
    def test_roll_dice_saved_dice_four(self):
        dice = ['*1', '*2', '*3', '*4', '6']
        expected = ['1', '2', '3', '4', '5']
        actual = roll_dice(dice)
        self.assertEqual(expected, actual)

    @patch('random.sample', side_effect=[6, 6, 6, 6, 6])
    def test_roll_dice_all_change(self):
        dice = ['1', '2', '3', '4', '6']
        expected = ['6', '6', '6', '6', '6']
        actual = roll_dice(dice)
        self.assertEqual(expected, actual)

