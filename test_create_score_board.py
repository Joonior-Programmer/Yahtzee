from unittest import TestCase
from yahtzee import create_score_board


class TestCreateScoreBoard(TestCase):
    def test_create_score_board_my_name(self):
        name = 'Joon'
        expected = {'Name': 'Joon', '2': None, '3': None, '4': None, '5': None,
                    '6': None, '1': None, 'Three of a Kind': None, 'Four of a Kind': None,
                    'Full House': None, 'Small Straight': None, 'Large Straight': None,
                    'Yahtzee': None, 'Chance': None}
        actual = create_score_board(name)
        self.assertEqual(expected, actual)

    def test_create_score_board_number(self):
        name = '1'
        expected = {'Name': '1', '2': None, '3': None, '4': None, '5': None,
                    '6': None, '1': None, 'Three of a Kind': None, 'Four of a Kind': None,
                    'Full House': None, 'Small Straight': None, 'Large Straight': None,
                    'Yahtzee': None, 'Chance': None}
        actual = create_score_board(name)
        self.assertEqual(expected, actual)

    def test_create_score_character(self):
        name = '#'
        expected = {'Name': '#', '2': None, '3': None, '4': None, '5': None,
                    '6': None, '1': None, 'Three of a Kind': None, 'Four of a Kind': None,
                    'Full House': None, 'Small Straight': None, 'Large Straight': None,
                    'Yahtzee': None, 'Chance': None}
        actual = create_score_board(name)
        self.assertEqual(expected, actual)

    def test_create_score_board_empty(self):
        name = ''
        expected = {'Name': '', '2': None, '3': None, '4': None, '5': None,
                    '6': None, '1': None, 'Three of a Kind': None, 'Four of a Kind': None,
                    'Full House': None, 'Small Straight': None, 'Large Straight': None,
                    'Yahtzee': None, 'Chance': None}
        actual = create_score_board(name)
        self.assertEqual(expected, actual)

    def test_create_score_board_letter_number(self):
        name = 'Player1'
        expected = {'Name': 'Player1', '2': None, '3': None, '4': None, '5': None,
                    '6': None, '1': None, 'Three of a Kind': None, 'Four of a Kind': None,
                    'Full House': None, 'Small Straight': None, 'Large Straight': None,
                    'Yahtzee': None, 'Chance': None}
        actual = create_score_board(name)
        self.assertEqual(expected, actual)

    def test_create_score_board_character_letter(self):
        name = '#Joon'
        expected = {'Name': '#Joon', '2': None, '3': None, '4': None, '5': None,
                    '6': None, '1': None, 'Three of a Kind': None, 'Four of a Kind': None,
                    'Full House': None, 'Small Straight': None, 'Large Straight': None,
                    'Yahtzee': None, 'Chance': None}
        actual = create_score_board(name)
        self.assertEqual(expected, actual)

    def test_create_score_board_character_number(self):
        name = '#1'
        expected = {'Name': '#1', '2': None, '3': None, '4': None, '5': None,
                    '6': None, '1': None, 'Three of a Kind': None, 'Four of a Kind': None,
                    'Full House': None, 'Small Straight': None, 'Large Straight': None,
                    'Yahtzee': None, 'Chance': None}
        actual = create_score_board(name)
        self.assertEqual(expected, actual)

    def test_create_score_board_space(self):
        name = ' '
        expected = {'Name': ' ', '2': None, '3': None, '4': None, '5': None,
                    '6': None, '1': None, 'Three of a Kind': None, 'Four of a Kind': None,
                    'Full House': None, 'Small Straight': None, 'Large Straight': None,
                    'Yahtzee': None, 'Chance': None}
        actual = create_score_board(name)
        self.assertEqual(expected, actual)
