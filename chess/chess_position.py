from boardgame.position import Position
from chess.chess_constants import ChessConstants
from chess.chess_exception import ChessException


class ChessPosition(object):

    def __init__(self, column: str, row: int) -> None:

        if column < ChessConstants.FIRST_COLUMN or column > ChessConstants.LAST_COLUMN \
                or row < 1 or row > ChessConstants.ROWS:
            raise ChessException('Error instantiating ChessPosition. Valid values are from a1 to h8.')

        self.__row = row
        self.__column = column

    def __str__(self) -> str:
        return f'{self.column}{self.row}'

    @property
    def row(self) -> int:
        return self.__row

    @property
    def column(self) -> str:
        return self.__column

    def to_position(self) -> Position:

        row = ChessConstants.ROWS - self.__row
        board_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        column = board_alpha.index(self.__column) - board_alpha.index(ChessConstants.FIRST_COLUMN)

        return Position(row, column)

    @staticmethod
    def from_position(position: Position):

        row = ChessConstants.ROWS - position.row
        board_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        column = board_alpha[board_alpha.index(ChessConstants.FIRST_COLUMN) - position.column]

        return ChessPosition(column, row)
