"""
Configuration constants for Patch.py quilt design application.

Centralizes all magic numbers and configuration to improve maintainability
and testability. Allows configuration to be mocked in tests.
"""

# Canvas dimensions
PATCH_SIZE = 100
CANVAS_WIDTH = PATCH_SIZE * 4
CANVAS_HEIGHT = PATCH_SIZE * 4

# Available quilt block designs
AVAILABLE_QUILT_BLOCKS = [
    "one patch",
    "four patch",
    "half square triangle",
    "quarter square triangle"
]

# Position options per block type
BLOCK_POSITIONS = {
    "four patch": ["upper left, lower right", "upper right, lower left"],
    "half square triangle": ["upper left", "upper right", "lower left", "lower right"],
    "quarter square triangle": ["horizontal", "vertical"]
}

# Tkinter color names (140+ supported colors)
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
