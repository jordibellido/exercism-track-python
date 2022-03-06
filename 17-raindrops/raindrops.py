"""
Exercise 17 - Raindrops
"""

def convert (number):
    """

    :param number: int
    :return: str - as requested
    """

    result = ''

    if (number % 3) == 0:
        result = 'Pling'

    if (number % 5) == 0:
        result += 'Plang'

    if (number % 7) == 0:
        result += 'Plong'

    if len (result) == 0:
        return f'{number}'

    return result
