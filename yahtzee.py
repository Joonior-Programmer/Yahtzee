"""
Student Name : Joonhyeong Kim
Student # : A01077938
COMP 1510
Assignment 3
Yahtzee Game
"""


import random


def create_score_board(user_name: str) -> dict:
    """
    >>> name = 'Joonnn'
    >>> create_score_board(name)
    {'Name': 'Joonnn', '1': None, '2': None, '3': None, '4': None,\
     '5': None, '6': None, 'Three of a Kind': None, 'Four of a Kind': None,\
     'Full House': None, 'Small Straight': None, 'Large Straight': None,\
     'Yahtzee': None, 'Chance': None}

    >>> name = 'Chris'
    >>> create_score_board(name)
    {'Name': 'Chris', '1': None, '2': None, '3': None, '4': None,\
     '5': None, '6': None, 'Three of a Kind': None, 'Four of a Kind': None,\
     'Full House': None, 'Small Straight': None, 'Large Straight': None,\
     'Yahtzee': None, 'Chance': None}

    :param user_name: a string that represents user name
    :return: a dictionary that represent score board with user name
    """
    return {'Name': user_name, '1': None, '2': None, '3': None, '4': None,
            '5': None, '6': None, 'Three of a Kind': None, 'Four of a Kind': None,
            'Full House': None, 'Small Straight': None, 'Large Straight': None,
            'Yahtzee': None, 'Chance': None}


def menu_before_roll_dice() -> str or False:
    """
    Get a user's choice before roll dice

    :post-condition: get a user input, and return it
    :return: a number that represent what user wants to do
    """
    while True:
        user_choice = input('Please write the number that you want to do\n'
                            '1: Roll dice\n'
                            'Q: Quit\n')
        if user_choice == '1':
            return 1
        elif user_choice == 'q' or user_choice == 'Q':
            quit('Successfully quit! Bye!')
        else:
            print('You wrote wrong input! Write 1 or Q!\n')


def menu_after_roll_dice() -> str or False:
    """
    Get a user's choice

    :post-condition: get a user input, and return it
    :return: a number that represent what user wants to do
    """
    choice_list = ['1', '2', '3']
    while True:
        user_choice = input('Please write the the number that you want to do\n'
                            '1: Roll dice\n'
                            '2: Save dice\n'
                            '3: Choose score\n'
                            'Q: Quit\n')
        if user_choice in choice_list:
            return int(user_choice)
        elif user_choice == 'Q' or user_choice == 'q':
            quit('Successfully quit! Bye!')
        else:
            print('You wrote wrong input! Write 1, 2, 3 or Q!\n')


def roll_dice(scores=None) -> list:
    """
    Roll dice

    >>> dice = ['*3', '*3', '*3', '*3', '*3']
    >>> roll_dice(dice)
    ['3', '3', '3', '3', '3']

    >>> dice = ['*1', '*2', '*3', '*4', '*5']
    >>> roll_dice(dice)
    ['1', '2', '3', '4', '5']

    :precondition: the argument must be an integer
    :post-condition: generate 5 integers between 1 and 6 that represent dice numbers as a list
    :return: a list that represent dice number
    """
    if scores:
        new_dice = [str(random.randint(1, 6)) if die.find('*') == -1 else die.replace('*', '') for die in scores]
        print(f'Your Dice : {new_dice[0]} {new_dice[1]} {new_dice[2]} {new_dice[3]} {new_dice[4]}')
        return new_dice
    else:
        new_dice = random.choices(range(1, 6), k=5)
        print(f'Your Dice : {new_dice[0]} {new_dice[1]} {new_dice[2]} {new_dice[3]} {new_dice[4]}')
        return new_dice


def select_dice(current_dice: list) -> list:
    """
    Save dice for next roll

    :param current_dice: a list that represent current dice numbers
    :precondition: current_dice must be a list that has 5 integers in it
    :post-condition: get user input for dice that user want to save, and add * if user choose to save the dice
    :return: a list that represent if dice saved
    """
    while True:
        dice_choice = input(f'Which die do you want to choose? (* represents saved)\n'
                            f'1: {current_dice[0]}\n2: {current_dice[1]}\n3: {current_dice[2]}\n'
                            f'4: {current_dice[3]}\n5: {current_dice[4]}\nB: Back to Menu\nQ: Quit Game\n')
        if dice_choice in str(list(range(1, 6))):
            if current_dice[int(dice_choice) - 1].find('*') == -1:
                current_dice[int(dice_choice) - 1] = current_dice[int(dice_choice) - 1].replace(
                    current_dice[int(dice_choice) - 1], '*' + current_dice[int(dice_choice) - 1])
            else:
                current_dice[int(dice_choice) - 1] = current_dice[int(dice_choice) - 1].replace('*', '')
        elif dice_choice == 'b' or dice_choice == 'B':
            return current_dice
        elif dice_choice == 'q' or dice_choice == 'Q':
            quit('Successfully quit! Bye!')
        else:
            print('\n***Please write right numbers or letters!***\n')


