from unittest import TestCase
from yahtzee import check_bonus


class TestCheckBonus(TestCase):
    def test_check_bonus_all_zeros(self):
        score = {'Name': 'Joon', '1': 0, '2': 0, '3': 0, '4': 0,
                 '5': 0, '6': 0, 'Three of a Kind': None, 'Four of a Kind': None,
                 'Full House': None, 'Small Straight': None, 'Large Straight': None,
                 'Yahtzee': None, 'Chance': None}
        expected = {'Name': 'Joon', '1': 0, '2': 0, '3': 0, '4': 0,
                 '5': 0, '6': 0, 'Three of a Kind': None, 'Four of a Kind': None,
                 'Full House': None, 'Small Straight': None, 'Large Straight': None,
                 'Yahtzee': None, 'Chance': None}
        actual = check_bonus(score)
        self.assertEqual(expected, actual)

    def test_check_bonus_all_one(self):
        score = {'Name': 'Joon', '1': 1, '2': 2, '3': 3, '4': 4,
                 '5': 5, '6': 6, 'Three of a Kind': None, 'Four of a Kind': None,
                 'Full House': None, 'Small Straight': None, 'Large Straight': None,
                 'Yahtzee': None, 'Chance': None}
        expected = {'Name': 'Joon', '1': 1, '2': 2, '3': 3, '4': 4,
                 '5': 5, '6': 6, 'Three of a Kind': None, 'Four of a Kind': None,
                 'Full House': None, 'Small Straight': None, 'Large Straight': None,
                 'Yahtzee': None, 'Chance': None}
        actual = check_bonus(score)
        self.assertEqual(expected, actual)

    def test_check_bonus_all_two(self):
        score = {'Name': 'Joon', '1': 2, '2': 4, '3': 6, '4': 8,
                 '5': 10, '6': 12, 'Three of a Kind': None, 'Four of a Kind': None,
                 'Full House': None, 'Small Straight': None, 'Large Straight': None,
                 'Yahtzee': None, 'Chance': None}
        expected = {'Name': 'Joon', '1': 2, '2': 4, '3': 6, '4': 8,
                 '5': 10, '6': 12, 'Three of a Kind': None, 'Four of a Kind': None,
                 'Full House': None, 'Small Straight': None, 'Large Straight': None,
                 'Yahtzee': None, 'Chance': None}
        actual = check_bonus(score)
        self.assertEqual(expected, actual)

    def test_check_bonus_all_three(self):
        score = {'Name': 'Joon', '1': 3, '2': 6, '3': 9, '4': 12,
                 '5': 15, '6': 18, 'Three of a Kind': None, 'Four of a Kind': None,
                 'Full House': None, 'Small Straight': None, 'Large Straight': None,
                 'Yahtzee': None, 'Chance': None}
        expected = {'Name': 'Joon', '1': 1, '2': 2, '3': 3, '4': 4,
                 '5': 5, '6': 6, 'Three of a Kind': None, 'Four of a Kind': None,
                 'Full House': None, 'Small Straight': None, 'Large Straight': None,
                 'Yahtzee': None, 'Chance': None, 'Bonus': 35}
        actual = check_bonus(score)
        self.assertEqual(expected, actual)

    def test_check_bonus_all_four(self):
        score = {'Name': 'Joon', '1': 4, '2': 8, '3': 12, '4': 16,
                 '5': 20, '6': 24, 'Three of a Kind': None, 'Four of a Kind': None,
                 'Full House': None, 'Small Straight': None, 'Large Straight': None,
                 'Yahtzee': None, 'Chance': None}
        expected = {'Name': 'Joon', '1': 4, '2': 8, '3': 12, '4': 16,
                 '5': 20, '6': 24, 'Three of a Kind': None, 'Four of a Kind': None,
                 'Full House': None, 'Small Straight': None, 'Large Straight': None,
                 'Yahtzee': None, 'Chance': None, 'Bonus': 35}
        actual = check_bonus(score)
        self.assertEqual(expected, actual)

    def test_check_bonus_all_five(self):
        score = {'Name': 'Joon', '1': 5, '2': 10, '3': 15, '4': 20,
                 '5': 25, '6': 30, 'Three of a Kind': None, 'Four of a Kind': None,
                 'Full House': None, 'Small Straight': None, 'Large Straight': None,
                 'Yahtzee': None, 'Chance': None}
        expected = {'Name': 'Joon', '1': 1, '2': 2, '3': 3, '4': 4,
                 '5': 5, '6': 6, 'Three of a Kind': None, 'Four of a Kind': None,
                 'Full House': None, 'Small Straight': None, 'Large Straight': None,
                 'Yahtzee': None, 'Chance': None, 'Bonus': 35}
        actual = check_bonus(score)
        self.assertEqual(expected, actual)

    def test_check_bonus_all_random_no_bonus(self):
        score = {'Name': 'Joon', '1': 1, '2': 4, '3': 9, '4': 4,
                 '5': 15, '6': 6, 'Three of a Kind': None, 'Four of a Kind': None,
                 'Full House': None, 'Small Straight': None, 'Large Straight': None,
                 'Yahtzee': None, 'Chance': None}
        expected = {'Name': 'Joon', '1': 1, '2': 4, '3': 9, '4': 4,
                 '5': 15, '6': 6, 'Three of a Kind': None, 'Four of a Kind': None,
                 'Full House': None, 'Small Straight': None, 'Large Straight': None,
                 'Yahtzee': None, 'Chance': None}
        actual = check_bonus(score)
        self.assertEqual(expected, actual)

    def test_check_bonus_all_random_bonus(self):
        score = {'Name': 'Joon', '1': 4, '2': 4, '3': 9, '4': 16,
                 '5': 25, '6': 24, 'Three of a Kind': None, 'Four of a Kind': None,
                 'Full House': None, 'Small Straight': None, 'Large Straight': None,
                 'Yahtzee': None, 'Chance': None}
        expected = {'Name': 'Joon', '1': 4, '2': 4, '3': 9, '4': 16,
                 '5': 25, '6': 24, 'Three of a Kind': None, 'Four of a Kind': None,
                 'Full House': None, 'Small Straight': None, 'Large Straight': None,
                 'Yahtzee': None, 'Chance': None, 'Bonus': 35}
        actual = check_bonus(score)
        self.assertEqual(expected, actual)
