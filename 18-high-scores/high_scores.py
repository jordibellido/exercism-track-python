"""
Exercise 18 - High Scores
"""

def latest (scores):
    """

    :param scores - list of high scores
    :return: int - the last added score from the list
    """

    return scores[-1]


def personal_best (scores):
    """

    :param scores - list of high scores
    :return: int - the highest score from the list
    """

    return max (scores)


def personal_top_three (scores):
    """

    :param scores - list of high scores
    :return: list of int - the three highest scores from the list
    """

    result      = []
    scores_copy = scores.copy ()
    scores_copy.sort (reverse = True)

    if len (scores) <= 3:
        return scores_copy

    return [scores_copy[0], scores_copy[1], scores_copy[2]]