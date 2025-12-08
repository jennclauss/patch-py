"""
Configuration constants for Patch.py quilt design app.

Centralizes all magic numbers and configuration to improve maintainability
and testability. Allows configuration to be mocked in tests.
"""

# Each patch is a square with this width and height in pixels
PATCH_SIZE = 100

# Canvas size in pixels
CANVAS_WIDTH = PATCH_SIZE * 4
CANVAS_HEIGHT = PATCH_SIZE * 4

# Quilt block designs included in the program with draw functions
AVAILABLE_QUILT_BLOCKS = ["one patch", "four patch", "half square triangle", "quarter square triangle" ]
# Stores the size of the AVAILABLE_QUILT_BLOCKS list as a variable
QUILT_BLOCKS_LIST_SIZE = len(AVAILABLE_QUILT_BLOCKS)

# Lists provide positioning options 
FOUR_PATCH_POSITIONS = ["upper left, lower right", "upper right, lower left"]
# Stores the size of the FOUR_PATCH_POSITIONS list as a variable
FOUR_PATCH_POSITIONS_LIST_SIZE = len(FOUR_PATCH_POSITIONS)

HALF_SQUARE_TRIANGLE_POSITIONS = ["upper left", "upper right", "lower left", "lower right"]
# Stores the size of the HALF_SQUARE_TRIANGLE_POSITIONS list as a variable
HALF_SQUARE_TRIANGLE_POSITIONS_LIST_SIZE = len(HALF_SQUARE_TRIANGLE_POSITIONS)

QUARTER_SQUARE_TRIANGLE_POSITIONS = ["horizontal", "vertical"]
# Stores the size of the QUARTER_SQUARE_TRIANGLE_POSITIONS list as a variable
QUARTER_SQUARE_TRIANGLE_POSITIONS_LIST_SIZE = len(QUARTER_SQUARE_TRIANGLE_POSITIONS)

# List of colors available in Tkinter library; used to validates user's color inputs
TK_COLOR_NAMES = [
    'snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white',
    'old lace', 'linen', 'antique white', 'papaya whip', 'blanched almond',
    'bisque', 'peach puff', 'navajo white', 'moccasin', 'cornsilk',
    'ivory', 'lemon chiffon', 'seashell', 'honeydew', 'mint cream',
    'azure', 'alice blue', 'lavender', 'lavender blush', 'misty rose',
    'white', 'black', 'dark slate gray', 'dim gray', 'slate gray',
    'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy',
    'cornflower blue', 'dark slate blue', 'slate blue', 'medium slate blue',
    'light slate blue', 'medium blue', 'royal blue', 'blue', 'dodger blue',
    'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
    'light blue', 'powder blue', 'pale turquoise', 'dark turquoise',
    'medium turquoise', 'turquoise', 'cyan', 'light cyan', 'cadet blue',
    'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
    'dark sea green', 'sea green', 'medium sea green', 'light sea green',
    'pale green', 'spring green', 'lawn green', 'green', 'chartreuse',
    'medium spring green', 'green yellow', 'lime green', 'yellow green',
    'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod',
    'light goldenrod yellow', 'light yellow', 'yellow', 'gold', 'light goldenrod',
    'goldenrod', 'dark goldenrod', 'rosy brown', 'indian red', 'saddle brown',
    'sienna', 'peru', 'burlywood', 'beige', 'wheat', 'sandy brown',
    'tan', 'chocolate', 'firebrick', 'brown', 'dark salmon', 'salmon',
    'light salmon', 'orange', 'dark orange', 'coral', 'light coral',
    'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink',
    'light pink', 'pale violet red', 'maroon', 'medium violet red',
    'violet red', 'magenta', 'violet', 'plum', 'orchid', 'medium orchid',
    'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
    'thistle'
]