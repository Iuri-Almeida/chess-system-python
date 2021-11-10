from application.color_constants import ColorConstants


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
    BLACK_PIECE_COLOR = ColorConstants.COLOR_YELLOW
    WHITE_PIECE_COLOR = ColorConstants.COLOR_WHITE
    BACKGROUND_COLOR = ColorConstants.BACKGROUND_DARK_BLUE
    INDICATORS_COLOR = ColorConstants.COLOR_GREEN
    GAME_STATUS_COLOR = ColorConstants.COLOR_RED
    RESET_COLOR = ColorConstants.RESET
