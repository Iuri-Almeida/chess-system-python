from typing import List
from abc import ABC

from chess.chess_piece import ChessPiece
from chess.color import Color
from boardgame.board import Board
from boardgame.position import Position


class Pawn(ChessPiece, ABC):

    def __init__(self, board: Board, color: Color) -> None:
        super().__init__(board, color)

    def __str__(self) -> str:
        return 'P'

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

        if self.color == Color.WHITE:

            # up one
            aux.set_values(row - 1, column)
            if self._board.position_exists_by_position(aux) and not self._board.there_is_a_piece(aux):
                mat[aux.row][aux.column] = True

            # up two
            aux.set_values(row - 2, column)
            aux_2: Position = Position(row - 2, column)
            if self._board.position_exists_by_position(aux) and not self._board.there_is_a_piece(aux) and\
                    self._board.position_exists_by_position(aux_2) and not self._board.there_is_a_piece(aux_2) and\
                    self.move_count == 0:
                mat[aux.row][aux.column] = True

            # up right
            aux.set_values(row - 1, column + 1)
            if self._board.position_exists_by_position(aux) and self._is_there_opponent_piece(aux):
                mat[aux.row][aux.column] = True

            # up left
            aux.set_values(row - 1, column - 1)
            if self._board.position_exists_by_position(aux) and self._is_there_opponent_piece(aux):
                mat[aux.row][aux.column] = True

        else:

            # down one
            aux.set_values(row + 1, column)
            if self._board.position_exists_by_position(aux) and not self._board.there_is_a_piece(aux):
                mat[aux.row][aux.column] = True

            # down two
            aux.set_values(row + 2, column)
            aux_2: Position = Position(row + 2, column)
            if self._board.position_exists_by_position(aux) and not self._board.there_is_a_piece(aux) and \
                    self._board.position_exists_by_position(aux_2) and not self._board.there_is_a_piece(aux_2) and \
                    self.move_count == 0:
                mat[aux.row][aux.column] = True

            # down right
            aux.set_values(row + 1, column + 1)
            if self._board.position_exists_by_position(aux) and self._is_there_opponent_piece(aux):
                mat[aux.row][aux.column] = True

            # down left
            aux.set_values(row + 1, column - 1)
            if self._board.position_exists_by_position(aux) and self._is_there_opponent_piece(aux):
                mat[aux.row][aux.column] = True

        return mat
