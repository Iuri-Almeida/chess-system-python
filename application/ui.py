from typing import List, Union

from chess.chess_piece import ChessPiece
from chess.color import Color
from application.color_constants import ColorConstants


class UI(object):

    @staticmethod
    def print_board(pieces: List[List[Union[ChessPiece, None]]]) -> None:

        rows = len(pieces)
        columns = len(pieces[0])

        for i in range(rows):

            print(f'{rows - i} ', end='')

            for j in range(columns):

                UI.print_piece(pieces[i][j])

            print()

        print('  a b c d e f g h')

    @staticmethod
    def print_piece(piece: ChessPiece) -> None:

        if piece is None:
            print('-', end='')
        else:
            if piece.color == Color.WHITE:
                print(piece, end='')
            else:
                print(f'{ColorConstants.COLOR_YELLOW}{piece}{ColorConstants.RESET}', end='')

        print(' ', end='')
