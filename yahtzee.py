"""
Student Name : Joonhyeong Kim
Student # : A01077938
COMP 1510
Assignment 3
Yahtzee Game
"""


def create_score_board(user_name: str) -> dict:
    """
    >>> name = 'Joon'
    >>> create_score_board(name)
    {'Name': 'Joon', '1\'s': None, '2\'s': None, '3\'s': None, '4\'s': None,\
     '5\'s': None, '6\'s': None, 'Three of a Kind': None, 'Four of a Kind': None,\
     'Full House': None, 'Small Straight': None, 'Large Straight': None,\
     'Yahtzee': None, 'Chance': None}

    >>> name = 'Chris'
    >>> create_score_board(name)
    {'Name': 'Chris', '1\'s': None, '2\'s': None, '3\'s': None, '4\'s': None,\
     '5\'s': None, '6\'s': None, 'Three of a Kind': None, 'Four of a Kind': None,\
     'Full House': None, 'Small Straight': None, 'Large Straight': None,\
     'Yahtzee': None, 'Chance': None}

    :param user_name: a string that represents user name
    :return: a dictionary that represent score board with user name
    """
    pass


def menu_before_roll_dice() -> str or False:
    """
    Get a user's choice before roll dice

    :post-condition: get a user input, and return it
    :return: a number that represent what user wants to do
    """
    pass


def menu_after_roll_dice() -> str or False:
    """
    Get a user's choice

    :post-condition: get a user input, and return it
    :return: a number that represent what user wants to do
    """
    pass


def roll_dice(scores: None) -> list:
    """
    Roll dice

    :precondition: the argument must be an integer
    :post-condition: generate 5 integers between 1 and 6 that represent dice numbers as a list
    :return: a list that represent dice number
    """
    pass


def select_dice(current_dice: list) -> list:
    """
    Save dice for next roll

    :param current_dice: a list that represent current dice numbers
    :precondition: current_dice must be a list that has 5 integers in it
    :post-condition: get user input for dice that user want to save, and add * if user choose to save the dice
    :return: a list that represent if dice saved
    """
    pass


def choose_score_location(scores: dict) -> dict:
    """
    Choose box on score board to place score

    :param scores: a dictionary that represents user scores
    :post-condition: get user input to choose location, and add the score in the location
    :return: an integer that represent location
    """
    pass


def score_type(dice: list, scores: dict, location) -> dict:
    """
    Define constant scores that user can obtain

    >>> die = ['3', '3', '4', '1', '2']
    >>> score = {'Name': 'Joon', '1': None, '2': None, '3': None, '4': None,\
                 '5': None, '6': None, 'Three of a Kind': None, 'Four of a Kind': None,\
                 'Full House': None, 'Small Straight': None, 'Large Straight': None,\
                 'Yahtzee': None, 'Chance': None}
    >>> score_location = 3
    >>> SCORE_TYPES(die, score, score_location)
    {'Name': 'Joon', '1': None, '2': None, '3': 6, '4': None,\
    '5': None, '6': None, 'Three of a Kind': None, 'Four of a Kind': None,\
    'Full House': None, 'Small Straight': None, 'Large Straight': None,\
    'Yahtzee': None, 'Chance': None}

    >>> die = ['3', '4', '4', '1', '2']
    >>> score = {'Name': 'Joon', '1': None, '2': None, '3': None, '4': None,\
                 '5': None, '6': None, 'Three of a Kind': None, 'Four of a Kind': None,\
                 'Full House': None, 'Small Straight': None, 'Large Straight': None,\
                 'Yahtzee': None, 'Chance': None}
    >>> score_location = 13
    {'Name': 'Joon', '1': None, '2': None, '3': None, '4': None,\
    '5': None, '6': None, 'Three of a Kind': None, 'Four of a Kind': None,\
    'Full House': None, 'Small Straight': None, 'Large Straight': None,\
    'Yahtzee': None, 'Chance': 14}

    :param dice: a list that represents dice numbers
    :param scores: a dictionary that represents user scores
    :param location: an integer that represent location
    :precondition: arguments must be in right format
    :post-condition: define score that user gets, and add to score board
    :return: a dictionary that the score added in right place
    """
    pass


def check_win(player1_scores: dict, player2_scores: dict) -> str:
    """
    define who wins from adding all scores

    :param player1_scores: a dictionary that represents player1 scores
    :param player2_scores: a dictionary that represents player2 scores
    :precondition: dictionaries must be fully filled
    :post-condition: define which player has more score, and return the player
    :return: a string that represent winner.
    """
    pass


def check_bonus(scores: dict) -> dict:
    """
    check if the total upper score is over 63

    >>> score = {'Name': 'Joon', '1': 6, '2': 12, '3': 18, '4': 24,\
                 '5': 30, '6': 36, 'Three of a Kind': None, 'Four of a Kind': None,\
                 'Full House': None, 'Small Straight': None, 'Large Straight': None,\
                 'Yahtzee': None, 'Chance': None}
    >>> check_bonus(score)
    {'Name': 'Joon', '1': 6, '2': 12, '3': 18, '4': 24,\
                 '5': 30, '6': 36, 'Three of a Kind': None, 'Four of a Kind': None,\
                 'Full House': None, 'Small Straight': None, 'Large Straight': None,\
                 'Yahtzee': None, 'Chance': None, 'Bonus': 35}

    >>> score = {'Name': 'Joon', '1': None, '2': None, '3': None, '4': None,\
                 '5': None, '6': None, 'Three of a Kind': None, 'Four of a Kind': None,\
                 'Full House': None, 'Small Straight': None, 'Large Straight': None,\
                 'Yahtzee': None, 'Chance': None}
    >>> check_bonus(score)
    {'Name': 'Joon', '1': 6, '2': 12, '3': 18, '4': 24,\
                 '5': 30, '6': 36, 'Three of a Kind': None, 'Four of a Kind': None,\
                 'Full House': None, 'Small Straight': None, 'Large Straight': None,\
                 'Yahtzee': None, 'Chance': None}

    :param scores: a dictionary that represents user scores
    :precondition: scores must be in dictionary format
    :post-condition: check if the user can get bonus point. if so, add 35 point to scores
    :return: a dictionary that added 35 points, if the user can get 35 points
    """
    pass


def main():
    """Drive the program"""
    pass
