from typing import List
from abc import ABC

from chess.chess_piece import ChessPiece
from chess.color import Color
from boardgame.board import Board
from boardgame.position import Position


class King(ChessPiece, ABC):

    def __init__(self, board: Board, color: Color) -> None:
        super().__init__(board, color)

    def __str__(self) -> str:
        return 'K'

    def possible_moves(self) -> List[List[bool]]:

        rows: int = self._board.rows
        columns: int = self._board.columns

        mat: List[List[bool]] = []
        for i in range(rows):
            row: List[bool] = []
            for j in range(columns):
                row.append(False)
            mat.append(row)

        # auxiliary position
        aux: Position = Position(0, 0)

        # piece position
        row: int = self._position.row
        column: int = self._position.column

        # up
        aux.set_values(row - 1, column)
        if self._board.position_exists_by_position(aux) and self.__can_move(aux):
            mat[aux.row][aux.column] = True

        # right-up
        aux.set_values(row - 1, column + 1)
        if self._board.position_exists_by_position(aux) and self.__can_move(aux):
            mat[aux.row][aux.column] = True

        # right
        aux.set_values(row, column + 1)
        if self._board.position_exists_by_position(aux) and self.__can_move(aux):
            mat[aux.row][aux.column] = True

        # right-down
        aux.set_values(row + 1, column + 1)
        if self._board.position_exists_by_position(aux) and self.__can_move(aux):
            mat[aux.row][aux.column] = True

        # down
        aux.set_values(row + 1, column)
        if self._board.position_exists_by_position(aux) and self.__can_move(aux):
            mat[aux.row][aux.column] = True

        # left-down
        aux.set_values(row + 1, column - 1)
        if self._board.position_exists_by_position(aux) and self.__can_move(aux):
            mat[aux.row][aux.column] = True

        # left
        aux.set_values(row, column - 1)
        if self._board.position_exists_by_position(aux) and self.__can_move(aux):
            mat[aux.row][aux.column] = True

        # left-up
        aux.set_values(row - 1, column - 1)
        if self._board.position_exists_by_position(aux) and self.__can_move(aux):
            mat[aux.row][aux.column] = True

        return mat

    def __can_move(self, position: Position) -> bool:
        piece: ChessPiece = self._board.piece_by_position(position)
        return piece is None or piece.color != self.color
