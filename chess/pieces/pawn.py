from typing import List
from abc import ABC

from boardgame.board import Board
from boardgame.position import Position

# from chess.chess_match import ChessMatch
from chess.chess_piece import ChessPiece
from chess.color import Color


class Pawn(ChessPiece, ABC):

    def __init__(self, board: Board, color: Color, chess_match) -> None:
        super().__init__(board, color)
        self.__chess_match = chess_match

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

            # SPECIAL MOVE - EN PASSANT
            if row == 3:

                left_opponent: Position = Position(row, column - 1)
                if self._board.position_exists_by_position(left_opponent) and\
                    self._is_there_opponent_piece(left_opponent) and\
                        self._board.piece_by_position(left_opponent) == self.__chess_match.en_passant_vulnerable:
                    mat[left_opponent.row - 1][left_opponent.column] = True

                right_opponent: Position = Position(row, column + 1)
                if self._board.position_exists_by_position(right_opponent) and\
                    self._is_there_opponent_piece(right_opponent) and\
                        self._board.piece_by_position(right_opponent) == self.__chess_match.en_passant_vulnerable:
                    mat[right_opponent.row - 1][right_opponent.column] = True

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

            # SPECIAL MOVE - EN PASSANT
            if row == 4:

                left_opponent: Position = Position(row, column - 1)
                if self._board.position_exists_by_position(left_opponent) and \
                        self._is_there_opponent_piece(left_opponent) and \
                        self._board.piece_by_position(left_opponent) == self.__chess_match.en_passant_vulnerable:
                    mat[left_opponent.row + 1][left_opponent.column] = True

                right_opponent: Position = Position(row, column + 1)
                if self._board.position_exists_by_position(right_opponent) and \
                        self._is_there_opponent_piece(right_opponent) and \
                        self._board.piece_by_position(right_opponent) == self.__chess_match.en_passant_vulnerable:
                    mat[right_opponent.row + 1][right_opponent.column] = True

        return mat
