from unittest import TestCase
from yahtzee import SCORE_TYPES


class TestLowerScoreTypes(TestCase):
    def test_lower_score_types_one(self):
        dice = ['2', '4', '5', '5', '5']
        score = {'Name': 'Joon', '1': None, '2': None, '3': None, '4': None,
                 '5': None, '6': None, 'Three of a Kind': None, 'Four of a Kind': None,
                 'Full House': None, 'Small Straight': None, 'Large Straight': None,
                 'Yahtzee': None, 'Chance': None}
        location = 1
        expected = {'Name': 'Joon', '1': 0, '2': None, '3': None, '4': None,
                    '5': None, '6': None, 'Three of a Kind': None, 'Four of a Kind': None,
                    'Full House': None, 'Small Straight': None, 'Large Straight': None,
                    'Yahtzee': None, 'Chance': None}
        actual = SCORE_TYPES(dice, score, location)
        self.assertEqual(expected, actual)

        def test_lower_score_types_two(self):
            dice = ['2', '4', '5', '5', '5']
            score = {'Name': 'Joon', '1': None, '2': None, '3': None, '4': None,
                     '5': None, '6': None, 'Three of a Kind': None, 'Four of a Kind': None,
                     'Full House': None, 'Small Straight': None, 'Large Straight': None,
                     'Yahtzee': None, 'Chance': None}
            location = 2
            expected = {'Name': 'Joon', '1': None, '2': 2, '3': None, '4': None,
                        '5': None, '6': None, 'Three of a Kind': None, 'Four of a Kind': None,
                        'Full House': None, 'Small Straight': None, 'Large Straight': None,
                        'Yahtzee': None, 'Chance': None}
            actual = SCORE_TYPES(dice, score, location)
            self.assertEqual(expected, actual)

        def test_lower_score_types_three(self):
            dice = ['2', '4', '5', '5', '5']
            score = {'Name': 'Joon', '1': None, '2': None, '3': None, '4': None,
                     '5': None, '6': None, 'Three of a Kind': None, 'Four of a Kind': None,
                     'Full House': None, 'Small Straight': None, 'Large Straight': None,
                     'Yahtzee': None, 'Chance': None}
            location = 3
            expected = {'Name': 'Joon', '1': None, '2': None, '3': 0, '4': None,
                        '5': None, '6': None, 'Three of a Kind': None, 'Four of a Kind': None,
                        'Full House': None, 'Small Straight': None, 'Large Straight': None,
                        'Yahtzee': None, 'Chance': None}
            actual = SCORE_TYPES(dice, score, location)
            self.assertEqual(expected, actual)

        def test_lower_score_types_four(self):
            dice = ['2', '4', '5', '5', '5']
            score = {'Name': 'Joon', '1': None, '2': None, '3': None, '4': None,
                     '5': None, '6': None, 'Three of a Kind': None, 'Four of a Kind': None,
                     'Full House': None, 'Small Straight': None, 'Large Straight': None,
                     'Yahtzee': None, 'Chance': None}
            location = 4
            expected = {'Name': 'Joon', '1': None, '2': None, '3': None, '4': 4,
                        '5': None, '6': None, 'Three of a Kind': None, 'Four of a Kind': None,
                        'Full House': None, 'Small Straight': None, 'Large Straight': None,
                        'Yahtzee': None, 'Chance': None}
            actual = SCORE_TYPES(dice, score, location)
            self.assertEqual(expected, actual)

        def test_lower_score_types_five(self):
            dice = ['2', '4', '5', '5', '5']
            score = {'Name': 'Joon', '1': None, '2': None, '3': None, '4': None,
                     '5': None, '6': None, 'Three of a Kind': None, 'Four of a Kind': None,
                     'Full House': None, 'Small Straight': None, 'Large Straight': None,
                     'Yahtzee': None, 'Chance': None}
            location = 5
            expected = {'Name': 'Joon', '1': None, '2': None, '3': None, '4': None,
                        '5': 15, '6': None, 'Three of a Kind': None, 'Four of a Kind': None,
                        'Full House': None, 'Small Straight': None, 'Large Straight': None,
                        'Yahtzee': None, 'Chance': None}
            actual = SCORE_TYPES(dice, score, location)
            self.assertEqual(expected, actual)

        def test_lower_score_types_six(self):
            dice = ['2', '4', '5', '5', '5']
            score = {'Name': 'Joon', '1': None, '2': None, '3': None, '4': None,
                     '5': None, '6': None, 'Three of a Kind': None, 'Four of a Kind': None,
                     'Full House': None, 'Small Straight': None, 'Large Straight': None,
                     'Yahtzee': None, 'Chance': None}
            location = 6
            expected = {'Name': 'Joon', '1': None, '2': None, '3': None, '4': None,
                        '5': None, '6': 0, 'Three of a Kind': None, 'Four of a Kind': None,
                        'Full House': None, 'Small Straight': None, 'Large Straight': None,
                        'Yahtzee': None, 'Chance': None}
            actual = SCORE_TYPES(dice, score, location)
            self.assertEqual(expected, actual)

        def test_lower_score_types_seven(self):
            dice = ['2', '4', '5', '5', '5']
            score = {'Name': 'Joon', '1': None, '2': None, '3': None, '4': None,
                     '5': None, '6': None, 'Three of a Kind': None, 'Four of a Kind': None,
                     'Full House': None, 'Small Straight': None, 'Large Straight': None,
                     'Yahtzee': None, 'Chance': None}
            location = 7
            expected = {'Name': 'Joon', '1': None, '2': None, '3': None, '4': None,
                        '5': None, '6': None, 'Three of a Kind': 21, 'Four of a Kind': None,
                        'Full House': None, 'Small Straight': None, 'Large Straight': None,
                        'Yahtzee': None, 'Chance': None}
            actual = SCORE_TYPES(dice, score, location)
            self.assertEqual(expected, actual)

        def test_lower_score_types_eight(self):
            dice = ['2', '5', '5', '5', '5']
            score = {'Name': 'Joon', '1': None, '2': None, '3': None, '4': None,
                     '5': None, '6': None, 'Three of a Kind': None, 'Four of a Kind': None,
                     'Full House': None, 'Small Straight': None, 'Large Straight': None,
                     'Yahtzee': None, 'Chance': None}
            location = 8
            expected = {'Name': 'Joon', '1': None, '2': None, '3': None, '4': None,
                        '5': None, '6': None, 'Three of a Kind': None, 'Four of a Kind': 22,
                        'Full House': None, 'Small Straight': None, 'Large Straight': None,
                        'Yahtzee': None, 'Chance': None}
            actual = SCORE_TYPES(dice, score, location)
            self.assertEqual(expected, actual)

        def test_lower_score_types_nine(self):
            dice = ['4', '4', '5', '5', '5']
            score = {'Name': 'Joon', '1': None, '2': None, '3': None, '4': None,
                     '5': None, '6': None, 'Three of a Kind': None, 'Four of a Kind': None,
                     'Full House': None, 'Small Straight': None, 'Large Straight': None,
                     'Yahtzee': None, 'Chance': None}
            location = 9
            expected = {'Name': 'Joon', '1': None, '2': None, '3': None, '4': None,
                        '5': None, '6': None, 'Three of a Kind': None, 'Four of a Kind': None,
                        'Full House': 25, 'Small Straight': None, 'Large Straight': None,
                        'Yahtzee': None, 'Chance': None}
            actual = SCORE_TYPES(dice, score, location)
            self.assertEqual(expected, actual)

        def test_lower_score_types_ten(self):
            dice = ['1', '2', '3', '4', '6']
            score = {'Name': 'Joon', '1': None, '2': None, '3': None, '4': None,
                     '5': None, '6': None, 'Three of a Kind': None, 'Four of a Kind': None,
                     'Full House': None, 'Small Straight': None, 'Large Straight': None,
                     'Yahtzee': None, 'Chance': None}
            location = 10
            expected = {'Name': 'Joon', '1': None, '2': None, '3': None, '4': None,
                        '5': None, '6': None, 'Three of a Kind': None, 'Four of a Kind': None,
                        'Full House': None, 'Small Straight': 30, 'Large Straight': None,
                        'Yahtzee': None, 'Chance': None}
            actual = SCORE_TYPES(dice, score, location)
            self.assertEqual(expected, actual)

        def test_lower_score_types_eleven(self):
            dice = ['1', '2', '3', '4', '5']
            score = {'Name': 'Joon', '1': None, '2': None, '3': None, '4': None,
                     '5': None, '6': None, 'Three of a Kind': None, 'Four of a Kind': None,
                     'Full House': None, 'Small Straight': None, 'Large Straight': None,
                     'Yahtzee': None, 'Chance': None}
            location = 11
            expected = {'Name': 'Joon', '1': None, '2': None, '3': None, '4': None,
                        '5': None, '6': None, 'Three of a Kind': None, 'Four of a Kind': None,
                        'Full House': None, 'Small Straight': None, 'Large Straight': 40,
                        'Yahtzee': None, 'Chance': None}
            actual = SCORE_TYPES(dice, score, location)
            self.assertEqual(expected, actual)

        def test_lower_score_types_twelve(self):
            dice = ['5', '5', '5', '5', '5']
            score = {'Name': 'Joon', '1': None, '2': None, '3': None, '4': None,
                     '5': None, '6': None, 'Three of a Kind': None, 'Four of a Kind': None,
                     'Full House': None, 'Small Straight': None, 'Large Straight': None,
                     'Yahtzee': None, 'Chance': None}
            location = 12
            expected = {'Name': 'Joon', '1': None, '2': None, '3': None, '4': None,
                        '5': None, '6': None, 'Three of a Kind': None, 'Four of a Kind': None,
                        'Full House': None, 'Small Straight': None, 'Large Straight': None,
                        'Yahtzee': 50, 'Chance': None}
            actual = SCORE_TYPES(dice, score, location)
            self.assertEqual(expected, actual)

        def test_lower_score_types_yahtzee_twice(self):
            dice = ['5', '5', '5', '5', '5']
            score = {'Name': 'Joon', '1': None, '2': None, '3': None, '4': None,
                     '5': None, '6': None, 'Three of a Kind': None, 'Four of a Kind': None,
                     'Full House': None, 'Small Straight': None, 'Large Straight': None,
                     'Yahtzee': 50, 'Chance': None}
            location = 12
            expected = {'Name': 'Joon', '1': None, '2': None, '3': None, '4': None,
                        '5': None, '6': None, 'Three of a Kind': None, 'Four of a Kind': None,
                        'Full House': None, 'Small Straight': None, 'Large Straight': None,
                        'Yahtzee': 150, 'Chance': None}
            actual = SCORE_TYPES(dice, score, location)
            self.assertEqual(expected, actual)

        def test_lower_score_types_thirteen(self):
            dice = ['3', '2', '4', '3', '2']
            score = {'Name': 'Joon', '1': None, '2': None, '3': None, '4': None,
                     '5': None, '6': None, 'Three of a Kind': None, 'Four of a Kind': None,
                     'Full House': None, 'Small Straight': None, 'Large Straight': None,
                     'Yahtzee': None, 'Chance': None}
            location = 13
            expected = {'Name': 'Joon', '1': None, '2': None, '3': None, '4': None,
                        '5': None, '6': None, 'Three of a Kind': None, 'Four of a Kind': None,
                        'Full House': None, 'Small Straight': None, 'Large Straight': None,
                        'Yahtzee': None, 'Chance': 14}
            actual = SCORE_TYPES(dice, score, location)
            self.assertEqual(expected, actual)
