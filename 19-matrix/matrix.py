"""
Exercise 19 - Matrix
"""

class Matrix:
    """
    Create a Matrix object from a string representation.

    Attributes
    ----------
    rows: list - List of lists representing an int matrix

    Methods
    -------
    row ():    list - Return a row of the matrix.
    column (): list - Return a column of the matrix.
    """

    def __init__ (self, matrix_string):
        """

        :param matrix_string: string - a string representing a matrix of numbers
        :return: a new Matrix instance
        """

        self.rows = []

        for line in matrix_string.split('\n'):
            temp_row = []

            for value in line.split (' '):
                if value != ' ':
                    temp_row.append (int (value))

            self.rows.append (temp_row)


    def row (self, index):
        """

        :param index: int - row index. It is 1 unit ahead of the zero-based numbering
        :return: list - row of the matrix
        """

        return self.rows[index - 1]


    def column (self, index):
        """

        :param index: int - column index. It is 1 unit ahead of the zero-based numbering
        :return: list - column of the matrix
        """
        index      -= 1
        temp_column = []

        for row in self.rows:
            if index < len (row):
                temp_column.append (row[index])

        return temp_column