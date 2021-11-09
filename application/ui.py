from typing import List, Union

from chess.chess_piece import ChessPiece


class UI(object):

    @staticmethod
    def print_board(pieces: List[List[Union[ChessPiece, None]]]):

        rows = len(pieces)
        columns = len(pieces[0])

        for i in range(rows):

            print(f'{rows - i} ', end='')

            for j in range(columns):
                piece: ChessPiece = pieces[i][j]
                print(f'{"-" if piece is None else piece} ', end='')

            print()

        print('  a b c d e f g h')
