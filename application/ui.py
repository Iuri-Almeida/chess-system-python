from typing import List, Optional
from os import system

from application.program_constants import ProgramConstants

from chess.chess_match import ChessMatch
from chess.chess_piece import ChessPiece
from chess.chess_position import ChessPosition
from chess.color import Color


class UI(object):

    @staticmethod
    def clear_screen() -> None:
        system('clear')

    @staticmethod
    def read_chess_position(txt: str, chess_match: ChessMatch) -> ChessPosition:

        try:

            player: Color = chess_match.current_player

            s: str = input(f'{txt}'
            f'{ProgramConstants.BLACK_PIECE_COLOR if player == Color.BLACK else ProgramConstants.WHITE_PIECE_COLOR}').lower()
            print(ProgramConstants.RESET_COLOR)

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

        print(f'\nTurn: {ProgramConstants.TURN_COLOR}{chess_match.turn}{ProgramConstants.RESET_COLOR}')

        if not chess_match.checkmate:

            player: Color = chess_match.current_player

            print(
                f'Waiting player: '
                f'{ProgramConstants.BLACK_PIECE_COLOR if player == Color.BLACK else ProgramConstants.WHITE_PIECE_COLOR}'
                f'{player.name}{ProgramConstants.RESET_COLOR}')
            
            if chess_match.check:
                game_status = ProgramConstants.CHECK
        else:
            game_status = ProgramConstants.CHECKMATE

            player: Color = chess_match.current_player

            print(
                f'Winner: '
                f'{ProgramConstants.BLACK_PIECE_COLOR if player == Color.BLACK else ProgramConstants.WHITE_PIECE_COLOR}'
                f'{player.name}{ProgramConstants.RESET_COLOR}')

        print(f'\nGame status: {ProgramConstants.GAME_STATUS_COLOR}{game_status}{ProgramConstants.RESET_COLOR}')

    @staticmethod
    def print_board(pieces: List[List[Optional[ChessPiece]]]) -> None:

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
            pieces: List[List[Optional[ChessPiece]]], possible_moves: List[List[bool]]) -> None:

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

        white: List[str] = [str(x) for x in captured if x.color == Color.WHITE]
        black: List[str] = [str(x) for x in captured if x.color == Color.BLACK]

        print('Captured pieces:')
        print(f'{ProgramConstants.WHITE_PIECE_COLOR}White: {white}{ProgramConstants.RESET_COLOR}')
        print(f'{ProgramConstants.BLACK_PIECE_COLOR}Black: {black}{ProgramConstants.RESET_COLOR}')
