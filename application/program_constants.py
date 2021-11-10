from application.ansi_color_constants import ANSIColorConstants


class ProgramConstants(object):

    # Board
    ROWS = 8
    COLUMNS = 8
    FIRST_COLUMN = 'a'
    LAST_COLUMN = 'h'

    # Game Status
    CHECK = 'CHECK'
    CHECKMATE = 'CHECKMATE'
    NO_CHECK = 'NO CHECK'

    # Game Colors
    BLACK_PIECE_COLOR = ANSIColorConstants.ANSI_YELLOW
    WHITE_PIECE_COLOR = ANSIColorConstants.ANSI_WHITE
    BACKGROUND_COLOR = ANSIColorConstants.ANSI_BLUE_BACKGROUND
    INDICATORS_COLOR = ANSIColorConstants.ANSI_GREEN
    GAME_STATUS_COLOR = ANSIColorConstants.ANSI_RED
    RESET_COLOR = ANSIColorConstants.ANSI_RESET