def choose_score_location(scores: dict, dice: list) -> dict:
    """
    Choose box on score board to place score

    :param scores: a dictionary that represents user scores
    :param dice: a list that contains strings of numbers that represent a die that user gets
    :post-condition: get user input to choose location, and add the score in the location
    :return: an integer that represent location
    """
    score_list = ['1', '2', '3', '4', '5', '6', 'Three of a Kind', 'Four of a Kind', 'Full House', 'Small Straight',
                  'Large Straight', 'Yahtzee', 'Chance']
    while True:
        location = input('Please write a number that you want to get a score.\n'
                         '1: 1                   8: Four of a Kind\n2: 2                   9: Full House\n'
                         '3: 3                   10: Small Straight\n4: 4                   11: Large Straight\n'
                         '5: 5                   12: Yahtzee\n6: 6                   13: Chance\n'
                         '7: Three of a Kind     Q: Quit\n')
        if location == 'q' or location == 'Q':
            quit('Successfully quit! Bye!')
        elif location == '12' and sorted(dice[0]) == sorted(dice[4]) and scores['Yahtzee'] != 0:
            return int(location)
        elif location in str(list(range(1, 14))) and \
                scores[score_list[int(location) - 1]] is None:
            return int(location)
        elif scores[score_list[int(location) - 1]] is not None:
            print('\nYou chose the place you have already chosen! Try to choose another place!\n')
        else:
            print('\nYou put wrong type of number or letter!\n')


def score_type(dice: list, scores: dict, location) -> dict:
    """
    Define constant scores that user can obtain

    >>> die = ['3', '3', '4', '1', '2']
    >>> score = {'Name': 'Joon', '1': None, '2': None, '3': None, '4': None,\
                 '5': None, '6': None, 'Three of a Kind': None, 'Four of a Kind': None,\
                 'Full House': None, 'Small Straight': None, 'Large Straight': None,\
                 'Yahtzee': None, 'Chance': None}
    >>> score_location = 3
    >>> score_type(die, score, score_location)
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

    >>> score_board = {'Name': 'Joon', '1': 6, '2': 12, '3': 18, '4': 24,\
                 '5': 30, '6': 36, 'Three of a Kind': None, 'Four of a Kind': None,\
                 'Full House': None, 'Small Straight': None, 'Large Straight': None,\
                 'Yahtzee': None, 'Chance': None}
    >>> check_bonus(score_board)
    {'Name': 'Joon', '1': 6, '2': 12, '3': 18, '4': 24,\
                 '5': 30, '6': 36, 'Three of a Kind': None, 'Four of a Kind': None,\
                 'Full House': None, 'Small Straight': None, 'Large Straight': None,\
                 'Yahtzee': None, 'Chance': None, 'Bonus': 35}

    >>> score_board = {'Name': 'Joon', '1': None, '2': None, '3': None, '4': None,\
                 '5': None, '6': None, 'Three of a Kind': None, 'Four of a Kind': None,\
                 'Full House': None, 'Small Straight': None, 'Large Straight': None,\
                 'Yahtzee': None, 'Chance': None}
    >>> check_bonus(score_board)
    {'Name': 'Joon', '1': 6, '2': 12, '3': 18, '4': 24,\
                 '5': 30, '6': 36, 'Three of a Kind': None, 'Four of a Kind': None,\
                 'Full House': None, 'Small Straight': None, 'Large Straight': None,\
                 'Yahtzee': None, 'Chance': None}

    :param scores: a dictionary that represents user scores
    :precondition: scores must be in dictionary format
    :post-condition: check if the user can get bonus point. if so, add 35 point to scores
    :return: a dictionary that added 35 points, if the user can get 35 points
    """
    score_list = ['1', '2', '3', '4', '5', '6']
    sum_of_upper_score = 0
    for key, score in scores.items():
        if key in score_list:
            sum_of_upper_score += score
    if sum_of_upper_score >= 63:
        scores['Bonus'] = 35
    return scores


print(check_bonus({'Name': 'Joon', '1': 6, '2': 12, '3': 18, '4': 24,\
                 '5': 30, '6': 36, 'Three of a Kind': None, 'Four of a Kind': None,\
                 'Full House': None, 'Small Straight': None, 'Large Straight': None,\
                 'Yahtzee': None, 'Chance': None}))


def main():
    """Drive the program"""
    pass
