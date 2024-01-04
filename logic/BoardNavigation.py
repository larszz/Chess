from typing import Type, ForwardRef

from logic.ChessError import ChessError


class CoordinateDifference:
    row_diff: int
    col_diff: int


    def __init__(self, row_diff, col_diff):
        self.row_diff = row_diff
        self.col_diff = col_diff


    def has_valid_direction(self) -> bool:
        return (self.row_diff == 0) or (self.col_diff == 0) or (self.get_absolute_row_diff() == self.get_absolute_col_diff())


    def get_direction(self):
        if not self.has_valid_direction():
            raise ChessError(f"Difference {self} has no valid direction")
        return CoordinateDifference(self.get_row_direction(), self.get_col_direction())


    def get_row_direction(self):
        return CoordinateDifference._get_direction_from_value(self.row_diff)


    def get_col_direction(self):
        return CoordinateDifference._get_direction_from_value(self.col_diff)


    def get_absolute_row_diff(self):
        return abs(self.row_diff)


    def get_absolute_col_diff(self):
        return abs(self.col_diff)


    def get_max_difference(self):
        return max(self.row_diff, self.col_diff)


    def get_min_difference(self):
        return min(self.row_diff, self.col_diff)


    def create_as_absolute(self):
        return CoordinateDifference(self.get_absolute_row_diff(), self.get_absolute_col_diff())


    def get_length_to_move(self):
        return self.create_as_absolute().get_max_difference()


    def is_straight_direction(self):
        try:
            direction = self.get_direction()
            return (direction.create_as_absolute().get_max_difference() > 0) and ((direction.row_diff == 0) or (direction.col_diff == 0))
        except ChessError:
            return False

    def is_diagonal_direction(self):
        try:
            direction = self.create_as_absolute().get_direction()
            return (direction.create_as_absolute().get_max_difference() > 0) and (direction.row_diff == direction.col_diff)
        except ChessError:
            return False



    def __str__(self):
        return f"({self.row_diff},{self.col_diff})"

    def __eq__(self, other):
        if not isinstance(other, CoordinateDifference):
            return False
        return (self.row_diff == other.row_diff) and (self.col_diff == other.col_diff)

    @staticmethod
    def _get_direction_from_value(value: int):
        if value < 0:
            return -1
        elif value > 0:
            return 1
        return 0


class Coordinate:
    row: int
    col: int


    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col


    def get_with_added(self, diff: CoordinateDifference) -> ForwardRef('Coordinate'):
        return Coordinate(self.row + diff.row_diff, self.col + diff.col_diff)


    def get_difference_to_other(self, other: ForwardRef('Coordinate')) -> CoordinateDifference:
        return CoordinateDifference(other.row - self.row, other.col - self.col)


    def get_direction_to_other(self, other: ForwardRef('Coordinate')) -> CoordinateDifference:
        return self.get_difference_to_other(other).get_direction()


    def get_fields_on_way_to(self, other: ForwardRef('Coordinate')) -> list:
        fields: list[Coordinate] = []
        if self != other:
            direction = self.get_direction_to_other(other)
            current_field: Coordinate = self
            while True:
                current_field = current_field.get_with_added(direction)
                if current_field == other:
                    break
                fields.append(current_field)
        return fields


    def get_number_of_fields_to_move(self, other: ForwardRef('Coordinate')) -> int:
        difference = self.get_difference_to_other(other).create_as_absolute()
        if not difference.has_valid_direction():
            raise ChessError(f"Difference {difference} has no valid direction")
        return max(difference.row_diff, difference.col_diff)


    def get_number_of_fields_between(self, other: ForwardRef('Coordinate')) -> int:
        number_of_fields_total = self.get_number_of_fields_to_move(other)
        number_of_fields_to_subtract = 1  # one of start/destination would be counted
        number_of_fields_between = max(number_of_fields_total-number_of_fields_to_subtract, 0)  # allow same field be 0 distance
        return number_of_fields_between


    def __eq__(self, other):
        return (other.row == self.row) and (other.col == self.col)

    def __str__(self):
        return f"({self.row},{self.col})"

    def __hash__(self):
        return hash((self.row, self.col))

    @staticmethod
    def make_from_tuple(t: tuple):
        if len(t) != 2:
            raise ChessError(f"Tuple length != 2: {len(t)}")
        return Coordinate(t[0], t[1])


class ChessCoordinate(Coordinate):

    def __init__(self, coordinate: str):
        chars = [_ for _ in coordinate]
        if len(chars) != 2:
            raise ChessError(f"Coordinate has wrong length: is {len(chars)}, should be 2")
        row = self.get_row_value_from_char(chars[1])
        col = self.get_col_value_from_char(chars[0])

        super().__init__(row, col)


    @staticmethod
    def get_col_value_from_char(char: str) -> int:
        if len(char) != 1:
            raise ChessError(f"Row coordinate has wrong length: {len(char)} != 1")
        char = char.lower()
        lower_bound = ord('a')
        upper_bound = ord('h') + 1
        if ord(char) not in [_ for _ in range(lower_bound, upper_bound)]:
            raise ChessError(f"Row coordinate is not in range: {char}")
        return ord(char) - lower_bound

    @staticmethod
    def get_row_value_from_char(char: str) -> int:
        if len(char) != 1:
            raise ChessError(f"Col coordinate has wrong length: {len(char)} != 1")
        lower_bound = 0
        upper_bound = 7 + 1
        index = upper_bound - int(char)  # chess coordinates are one-based
        if index not in [_ for _ in range(lower_bound, upper_bound)]:
            raise ChessError(f"Col coordinate is not in range: {index}")
        return index


class Move:
    from_coordinate: Coordinate
    to_coordinate: Coordinate

    def __init__(self, from_coordinate: Coordinate, to_coordinate: Coordinate):
        self.from_coordinate = from_coordinate
        self.to_coordinate = to_coordinate


    def get_difference(self):
        return self.from_coordinate.get_difference_to_other(other=self.to_coordinate)

    def get_direction(self):
        return self.from_coordinate.get_direction_to_other(other=self.to_coordinate)

    def get_fields_on_way(self):
        return self.from_coordinate.get_fields_on_way_to(other=self.to_coordinate)

    def get_number_of_fields_to_move(self) -> int:
        return self.from_coordinate.get_number_of_fields_to_move(other=self.to_coordinate)

    def get_number_of_fields_between(self) -> int:
        return self.from_coordinate.get_number_of_fields_between(other=self.to_coordinate)

    def __str__(self):
        return f"from {self.from_coordinate} to {self.to_coordinate}"

    @staticmethod
    def make_from_tuples(from_tuple: tuple, to_tuple: tuple):
        return Move(Coordinate.make_from_tuple(from_tuple), Coordinate.make_from_tuple(to_tuple))

    @staticmethod
    def make_from_chess_coordinates(from_coordinate: str, to_coordinate: str):
        return Move(ChessCoordinate(from_coordinate), ChessCoordinate(to_coordinate))




