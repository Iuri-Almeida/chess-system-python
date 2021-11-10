from typing import List, Union
from os import system

from chess.chess_piece import ChessPiece
from chess.chess_position import ChessPosition
from chess.chess_match import ChessMatch
from chess.color import Color
from application.program_constants import ProgramConstants


class UI(object):

    @staticmethod
    def clear_screen() -> None:
        system('clear')

    @staticmethod
    def read_chess_position(txt: str) -> ChessPosition:

        try:
            s: str = input(txt)

            column: str = s[0]
            row: int = int(s[1:])

            return ChessPosition(column, row)
        except RuntimeError:
            raise ValueError('Error reading ChessPosition. Valida values are from a1 to h8.')

    @staticmethod
    def print_match(chess_match: ChessMatch, captured: List[ChessPiece]) -> None:

        game_status: str = ProgramConstants.NO_CHECK

        UI.print_board(chess_match.get_pieces())

        print()
        UI.__print_captured_pieces(captured)

        print(f'\nTurn: {chess_match.turn}')

        if not chess_match.checkmate:
            print(f'Waiting player: {chess_match.current_player}')
            if chess_match.check:
                game_status = ProgramConstants.CHECK
        else:
            game_status = ProgramConstants.CHECKMATE

            player: Color = chess_match.current_player

            print(
                f'Winner: '
                f'{ProgramConstants.BLACK_PIECE_COLOR if player == Color.BLACK else ProgramConstants.WHITE_PIECE_COLOR}'
                f'{player}{ProgramConstants.RESET_COLOR}')

        print(f'\nGame status: {ProgramConstants.GAME_STATUS_COLOR}{game_status}{ProgramConstants.RESET_COLOR}')

    @staticmethod
    def print_board(pieces: List[List[Union[ChessPiece, None]]]) -> None:

        rows: int = len(pieces)
        columns: int = len(pieces[0])

        for i in range(rows):

            print(f'{ProgramConstants.INDICATORS_COLOR}{rows - i} {ProgramConstants.RESET_COLOR}', end='')

            for j in range(columns):

                UI.__print_piece(pieces[i][j], False)

            print()

        print(f'{ProgramConstants.INDICATORS_COLOR}  a b c d e f g h{ProgramConstants.RESET_COLOR}')

    @staticmethod
    def print_board_possible_moves(
            pieces: List[List[Union[ChessPiece, None]]], possible_moves: List[List[bool]]) -> None:

        rows: int = len(pieces)
        columns: int = len(pieces[0])

        for i in range(rows):

            print(f'{ProgramConstants.INDICATORS_COLOR}{rows - i} {ProgramConstants.RESET_COLOR}', end='')

            for j in range(columns):

                UI.__print_piece(pieces[i][j], possible_moves[i][j])

            print()

        print(f'{ProgramConstants.INDICATORS_COLOR}  a b c d e f g h{ProgramConstants.RESET_COLOR}')

    @staticmethod
    def __print_piece(piece: ChessPiece, background: bool) -> None:

        if background:
            print(ProgramConstants.BACKGROUND_COLOR, end='')

        if piece is None:
            print(f'-{ProgramConstants.RESET_COLOR}', end='')
        else:
            if piece.color == Color.WHITE:
                print(f'{ProgramConstants.WHITE_PIECE_COLOR}{piece}{ProgramConstants.RESET_COLOR}', end='')
            else:
                print(f'{ProgramConstants.BLACK_PIECE_COLOR}{piece}{ProgramConstants.RESET_COLOR}', end='')

        print(' ', end='')

    @staticmethod
    def __print_captured_pieces(captured: List[ChessPiece]) -> None:

        white: List[ChessPiece] = list(filter(lambda x: x.color == Color.WHITE, captured))
        black: List[ChessPiece] = list(filter(lambda x: x.color == Color.BLACK, captured))

        for i in range(len(white)):
            white[i] = str(white[i])

        for i in range(len(black)):
            black[i] = str(black[i])

        print('Captured pieces:')
        print(f'{ProgramConstants.WHITE_PIECE_COLOR}White: {", ".join(white)}{ProgramConstants.RESET_COLOR}')
        print(f'{ProgramConstants.BLACK_PIECE_COLOR}Black: {", ".join(black)}{ProgramConstants.RESET_COLOR}')
