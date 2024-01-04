from logic.ChessError import ChessError
from logic.Color import Color
from logic.BoardNavigation import Coordinate
from logic.pieces.Bishop import Bishop
from logic.pieces.ChessPiece import ChessPiece
from logic.pieces.King import King
from logic.pieces.Knight import Knight
from logic.pieces.Pawn import Pawn
from logic.pieces.Queen import Queen
from logic.pieces.Rook import Rook


class ChessBoard:
    NUMBER_OF_FIELDS: int = 8
    OUTPUT_SPACE: int = 1
    SIGN_BLANK: str = u'\u2003'
    SIGN_DASH: str = u'\u2015'
    OUTPUT_PLACEHOLDER: str = SIGN_BLANK

    fields: list[list[ChessPiece | None]]

    def __init__(self):
        self.fields = [[None for _ in range(self.NUMBER_OF_FIELDS)] for _ in range(self.NUMBER_OF_FIELDS)]


    def get_piece_at_coordinate(self, coordinate: Coordinate):
        return self.fields[coordinate.row][coordinate.col]


    def has_piece_at(self, coordinate: Coordinate):
        return self.get_piece_at_coordinate(coordinate) is not None


    def put_piece(self, coordinate: Coordinate, piece: ChessPiece):
        if self.fields[coordinate.row][coordinate.col]:
            raise ChessError(f"Coordinate already blocked: {coordinate}")
        self.fields[coordinate.row][coordinate.col] = piece


    def put_starting_pawns(self, color: Color):
        for i in range(self.NUMBER_OF_FIELDS):
            self.put_piece(Coordinate(color.get_pawn_row(), i), Pawn(color=color))


    def put_starting_pieces_for_color(self, color: Color):
        self.put_piece(Coordinate(color.get_king_row(), 0), Rook(color=color))
        self.put_piece(Coordinate(color.get_king_row(), 7), Rook(color=color))
        self.put_piece(Coordinate(color.get_king_row(), 1), Knight(color=color))
        self.put_piece(Coordinate(color.get_king_row(), 6), Knight(color=color))
        self.put_piece(Coordinate(color.get_king_row(), 2), Bishop(color=color))
        self.put_piece(Coordinate(color.get_king_row(), 5), Bishop(color=color))
        self.put_piece(Coordinate(color.get_king_row(), 3), Queen(color=color))
        self.put_piece(Coordinate(color.get_king_row(), 4), King(color=color))

        self.put_starting_pawns(color=color)


    def put_starting_pieces(self):
        for c in Color:
            self.put_starting_pieces_for_color(c)


    def check_is_valid_move(self, from_coordinate: Coordinate, to_coordinate: Coordinate) -> bool:
        # piece is movable
        if not self.has_piece_at(from_coordinate):
            raise ChessError(f"No piece at {from_coordinate}")

        # destination field is not blocked by own piece
        piece_to_move = self.get_piece_at_coordinate(from_coordinate)
        if self.has_piece_of_color_at(to_coordinate, piece_to_move.color):
            raise ChessError(f"Piece of same color at {to_coordinate}")

        # piece can move there
        if piece_to_move.is_impossible_move(from_coordinate, to_coordinate):
            raise ChessError(f"Piece can not move from {from_coordinate} to {to_coordinate}")

        # no piece in the way
        if self.has_pieces_at_coordinates(piece_to_move.get_moved_over_fields(from_coordinate, to_coordinate)):
            raise ChessError(f"Pieces in the way between {from_coordinate} and {to_coordinate}")

        return True

    def has_piece_of_color_at(self, coordinate: Coordinate, color: Color):
        return self.has_piece_at(coordinate) and (self.get_piece_at_coordinate(coordinate).color == color)


    def has_pieces_at_coordinates(self, coordinates: list[Coordinate]):
        for c in coordinates:
            if self.has_piece_at(c):
                return True
        return False


    @staticmethod
    def make_with_pieces():
        board = ChessBoard()
        board.put_starting_pieces()
        return board


    def __str__(self):
        output: str = ''
        space_of_sign = len(self.OUTPUT_PLACEHOLDER)
        space_per_column = space_of_sign + (self.OUTPUT_SPACE * 2)
        space_signs = self.OUTPUT_SPACE * self.SIGN_BLANK
        row_line = '+' + (self.SIGN_DASH * space_per_column + '+') * self.NUMBER_OF_FIELDS + '\n'
        output += row_line
        for row in self.fields:
            output += '|' + ''.join((space_signs + (i.get_sign() if i else self.OUTPUT_PLACEHOLDER) + space_signs + '|' for i in row)) + '\n'
            output += row_line
        return output



if __name__ == '__main__':
    fields = ChessBoard.make_with_pieces()
    print(fields)
