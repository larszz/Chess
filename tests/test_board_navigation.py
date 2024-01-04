import copy
import unittest

from logic.ChessError import ChessError
from logic.BoardNavigation import Coordinate, CoordinateDifference, ChessCoordinate, Move
from tests.BaseChessTest import BaseChessTest


class ChessTestCoordinateDifference(BaseChessTest):

    def test_valid_direction(self):
        self.assertTrue(CoordinateDifference(0, 3).has_valid_direction())
        self.assertTrue(CoordinateDifference(3, 0).has_valid_direction())
        self.assertTrue(CoordinateDifference(3, 3).has_valid_direction())
        self.assertTrue(CoordinateDifference(-3, -3).has_valid_direction())
        self.assertTrue(CoordinateDifference(3, -3).has_valid_direction())
        self.assertTrue(CoordinateDifference(-3, 3).has_valid_direction())

        self.assertFalse(CoordinateDifference(1, 2).has_valid_direction())
        self.assertFalse(CoordinateDifference(2, 1).has_valid_direction())


    def test_get_direction(self):
        self.assertEqual(CoordinateDifference(0, 3).get_direction(), CoordinateDifference(0, 1))
        self.assertEqual(CoordinateDifference(3, 0).get_direction(), CoordinateDifference(1, 0))
        self.assertEqual(CoordinateDifference(3, 3).get_direction(), CoordinateDifference(1, 1))
        self.assertEqual(CoordinateDifference(-3, -3).get_direction(), CoordinateDifference(-1, -1))
        self.assertEqual(CoordinateDifference(3, -3).get_direction(), CoordinateDifference(1, -1))
        self.assertEqual(CoordinateDifference(-3, 3).get_direction(), CoordinateDifference(-1, 1))

        self.assertRaises(ChessError, CoordinateDifference(1, 2).get_direction)
        self.assertRaises(ChessError, CoordinateDifference(2, 1).get_direction)


    def test_is_straight_direction(self):
        self.assertTrue(CoordinateDifference(0, 1).is_straight_direction())
        self.assertTrue(CoordinateDifference(0, 8).is_straight_direction())
        self.assertTrue(CoordinateDifference(1, 0).is_straight_direction())
        self.assertTrue(CoordinateDifference(8, 0).is_straight_direction())
        self.assertTrue(CoordinateDifference(0, -1).is_straight_direction())
        self.assertTrue(CoordinateDifference(0, -8).is_straight_direction())
        self.assertTrue(CoordinateDifference(-1, 0).is_straight_direction())
        self.assertTrue(CoordinateDifference(-8, 0).is_straight_direction())

        self.assertFalse(CoordinateDifference(0, 0).is_straight_direction())
        self.assertFalse(CoordinateDifference(1, 1).is_straight_direction())
        self.assertFalse(CoordinateDifference(-1, -1).is_straight_direction())
        self.assertFalse(CoordinateDifference(1, 3).is_straight_direction())
        self.assertFalse(CoordinateDifference(-1, -3).is_straight_direction())


    def test_is_diagonal_direction(self):
        self.assertTrue(CoordinateDifference(1, 1).is_diagonal_direction())
        self.assertTrue(CoordinateDifference(8, 8).is_diagonal_direction())
        self.assertTrue(CoordinateDifference(-1, -1).is_diagonal_direction())
        self.assertTrue(CoordinateDifference(-8, -8).is_diagonal_direction())

        self.assertFalse(CoordinateDifference(0, 0).is_diagonal_direction())
        self.assertFalse(CoordinateDifference(0, 1).is_diagonal_direction())
        self.assertFalse(CoordinateDifference(0, 8).is_diagonal_direction())
        self.assertFalse(CoordinateDifference(1, 0).is_diagonal_direction())
        self.assertFalse(CoordinateDifference(8, 0).is_diagonal_direction())
        self.assertFalse(CoordinateDifference(0, -1).is_diagonal_direction())
        self.assertFalse(CoordinateDifference(0, -8).is_diagonal_direction())
        self.assertFalse(CoordinateDifference(-1, 0).is_diagonal_direction())
        self.assertFalse(CoordinateDifference(-8, 0).is_diagonal_direction())

        self.assertFalse(CoordinateDifference(2, 1).is_diagonal_direction())
        self.assertFalse(CoordinateDifference(2, 8).is_diagonal_direction())
        self.assertFalse(CoordinateDifference(1, 2).is_diagonal_direction())
        self.assertFalse(CoordinateDifference(8, 2).is_diagonal_direction())
        self.assertFalse(CoordinateDifference(-2, -1).is_diagonal_direction())
        self.assertFalse(CoordinateDifference(-2, -8).is_diagonal_direction())
        self.assertFalse(CoordinateDifference(-1, -2).is_diagonal_direction())
        self.assertFalse(CoordinateDifference(-8, -2).is_diagonal_direction())


    def test_equality(self):
        self.assertEqual(CoordinateDifference(1, 1), CoordinateDifference(1, 1))
        self.assertNotEqual(CoordinateDifference(0, 0), CoordinateDifference(1, 1))


