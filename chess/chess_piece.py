from abc import ABC

from boardgame.piece import Piece
from boardgame.board import Board
from chess.color import Color


class ChessPiece(Piece, ABC):

    def __init__(self, board: Board, color: Color) -> None:
        self.__color = color
        super().__init__(board)

    @property
    def color(self) -> Color:
        return self.__color
