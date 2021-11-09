from typing import List, Union

from boardgame.piece import Piece
from boardgame.position import Position


class Board(object):

    def __init__(self, rows: int, columns: int) -> None:
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
        return self.__pieces[row][column]

    def piece_by_position(self, position: Position):
        return self.__pieces[position.row][position.column]

    def place_piece(self, piece: Piece, position: Position) -> None:
        row = position.row
        column = position.column

        self.__pieces[row][column] = piece
        piece._position = position
