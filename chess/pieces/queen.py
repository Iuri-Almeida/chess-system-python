from typing import List

from boardgame.board import Board
from boardgame.position import Position

from chess.chess_piece import ChessPiece
from chess.color import Color


class Queen(ChessPiece):

    def __init__(self, board: Board, color: Color) -> None:
        super().__init__(board, color)

    def __str__(self) -> str:
        return 'Q'

    def possible_moves(self) -> List[List[bool]]:

        rows: int = self._board.rows
        columns: int = self._board.columns

        mat: List[List[bool]] = []
        for _ in range(rows):
            row: List[bool] = []
            for _ in range(columns):
                row.append(False)
            mat.append(row)

        # auxiliary position
        aux: Position = Position(0, 0)

        # piece position
        row: int = self._position.row
        column: int = self._position.column

        # up
        aux.set_values(row - 1, column)
        while self._board.position_exists_by_position(aux) and not self._board.there_is_a_piece(aux):
            mat[aux.row][aux.column] = True
            aux.row -= 1
        if self._board.position_exists_by_position(aux) and self._is_there_opponent_piece(aux):
            mat[aux.row][aux.column] = True

        # right-up
        aux.set_values(row - 1, column + 1)
        while self._board.position_exists_by_position(aux) and not self._board.there_is_a_piece(aux):
            mat[aux.row][aux.column] = True
            aux.set_values(aux.row - 1, aux.column + 1)
        if self._board.position_exists_by_position(aux) and self._is_there_opponent_piece(aux):
            mat[aux.row][aux.column] = True

        # right
        aux.set_values(row, column + 1)
        while self._board.position_exists_by_position(aux) and not self._board.there_is_a_piece(aux):
            mat[aux.row][aux.column] = True
            aux.column += 1
        if self._board.position_exists_by_position(aux) and self._is_there_opponent_piece(aux):
            mat[aux.row][aux.column] = True

        # right-down
        aux.set_values(row + 1, column + 1)
        while self._board.position_exists_by_position(aux) and not self._board.there_is_a_piece(aux):
            mat[aux.row][aux.column] = True
            aux.set_values(aux.row + 1, aux.column + 1)
        if self._board.position_exists_by_position(aux) and self._is_there_opponent_piece(aux):
            mat[aux.row][aux.column] = True

        # down
        aux.set_values(row + 1, column)
        while self._board.position_exists_by_position(aux) and not self._board.there_is_a_piece(aux):
            mat[aux.row][aux.column] = True
            aux.row += 1
        if self._board.position_exists_by_position(aux) and self._is_there_opponent_piece(aux):
            mat[aux.row][aux.column] = True

        # left-down
        aux.set_values(row + 1, column - 1)
        while self._board.position_exists_by_position(aux) and not self._board.there_is_a_piece(aux):
            mat[aux.row][aux.column] = True
            aux.set_values(aux.row + 1, aux.column - 1)
        if self._board.position_exists_by_position(aux) and self._is_there_opponent_piece(aux):
            mat[aux.row][aux.column] = True

        # left
        aux.set_values(row, column - 1)
        while self._board.position_exists_by_position(aux) and not self._board.there_is_a_piece(aux):
            mat[aux.row][aux.column] = True
            aux.column -= 1
        if self._board.position_exists_by_position(aux) and self._is_there_opponent_piece(aux):
            mat[aux.row][aux.column] = True

        # left-up
        aux.set_values(row - 1, column - 1)
        while self._board.position_exists_by_position(aux) and not self._board.there_is_a_piece(aux):
            mat[aux.row][aux.column] = True
            aux.set_values(aux.row - 1, aux.column - 1)
        if self._board.position_exists_by_position(aux) and self._is_there_opponent_piece(aux):
            mat[aux.row][aux.column] = True

        return mat
