from abc import ABC

from boardgame.piece import Piece
from boardgame.board import Board
from boardgame.position import Position
from chess.color import Color


class ChessPiece(Piece, ABC):

    def __init__(self, board: Board, color: Color) -> None:
        self.__color = color
        super().__init__(board)

    @property
    def color(self) -> Color:
        return self.__color

    def is_there_opponent_piece(self, position: Position) -> bool:
        piece: ChessPiece = self._board.piece_by_position(position)
        return piece is not None and piece.color != self.color
