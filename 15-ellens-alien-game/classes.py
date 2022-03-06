"""
Solution to Ellen's Alien Game exercise

Exercise 15 - Ellen's Alien Game

"""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Amount of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    total_aliens_created = 0

    def __init__ (self, x_coordinate, y_coordinate):
        """

        :param x_coordinate: int
        :param y_coordinate: int
        :return: new Alien instance
        """

        self.x_coordinate           = x_coordinate
        self.y_coordinate           = y_coordinate
        self.health                 = 3
        Alien.total_aliens_created += 1

    def hit (self):
        """

        :return: int - decreased alien's health
        """
        if self.health > 0:
            self.health -= 1

    def is_alive (self):
        """

        :return: bool - whether the alien is alive or not
        """
        return self.health > 0

    def teleport (self, new_x_coordinate, new_y_coordinate):
        """

        :param new_x_coordinate: int
        :param new_y_coordinate: int
        """
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate

    def collision_detection (self, other_object):
        """

        :param other_object: unknown
        """
        return

def total_aliens_created ():
    """

    :return: int - how many aliens have been created over the game's lifetime
    """
    return total_aliens_created

def new_aliens_collection (alien_start_positions):
    """

    :return: list - Alien instances
    """

    result = []

    for position in alien_start_positions:
        result.append (Alien (position[0], position[1]))

    return result
