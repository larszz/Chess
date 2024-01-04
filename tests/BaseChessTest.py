import unittest
from typing import Type

from logic.BoardNavigation import Coordinate
from logic.Color import Color
from logic.pieces.ChessPiece import ChessPiece


class BaseChessTest(unittest.TestCase):
    tested_class: Type[ChessPiece]
    DEFAULT_PIECE_COLOR = Color.WHITE
    DEFAULT_START_COORDINATE: Coordinate = Coordinate(3, 3)  # == 'd5'
    DEFAULT_START_KNIGHT_MOVES: list[str] = ['c7', 'b6', 'b4', 'c3', 'e3', 'f4', 'f6', 'e7', ]

    def get_piece_for_testing(self):
        return self.tested_class(self.DEFAULT_PIECE_COLOR)


if __name__ == '__main__':
    unittest.main()
