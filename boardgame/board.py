from typing import List, Union

from boardgame.piece import Piece
from boardgame.position import Position

from boardgame.board_exception import BoardException


class Board(object):

    def __init__(self, rows: int, columns: int) -> None:

        if rows < 1 or columns < 1:
            raise BoardException('Error creating board: there must be at least 1 row and 1 column.')

        self.__rows = rows
        self.__columns = columns
        self.__pieces: List[List[Union[Piece, None]]] = []
        for i in range(rows):
            row = []
            for j in range(columns):
                row.append(None)
            self.__pieces.append(row)

    @property
    def rows(self) -> int:
        return self.__rows

    @property
    def columns(self) -> int:
        return self.__columns

    def piece_by_row_and_column(self, row: int, column: int) -> Union[Piece, None]:

        if not self.position_exists(row, column):
            raise BoardException('Position not on the board.')

        return self.__pieces[row][column]

    def piece_by_position(self, position: Position) -> Union[Piece, None]:

        if not self.position_exists_by_position(position):
            raise BoardException('Position not on the board.')

        return self.__pieces[position.row][position.column]

    def place_piece(self, piece: Piece, position: Position) -> None:

        if self.there_is_a_piece(position):
            raise BoardException(f'There is already a piece on position: {position}')

        row = position.row
        column = position.column

        self.__pieces[row][column] = piece
        piece._position = position

    def remove_piece(self, position: Position) -> Union[Piece, None]:

        if not self.position_exists_by_position(position):
            raise BoardException('Position not on the board.')

        if self.piece_by_position(position) is None:
            return None

        piece: Piece = self.piece_by_position(position)
        piece._position = None

        row: int = position.row
        column: int = position.column

        self.__pieces[row][column] = None

        return piece

    def position_exists(self, row: int, column: int) -> bool:
        return 0 <= row < self.__rows and 0 <= column < self.__columns

    def position_exists_by_position(self, position: Position) -> bool:
        return self.position_exists(position.row, position.column)

    def there_is_a_piece(self, position: Position) -> bool:

        if not self.position_exists_by_position(position):
            raise BoardException('Position not on the board.')

        return self.piece_by_position(position) is not None
