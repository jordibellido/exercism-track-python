"""
Exercise 7 - Card Games
"""

def get_rounds (number):
    """Creates a list containing the current and next two round numbers.

     :param number: int - current round number.
     :return: list - current round and the two that follow.
    """

    return list ({number, number + 1, number + 2})


def concatenate_rounds (rounds_1, rounds_2):
    """Concatenates two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round (rounds, number):
    """Checks if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return:  bool - was the round played?
    """

    return number in rounds


def card_average (hand):
    """Calculates and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return:  float - average value of the cards in the hand.
    """

    return sum (hand) / len (hand)


def approx_average_is_average (hand):
    """Returns if an average using (first + last index values ) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - if approximate average equals to the `true average`.
    """

    average   = card_average (hand)
    average_1 = (hand[0] + hand[-1]) / 2
    average_2 = hand[int(len (hand) / 2)]
    return average in {average_1, average_2}


def average_even_is_average_odd (hand):
    """Returns if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    hand_even_elem = []
    hand_odd_elem  = []

    for index, element in enumerate (hand):
        if index % 2:
            # Even indexes are odd positions in a list
            hand_even_elem.append (element)
        else:
            hand_odd_elem.append  (element)

    return card_average (hand_even_elem) == card_average (hand_odd_elem)


def maybe_double_last (hand):
    """Multiplies a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    if hand[-1] == 11:
        hand[-1] = 22

    return hand
