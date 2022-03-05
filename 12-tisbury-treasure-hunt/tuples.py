"""
Exercise 12 - Tisbury Treasure Hunt
"""

def get_coordinate (record):
    """

    :param record: tuple - a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """

    return record[1]


def convert_coordinate (coordinate):
    """

    :param coordinate: str - a string map coordinate
    :return:  tuple - the string coordinate seperated into its individual components.
    """

    return (coordinate[0], coordinate[1])


def compare_records (azara_record, rui_record):
    """

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: bool - True if coordinates match, False otherwise.
    """

    azara_coordinate = convert_coordinate (get_coordinate (azara_record))
    rui_coordinate   = rui_record[1]

    return azara_coordinate[0] == rui_coordinate[0] and azara_coordinate[1] == rui_coordinate[1]


def create_record (azara_record, rui_record):
    """

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return:  tuple - combined record, or "not a match" if the records are incompatible.
    """

    if not compare_records (azara_record, rui_record):
        return 'not a match'

    return azara_record + rui_record


def clean_up (combined_record_group):
    """

    :param combined_record_group: tuple of tuples - everything from both participants.
    :return: string of tuples separated by newlines - everything "cleaned". Excess coordinates and information removed.
    """

    result = ''

    for record in combined_record_group:
        if "'" in record[0]:
            result += f"(\"{record[0]}\", '{record[2]}', {record[3]}, '{record[4]}')\n"
        else:
            result += f"('{record[0]}', '{record[2]}', {record[3]}, '{record[4]}')\n"

    return result
