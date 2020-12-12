from unittest import TestCase
from yahtzee import choose_score_location
from unittest.mock import patch
import io


class TestChooseScoreLocation(TestCase):
    @patch('builtins.input', side_effect=['1'])
    def test_choose_score_location_one(self, mock_input):
        score = {'Name': 'Joon', '1': None, '2': None, '3': None, '4': None,
                     '5': None, '6': None, 'Three of a Kind': None, 'Four of a Kind': None,
                     'Full House': None, 'Small Straight': None, 'Large Straight': None,
                     'Yahtzee': None, 'Chance': None}
        dice = ['3', '3', '3', '3', '3']
        expected = 1
        actual = choose_score_location(score, dice)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['2'])
    def test_choose_score_location_two(self, mock_input):
        score = {'Name': 'Joon', '1': None, '2': None, '3': None, '4': None,
                 '5': None, '6': None, 'Three of a Kind': None, 'Four of a Kind': None,
                 'Full House': None, 'Small Straight': None, 'Large Straight': None,
                 'Yahtzee': None, 'Chance': None}
        dice = ['3', '3', '3', '3', '3']
        expected = 2
        actual = choose_score_location(score, dice)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['3'])
    def test_choose_score_location_three(self, mock_input):
        score = {'Name': 'Joon', '1': None, '2': None, '3': None, '4': None,
                 '5': None, '6': None, 'Three of a Kind': None, 'Four of a Kind': None,
                 'Full House': None, 'Small Straight': None, 'Large Straight': None,
                 'Yahtzee': None, 'Chance': None}
        dice = ['3', '3', '3', '3', '3']
        expected = 3
        actual = choose_score_location(score, dice)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['4'])
    def test_choose_score_location_four(self, mock_input):
        score = {'Name': 'Joon', '1': None, '2': None, '3': None, '4': None,
                 '5': None, '6': None, 'Three of a Kind': None, 'Four of a Kind': None,
                 'Full House': None, 'Small Straight': None, 'Large Straight': None,
                 'Yahtzee': None, 'Chance': None}
        dice = ['3', '3', '3', '3', '3']
        expected = 4
        actual = choose_score_location(score, dice)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['5'])
    def test_choose_score_location_five(self, mock_input):
        score = {'Name': 'Joon', '1': None, '2': None, '3': None, '4': None,
                 '5': None, '6': None, 'Three of a Kind': None, 'Four of a Kind': None,
                 'Full House': None, 'Small Straight': None, 'Large Straight': None,
                 'Yahtzee': None, 'Chance': None}
        dice = ['3', '3', '3', '3', '3']
        expected = 5
        actual = choose_score_location(score, dice)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['6'])
    def test_choose_score_location_six(self, mock_input):
        score = {'Name': 'Joon', '1': None, '2': None, '3': None, '4': None,
                 '5': None, '6': None, 'Three of a Kind': None, 'Four of a Kind': None,
                 'Full House': None, 'Small Straight': None, 'Large Straight': None,
                 'Yahtzee': None, 'Chance': None}
        dice = ['3', '3', '3', '3', '3']
        expected = 6
        actual = choose_score_location(score, dice)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['7'])
    def test_choose_score_location_seven(self, mock_input):
        score = {'Name': 'Joon', '1': None, '2': None, '3': None, '4': None,
                 '5': None, '6': None, 'Three of a Kind': None, 'Four of a Kind': None,
                 'Full House': None, 'Small Straight': None, 'Large Straight': None,
                 'Yahtzee': None, 'Chance': None}
        dice = ['3', '3', '3', '3', '3']
        expected = 7
        actual = choose_score_location(score, dice)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['8'])
    def test_choose_score_location_eight(self, mock_input):
        score = {'Name': 'Joon', '1': None, '2': None, '3': None, '4': None,
                 '5': None, '6': None, 'Three of a Kind': None, 'Four of a Kind': None,
                 'Full House': None, 'Small Straight': None, 'Large Straight': None,
                 'Yahtzee': None, 'Chance': None}
        dice = ['3', '3', '3', '3', '3']
        expected = 8
        actual = choose_score_location(score, dice)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['9'])
    def test_choose_score_location_nine(self, mock_input):
        score = {'Name': 'Joon', '1': None, '2': None, '3': None, '4': None,
                 '5': None, '6': None, 'Three of a Kind': None, 'Four of a Kind': None,
                 'Full House': None, 'Small Straight': None, 'Large Straight': None,
                 'Yahtzee': None, 'Chance': None}
        dice = ['3', '3', '3', '3', '3']
        expected = 9
        actual = choose_score_location(score, dice)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['10'])
    def test_choose_score_location_ten(self, mock_input):
        score = {'Name': 'Joon', '1': None, '2': None, '3': None, '4': None,
                 '5': None, '6': None, 'Three of a Kind': None, 'Four of a Kind': None,
                 'Full House': None, 'Small Straight': None, 'Large Straight': None,
                 'Yahtzee': None, 'Chance': None}
        dice = ['3', '3', '3', '3', '3']
        expected = 10
        actual = choose_score_location(score, dice)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['11'])
    def test_choose_score_location_eleven(self, mock_input):
        score = {'Name': 'Joon', '1': None, '2': None, '3': None, '4': None,
                 '5': None, '6': None, 'Three of a Kind': None, 'Four of a Kind': None,
                 'Full House': None, 'Small Straight': None, 'Large Straight': None,
                 'Yahtzee': None, 'Chance': None}
        dice = ['3', '3', '3', '3', '3']
        expected = 11
        actual = choose_score_location(score, dice)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['12'])
    def test_choose_score_location_twelve(self, mock_input):
        score = {'Name': 'Joon', '1': None, '2': None, '3': None, '4': None,
                 '5': None, '6': None, 'Three of a Kind': None, 'Four of a Kind': None,
                 'Full House': None, 'Small Straight': None, 'Large Straight': None,
                 'Yahtzee': None, 'Chance': None}
        dice = ['3', '3', '3', '3', '3']
        expected = 12
        actual = choose_score_location(score, dice)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['12'])
    def test_choose_score_location_double_yazthee(self, mock_input):
        score = {'Name': 'Joon', '1': None, '2': None, '3': None, '4': None,
                 '5': None, '6': None, 'Three of a Kind': None, 'Four of a Kind': None,
                 'Full House': None, 'Small Straight': None, 'Large Straight': None,
                 'Yahtzee': 50, 'Chance': None}
        dice = ['3', '3', '3', '3', '3']
        expected = 12
        actual = choose_score_location(score, dice)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['13'])
    def test_choose_score_location(self, mock_input):
        score = {'Name': 'Joon', '1': None, '2': None, '3': None, '4': None,
                 '5': None, '6': None, 'Three of a Kind': None, 'Four of a Kind': None,
                 'Full House': None, 'Small Straight': None, 'Large Straight': None,
                 'Yahtzee': None, 'Chance': None}
        dice = ['3', '3', '3', '3', '3']
        expected = 13
        actual = choose_score_location(score, dice)
        self.assertEqual(expected, actual)
