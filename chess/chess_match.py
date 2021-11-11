from typing import cast, List, Optional

from application.program_constants import ProgramConstants

from boardgame.board import Board
from boardgame.piece import Piece
from boardgame.position import Position

from chess.chess_exception import ChessException
from chess.chess_piece import ChessPiece
from chess.chess_position import ChessPosition
from chess.color import Color

from chess.pieces.bishop import Bishop
from chess.pieces.king import King
from chess.pieces.knight import Knight
from chess.pieces.pawn import Pawn
from chess.pieces.queen import Queen
from chess.pieces.rook import Rook


class ChessMatch(object):

    def __init__(self) -> None:
        self.__turn: int = 1
        self.__current_player: Color = Color.WHITE
        self.__board = Board(ProgramConstants.ROWS, ProgramConstants.COLUMNS)
        self.__check: bool = False
        self.__checkmate: bool = False
        self.__en_passant_vulnerable: Optional[ChessPiece] = None
        self.__promoted: Optional[ChessPiece] = None

        self.__pieces_on_the_board: List[Piece] = []
        self.__captured_pieces: List[Piece] = []

        self.__initial_setup()

    @property
    def turn(self) -> int:
        return self.__turn

    @property
    def current_player(self) -> Color:
        return self.__current_player

    @property
    def check(self) -> bool:
        return self.__check

    @property
    def checkmate(self) -> bool:
        return self.__checkmate

    @property
    def en_passant_vulnerable(self) -> Optional[ChessPiece]:
        return self.__en_passant_vulnerable

    @property
    def promoted(self) -> Optional[ChessPiece]:
        return self.__promoted

    def get_pieces(self) -> List[List[Optional[ChessPiece]]]:

        rows = self.__board.rows
        columns = self.__board.columns

        pieces: List[List[Optional[ChessPiece]]] = []
        for _ in range(rows):
            row = []
            for _ in range(columns):
                row.append(None)
            pieces.append(row)

        for i in range(rows):
            for j in range(columns):
                pieces[i][j] = self.__board.piece_by_row_and_column(i, j)

        return pieces

    def possible_moves(self, source_position: ChessPosition) -> List[List[bool]]:

        position: Position = source_position.to_position()

        self.__validate_source_position(position)

        return self.__board.piece_by_position(position).possible_moves()

    def perform_chess_move(self, source_position: ChessPosition, target_position: ChessPosition) -> ChessPiece:

        source: Position = source_position.to_position()
        target: Position = target_position.to_position()

        self.__validate_source_position(source)
        self.__validate_target_position(source, target)

        captured_piece = self.__make_move(source, target)

        if self.__test_check(self.__current_player):
            self.__undo_move(source, target, captured_piece)
            raise ChessException('You cannot put yourself in check.')

        moved_piece: ChessPiece = cast(ChessPiece, self.__board.piece_by_position(target))

        # SPECIAL MOVE - PROMOTION
        self.__promoted = None
        if isinstance(moved_piece, Pawn) and\
            ((moved_piece.color == Color.WHITE and target.row == 0) or
             (moved_piece.color == Color.BLACK and target.row == 7)):
            self.__promoted = self.__board.piece_by_position(target)
            self.__promoted = self.replace_promoted_piece('Q')

        self.__check = self.__test_check(self.__opponent(self.__current_player))

        self.__checkmate = self.__test_checkmate(self.__opponent(self.__current_player))

        if not self.checkmate:
            self.__next_turn()

        # SPECIAL MOVE - EN PASSANT
        if isinstance(moved_piece, Pawn) and (target.row == source.row - 2 or target.row == source.row + 2):
            self.__en_passant_vulnerable = moved_piece
        else:
            self.__en_passant_vulnerable = None

        return cast(ChessPiece, captured_piece)

    def replace_promoted_piece(self, promotion_type: str) -> ChessPiece:

        if self.promoted is None:
            raise ValueError('There is no piece to be promoted.')

        if not promotion_type == 'B' and not promotion_type == 'N' and\
                not promotion_type == 'R' and not promotion_type == 'Q':
            raise ValueError('Invalid type for promotion.')

        pos: Position = self.promoted.chess_position().to_position()
        piece: Piece = self.__board.remove_piece(pos)

        self.__pieces_on_the_board.remove(piece)

        new_piece: ChessPiece = self.__new_piece(promotion_type, self.promoted.color)

        self.__board.place_piece(new_piece, pos)
        self.__pieces_on_the_board.append(new_piece)

        return new_piece

    def __new_piece(self, promotion_type: str, color: Color) -> ChessPiece:

        if promotion_type == 'B':
            return Bishop(self.__board, color)
        elif promotion_type == 'N':
            return Knight(self.__board, color)
        elif promotion_type == 'R':
            return Rook(self.__board, color)
        else:
            return Queen(self.__board, color)

    def __make_move(self, source: Position, target: Position) -> Piece:

        piece: ChessPiece = cast(ChessPiece, self.__board.remove_piece(source))
        captured_piece: Piece = self.__board.remove_piece(target)

        piece.increase_move_count()

        self.__board.place_piece(piece, target)

        if captured_piece is not None:
            self.__pieces_on_the_board.remove(captured_piece)
            self.__captured_pieces.append(captured_piece)

        # SPECIAL MOVE - CASTLING (King side)
        if isinstance(piece, King) and target.column == source.column + 2:

            source_rook: Position = Position(source.row, source.column + 3)
            target_rook: Position = Position(source.row, source.column + 1)

            rook: ChessPiece = cast(ChessPiece, self.__board.remove_piece(source_rook))
            self.__board.place_piece(rook, target_rook)

            rook.increase_move_count()

        # SPECIAL MOVE - CASTLING (Queen side)
        if isinstance(piece, King) and target.column == source.column - 2:

            source_rook: Position = Position(source.row, source.column - 4)
            target_rook: Position = Position(source.row, source.column - 1)

            rook: ChessPiece = cast(ChessPiece, self.__board.remove_piece(source_rook))
            self.__board.place_piece(rook, target_rook)

            rook.increase_move_count()

        # SPECIAL MOVE - EN PASSANT
        if isinstance(piece, Pawn) and source.column != target.column and captured_piece is None:

            if piece.color == Color.WHITE:
                pos_pawn = Position(target.row + 1, target.column)
            else:
                pos_pawn = Position(target.row - 1, target.column)

            captured_piece = self.__board.remove_piece(pos_pawn)
            self.__pieces_on_the_board.remove(captured_piece)
            self.__captured_pieces.append(captured_piece)

        return captured_piece

    def __undo_move(self, source: Position, target: Position, captured_piece: Piece) -> None:

        piece: ChessPiece = cast(ChessPiece, self.__board.remove_piece(target))
        self.__board.place_piece(piece, source)

        piece.decrease_move_count()

        if captured_piece is not None:

            self.__board.place_piece(captured_piece, target)

            self.__captured_pieces.remove(captured_piece)
            self.__pieces_on_the_board.append(captured_piece)

        # SPECIAL MOVE - CASTLING (King side)
        if isinstance(piece, King) and target.column == source.column + 2:

            source_rook: Position = Position(source.row, source.column + 3)
            target_rook: Position = Position(source.row, source.column + 1)

            rook: ChessPiece = cast(ChessPiece, self.__board.remove_piece(target_rook))
            self.__board.place_piece(rook, source_rook)

            rook.decrease_move_count()

        # SPECIAL MOVE - CASTLING (Queen side)
        if isinstance(piece, King) and target.column == source.column - 2:

            source_rook: Position = Position(source.row, source.column - 4)
            target_rook: Position = Position(source.row, source.column - 1)

            rook: ChessPiece = cast(ChessPiece, self.__board.remove_piece(target_rook))
            self.__board.place_piece(rook, source_rook)

            rook.decrease_move_count()

        # SPECIAL MOVE - EN PASSANT
        if isinstance(piece, Pawn) and source.column != target.column and captured_piece == self.en_passant_vulnerable:

            pawn: ChessPiece = cast(ChessPiece, self.__board.remove_piece(target))

            if piece.color == Color.WHITE:
                pos_pawn = Position(3, target.column)
            else:
                pos_pawn = Position(4, target.column)

            self.__board.place_piece(pawn, pos_pawn)

    def __validate_source_position(self, position: Position) -> None:

        if not self.__board.there_is_a_piece(position):
            raise ChessException('There is no piece on source position.')

        if self.__current_player != cast(ChessPiece, self.__board.piece_by_position(position)).color:
            raise ChessException('The chosen piece is not yours.')

        if not self.__board.piece_by_position(position).is_there_any_possible_move():
            raise ChessException('There is no possible moves for the chosen piece.')

    def __validate_target_position(self, source: Position, target: Position) -> None:
        if not self.__board.piece_by_position(source).possible_move(target):
            raise ChessException('The chosen piece cannot move to target position.')

    def __next_turn(self) -> None:
        self.__turn += 1
        self.__current_player = Color.BLACK if self.__current_player == Color.WHITE else Color.WHITE

    @staticmethod
    def __opponent(color: Color) -> Color:
        return Color.BLACK if color == Color.WHITE else Color.WHITE

    def __king(self, color: Color) -> ChessPiece:

        pieces: List[Piece] = list(filter(lambda x: x.color == color, self.__pieces_on_the_board))

        for piece in pieces:
            if isinstance(piece, King):
                return piece

        raise ValueError(f'There is no {color.name} king on the board.')

    def __test_check(self, color: Color) -> bool:

        king_position: Position = self.__king(color).chess_position().to_position()

        opponent_pieces: List[Piece] = [x for x in self.__pieces_on_the_board
                                        if cast(ChessPiece, x).color == self.__opponent(color)]

        for piece in opponent_pieces:

            mat: List[List[bool]] = piece.possible_moves()

            # king position
            row: int = king_position.row
            column: int = king_position.column

            if mat[row][column]:
                return True

        return False

    def __test_checkmate(self, color: Color) -> bool:

        if not self.__test_check(color):
            return False

        pieces: List[ChessPiece] = [cast(ChessPiece, x) for x in self.__pieces_on_the_board
                                    if cast(ChessPiece, x).color == color]

        for piece in pieces:

            mat: List[List[bool]] = piece.possible_moves()

            rows: int = len(mat)
            columns: int = len(mat[0])

            for i in range(rows):
                for j in range(columns):
                    if mat[i][j]:

                        source: Position = piece.chess_position().to_position()
                        target: Position = Position(i, j)

                        captured_piece: Piece = self.__make_move(source, target)
                        test_check: bool = self.__test_check(color)
                        self.__undo_move(source, target, captured_piece)

                        if not test_check:
                            return False

        return True

    def __place_new_piece(self, column: str, row: int, piece: ChessPiece) -> None:
        self.__board.place_piece(piece, ChessPosition(column, row).to_position())

        self.__pieces_on_the_board.append(piece)

    def __initial_setup(self) -> None:

        # white players
        self.__place_new_piece('a', 1, Rook(self.__board, Color.WHITE))
        self.__place_new_piece('b', 1, Knight(self.__board, Color.WHITE))
        self.__place_new_piece('c', 1, Bishop(self.__board, Color.WHITE))
        self.__place_new_piece('d', 1, Queen(self.__board, Color.WHITE))
        self.__place_new_piece('e', 1, King(self.__board, Color.WHITE, self))
        self.__place_new_piece('f', 1, Bishop(self.__board, Color.WHITE))
        self.__place_new_piece('g', 1, Knight(self.__board, Color.WHITE))
        self.__place_new_piece('h', 1, Rook(self.__board, Color.WHITE))
        self.__place_new_piece('a', 2, Pawn(self.__board, Color.WHITE, self))
        self.__place_new_piece('b', 2, Pawn(self.__board, Color.WHITE, self))
        self.__place_new_piece('c', 2, Pawn(self.__board, Color.WHITE, self))
        self.__place_new_piece('d', 2, Pawn(self.__board, Color.WHITE, self))
        self.__place_new_piece('e', 2, Pawn(self.__board, Color.WHITE, self))
        self.__place_new_piece('f', 2, Pawn(self.__board, Color.WHITE, self))
        self.__place_new_piece('g', 2, Pawn(self.__board, Color.WHITE, self))
        self.__place_new_piece('h', 2, Pawn(self.__board, Color.WHITE, self))

        # black players
        self.__place_new_piece('a', 8, Rook(self.__board, Color.BLACK))
        self.__place_new_piece('b', 8, Knight(self.__board, Color.BLACK))
        self.__place_new_piece('c', 8, Bishop(self.__board, Color.BLACK))
        self.__place_new_piece('d', 8, Queen(self.__board, Color.BLACK))
        self.__place_new_piece('e', 8, King(self.__board, Color.BLACK, self))
        self.__place_new_piece('f', 8, Bishop(self.__board, Color.BLACK))
        self.__place_new_piece('g', 8, Knight(self.__board, Color.BLACK))
        self.__place_new_piece('h', 8, Rook(self.__board, Color.BLACK))
        self.__place_new_piece('a', 7, Pawn(self.__board, Color.BLACK, self))
        self.__place_new_piece('b', 7, Pawn(self.__board, Color.BLACK, self))
        self.__place_new_piece('c', 7, Pawn(self.__board, Color.BLACK, self))
        self.__place_new_piece('d', 7, Pawn(self.__board, Color.BLACK, self))
        self.__place_new_piece('e', 7, Pawn(self.__board, Color.BLACK, self))
        self.__place_new_piece('f', 7, Pawn(self.__board, Color.BLACK, self))
        self.__place_new_piece('g', 7, Pawn(self.__board, Color.BLACK, self))
        self.__place_new_piece('h', 7, Pawn(self.__board, Color.BLACK, self))
