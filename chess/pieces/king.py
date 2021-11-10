from typing import List
from abc import ABC

from boardgame.board import Board
from boardgame.position import Position

# from chess.chess_match import ChessMatch
from chess.chess_piece import ChessPiece
from chess.color import Color

from chess.pieces.rook import Rook


class King(ChessPiece, ABC):

    def __init__(self, board: Board, color: Color, chess_match) -> None:
        super().__init__(board, color)
        self.__chess_match = chess_match

    def __str__(self) -> str:
        return 'K'

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

        # SPECIAL MOVE - CASTLING
        if self.move_count == 0 and not self.__chess_match.check:

            # Castling - King side
            pos_rook_01: Position = Position(row, column + 3)
            if self.__test_rook_castling(pos_rook_01):

                pos_01: Position = Position(row, column + 1)
                pos_02: Position = Position(row, column + 2)

                if self._board.piece_by_position(pos_01) is None and\
                        self._board.piece_by_position(pos_02) is None:
                    mat[row][column + 2] = True

            # Castling - Queen side
            pos_rook_02: Position = Position(row, column - 4)
            if self.__test_rook_castling(pos_rook_02):

                pos_01: Position = Position(row, column - 1)
                pos_02: Position = Position(row, column - 2)
                pos_03: Position = Position(row, column - 3)

                if self._board.piece_by_position(pos_01) is None and\
                        self._board.piece_by_position(pos_02) is None and\
                        self._board.piece_by_position(pos_03) is None:
                    mat[row][column - 2] = True

        return mat

    def __can_move(self, position: Position) -> bool:
        piece: ChessPiece = self._board.piece_by_position(position)
        return piece is None or piece.color != self.color

    def __test_rook_castling(self, position: Position) -> bool:
        piece: ChessPiece = self._board.piece_by_position(position)
        return piece is not None and isinstance(piece, Rook) and piece.color == self.color and piece.move_count == 0
