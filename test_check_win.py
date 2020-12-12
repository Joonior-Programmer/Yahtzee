from unittest import TestCase
from yahtzee import check_win
from unittest.mock import patch
import io


class TestCheckWin(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_win_all_zero(self, mock_output):
        player1 = {'Name': '1', '1': 0, '2': 0, '3': 0, '4': 0,
                   '5': 0, '6': 0, 'Three of a Kind': 0, 'Four of a Kind': 0,
                   'Full House': 0, 'Small Straight': 0, 'Large Straight': 0,
                   'Yahtzee': 0, 'Chance': 0}
        player2 = {'Name': '2', '1': 0, '2': 0, '3': 0, '4': 0,
                   '5': 0, '6': 0, 'Three of a Kind': 0, 'Four of a Kind': 0,
                   'Full House': 0, 'Small Straight': 0, 'Large Straight': 0,
                   'Yahtzee': 0, 'Chance': 0}
        expected = 'Scores are same! Draw!'
        check_win(player1, player2)
        self.assertEqual(expected, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_win_player1_win(self, mock_output):
        player1 = {'Name': 'Joon', '1': 2, '2': 0, '3': 0, '4': 0,
                   '5': 0, '6': 0, 'Three of a Kind': 0, 'Four of a Kind': 0,
                   'Full House': 0, 'Small Straight': 0, 'Large Straight': 0,
                   'Yahtzee': 0, 'Chance': 0}
        player2 = {'Name': 'BCIT', '1': 1, '2': 0, '3': 0, '4': 0,
                   '5': 0, '6': 0, 'Three of a Kind': 0, 'Four of a Kind': 0,
                   'Full House': 0, 'Small Straight': 0, 'Large Straight': 0,
                   'Yahtzee': 0, 'Chance': 0}
        expected = 'Player: *** Joon ***, Win!'
        check_win(player1, player2)
        self.assertEqual(expected, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_win_all_player2_win(self, mock_output):
        player1 = {'Name': 'Joon', '1': 0, '2': 2, '3': 0, '4': 0,
                   '5': 0, '6': 0, 'Three of a Kind': 0, 'Four of a Kind': 0,
                   'Full House': 0, 'Small Straight': 0, 'Large Straight': 0,
                   'Yahtzee': 0, 'Chance': 0}
        player2 = {'Name': 'BCIT', '1': 0, '2': 3, '3': 0, '4': 0,
                   '5': 0, '6': 0, 'Three of a Kind': 0, 'Four of a Kind': 0,
                   'Full House': 0, 'Small Straight': 0, 'Large Straight': 0,
                   'Yahtzee': 0, 'Chance': 0}
        expected = 'Player: *** BCIT ***, Win!'
        check_win(player1, player2)
        self.assertEqual(expected, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_win_random_numbers(self, mock_output):
        player1 = {'Name': 'Joon', '1': 3, '2': 4, '3': 6, '4': 0,
                   '5': 0, '6': 0, 'Three of a Kind': 8, 'Four of a Kind': 0,
                   'Full House': 0, 'Small Straight': 35, 'Large Straight': 0,
                   'Yahtzee': 0, 'Chance': 0}
        player2 = {'Name': 'BCIT', '1': 0, '2': 0, '3': 9, '4': 0,
                   '5': 0, '6': 0, 'Three of a Kind': 15, 'Four of a Kind': 0,
                   'Full House': 0, 'Small Straight': 0, 'Large Straight': 0,
                   'Yahtzee': 0, 'Chance': 0}
        expected = 'Player: *** Joon ***, Win!'
        check_win(player1, player2)
        self.assertEqual(expected, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_win_all_name_number(self, mock_output):
        player1 = {'Name': '1', '1': 0, '2': 0, '3': 0, '4': 0,
                   '5': 0, '6': 0, 'Three of a Kind': 0, 'Four of a Kind': 0,
                   'Full House': 0, 'Small Straight': 0, 'Large Straight': 0,
                   'Yahtzee': 0, 'Chance': 0}
        player2 = {'Name': '2', '1': 0, '2': 0, '3': 0, '4': 0,
                   '5': 0, '6': 0, 'Three of a Kind': 35, 'Four of a Kind': 0,
                   'Full House': 0, 'Small Straight': 0, 'Large Straight': 0,
                   'Yahtzee': 0, 'Chance': 0}
        expected = '1: 0   2: 35\n2 Win!\n'
        check_win(player1, player2)
        self.assertEqual(expected, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_win_name_character(self, mock_output):
        player1 = {'Name': '@', '1': 0, '2': 0, '3': 0, '4': 0,
                   '5': 0, '6': 0, 'Three of a Kind': 0, 'Four of a Kind': 0,
                   'Full House': 0, 'Small Straight': 0, 'Large Straight': 0,
                   'Yahtzee': 50, 'Chance': 0}
        player2 = {'Name': '#', '1': 0, '2': 0, '3': 0, '4': 0,
                   '5': 0, '6': 0, 'Three of a Kind': 0, 'Four of a Kind': 0,
                   'Full House': 0, 'Small Straight': 0, 'Large Straight': 0,
                   'Yahtzee': 0, 'Chance': 0}
        expected = '@: 50   #: 0\n@ Win!\n'
        check_win(player1, player2)
        self.assertEqual(expected, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_win_name_space(self, mock_output):
        player1 = {'Name': ' ', '1': 0, '2': 0, '3': 0, '4': 0,
                   '5': 0, '6': 0, 'Three of a Kind': 0, 'Four of a Kind': 30,
                   'Full House': 0, 'Small Straight': 0, 'Large Straight': 0,
                   'Yahtzee': 0, 'Chance': 0}
        player2 = {'Name': '##', '1': 0, '2': 0, '3': 0, '4': 0,
                   '5': 0, '6': 0, 'Three of a Kind': 0, 'Four of a Kind': 0,
                   'Full House': 0, 'Small Straight': 0, 'Large Straight': 0,
                   'Yahtzee': 0, 'Chance': 0}
        expected = 'Player: ***   ***, Win!'
        check_win(player1, player2)
        self.assertEqual(expected, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_win_add_bonus(self, mock_output):
        player1 = {'Name': 'Bonus', '1': 6, '2': 12, '3': 18, '4': 24,
                   '5': 30, '6': 36, 'Three of a Kind': 0, 'Four of a Kind': 0,
                   'Full House': 0, 'Small Straight': 0, 'Large Straight': 0,
                   'Yahtzee': 0, 'Chance': 0, 'Bonus': 35}
        player2 = {'Name': 'Joon', '1': 0, '2': 0, '3': 0, '4': 0,
                   '5': 0, '6': 0, 'Three of a Kind': 0, 'Four of a Kind': 0,
                   'Full House': 0, 'Small Straight': 0, 'Large Straight': 0,
                   'Yahtzee': 0, 'Chance': 0}
        expected = 'Bonus: 161   Joon: 0\nBonus Win!\n'
        actual = check_win(player1, player2)
        self.assertEqual(expected, mock_output.getvalue())