class ChessTestCoordinates(BaseChessTest):

    def test_creation(self):
        row = 1
        col = 5
        coordinate = Coordinate(row, col)
        self.assertEqual(coordinate.row, row, 'Row not matching')
        self.assertEqual(coordinate.col, col, 'Col not matching')


    def test_distance(self):
        from_coordinate = Coordinate(1, 1)
        to_coordinate = Coordinate(5, 3)
        distance = from_coordinate.get_difference_to_other(to_coordinate)
        self.assertEqual(distance.row_diff, 4, 'Row distance not matching')
        self.assertEqual(distance.col_diff, 2, 'Col distance not matching')


    def test_get_number_of_fields_on_way_to_other(self):
        start = self.DEFAULT_START_COORDINATE
        self.assertEqual(start.get_number_of_fields_between(start), 0)
        self.assertEqual(start.get_number_of_fields_between(ChessCoordinate('c5')), 0)
        self.assertEqual(start.get_number_of_fields_between(ChessCoordinate('e5')), 0)
        self.assertEqual(start.get_number_of_fields_between(ChessCoordinate('d4')), 0)
        self.assertEqual(start.get_number_of_fields_between(ChessCoordinate('d6')), 0)

        self.assertEqual(start.get_number_of_fields_between(ChessCoordinate('d7')), 1)
        self.assertEqual(start.get_number_of_fields_between(ChessCoordinate('d1')), 3)
        self.assertEqual(start.get_number_of_fields_between(ChessCoordinate('a5')), 2)
        self.assertEqual(start.get_number_of_fields_between(ChessCoordinate('h5')), 3)

        with self.assertRaises(ChessError):
            for invalid_coordinate in self.DEFAULT_START_KNIGHT_MOVES:
                start.get_number_of_fields_between(ChessCoordinate(invalid_coordinate))
                pass


    def test_equal(self):
        self.assertEqual(Coordinate(1, 1), Coordinate(1, 1))
        self.assertNotEqual(Coordinate(1, 1), Coordinate(1, 2))


class TestChessCoordinate(unittest.TestCase):

    def test_get_col_value_from_char(self):
        self.assertEqual(ChessCoordinate.get_col_value_from_char('a'), 0)
        self.assertEqual(ChessCoordinate.get_col_value_from_char('A'), 0)
        self.assertEqual(ChessCoordinate.get_col_value_from_char('h'), 7)
        self.assertEqual(ChessCoordinate.get_col_value_from_char('H'), 7)

        with self.assertRaises(ChessError):
            ChessCoordinate.get_col_value_from_char('i')
            ChessCoordinate.get_col_value_from_char('j')
            ChessCoordinate.get_col_value_from_char('I')
            ChessCoordinate.get_col_value_from_char('I')
            ChessCoordinate.get_col_value_from_char(chr(ord('a') - 1))
            ChessCoordinate.get_col_value_from_char(chr(ord('A') - 1))
            ChessCoordinate.get_col_value_from_char('aa')
            ChessCoordinate.get_col_value_from_char('hh')
            ChessCoordinate.get_col_value_from_char('')


    def test_get_row_value_from_char(self):
        self.assertEqual(ChessCoordinate.get_row_value_from_char('1'), 7)
        self.assertEqual(ChessCoordinate.get_row_value_from_char('8'), 0)

        with self.assertRaises(ChessError):
            ChessCoordinate.get_row_value_from_char('11')
            ChessCoordinate.get_row_value_from_char('88')
            ChessCoordinate.get_row_value_from_char('')
            ChessCoordinate.get_row_value_from_char('9')
            ChessCoordinate.get_row_value_from_char('0')


    def test_init(self):
        coordinate_lower = ChessCoordinate('a8')
        self.assertEqual(coordinate_lower.row, 0)
        self.assertEqual(coordinate_lower.col, 0)

        coordinate_upper = ChessCoordinate('A8')
        self.assertEqual(coordinate_upper.row, 0)
        self.assertEqual(coordinate_upper.col, 0)

        coordinate_lower = ChessCoordinate('b5')
        self.assertEqual(coordinate_lower.row, 3)
        self.assertEqual(coordinate_lower.col, 1)

        coordinate_upper = ChessCoordinate('C4')
        self.assertEqual(coordinate_upper.row, 4)
        self.assertEqual(coordinate_upper.col, 2)

        with self.assertRaises(ChessError):
            ChessCoordinate('a0')
            ChessCoordinate('a9')
            ChessCoordinate('a10')
            ChessCoordinate('.10')
            ChessCoordinate('!10')


class TestMove(BaseChessTest):

    def test_make_from_tuples(self):
        from_tuple = (0, 0)
        to_tuple = (4, 4)
        move = Move.make_from_tuples(from_tuple, to_tuple)

        self.assertEqual(move.from_coordinate.row, from_tuple[0])
        self.assertEqual(move.from_coordinate.col, from_tuple[1])
        self.assertEqual(move.to_coordinate.row, to_tuple[0])
        self.assertEqual(move.to_coordinate.col, to_tuple[1])


if __name__ == '__main__':
    unittest.main()
