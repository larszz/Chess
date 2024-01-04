import unittest

from logic.ChessBoard import ChessBoard
from logic.ChessError import ChessError
from logic.Color import Color
from logic.BoardNavigation import Coordinate, ChessCoordinate


class TestChessboard(unittest.TestCase):

    def setUp(self) -> None:
        self.empty_board = ChessBoard()
        self.default_board = ChessBoard.make_with_pieces()


    def test_check_dimensions(self):
        self.assertEqual(len(self.empty_board.fields), self.empty_board.NUMBER_OF_FIELDS, "Wrong number of rows")
        for i in range(len(self.empty_board.fields)):
            self.assertEqual(len(self.empty_board.fields[i]), self.empty_board.NUMBER_OF_FIELDS,
                             f"Wrong number of columns in column {i}")


    def test_sign_length(self):
        for row in ChessBoard.make_with_pieces().fields:
            for item in row:
                self.assertTrue(len(item.sign if item else ChessBoard.OUTPUT_PLACEHOLDER) == 1)


    def test_is_valid_move(self):
        # piece at from coor
        # self.assertTrue(self.default_board.check_is_valid_move(ChessCoordinate('b1'), ChessCoordinate('d1')))


        with self.assertRaises(ChessError):
            self.default_board.check_is_valid_move(ChessCoordinate('c1'), ChessCoordinate('d1'))
            self.default_board.check_is_valid_move(ChessCoordinate('a1'), ChessCoordinate('b1'))
            self.default_board.check_is_valid_move(ChessCoordinate('a1'), ChessCoordinate('h1'))


    def test_has_piece_of_color_at(self):
        self.assertTrue(self.default_board.has_piece_of_color_at(ChessCoordinate('b8'), Color.BLACK))
        self.assertFalse(self.default_board.has_piece_of_color_at(ChessCoordinate('b1'), Color.BLACK))


    def test_has_pieces_at_coordinates(self):
        self.assertFalse(self.default_board.has_pieces_at_coordinates([Coordinate(i+2, i) for i in range(3)]))
        self.assertTrue(self.default_board.has_pieces_at_coordinates([Coordinate(0, i) for i in range(0, 3)]))


if __name__ == '__main__':
    unittest.main()
