from graphics import Canvas
from src.patch.config import (
    PATCH_SIZE, CANVAS_WIDTH, CANVAS_HEIGHT,
    AVAILABLE_QUILT_BLOCKS, QUILT_BLOCKS_LIST_SIZE,
    FOUR_PATCH_POSITIONS, FOUR_PATCH_POSITIONS_LIST_SIZE,
    HALF_SQUARE_TRIANGLE_POSITIONS, HALF_SQUARE_TRIANGLE_POSITIONS_LIST_SIZE,
    QUARTER_SQUARE_TRIANGLE_POSITIONS, QUARTER_SQUARE_TRIANGLE_POSITIONS_LIST_SIZE,
    TK_COLOR_NAMES
)

"""
Patch.py is a quilt design app that allows the user to design their own two color, 4x4 block 
quilt using a selection of classic, public domain quilt blocks in a variety of configurations. 
The user interacts with the program and designs their quilt in the terminal and views their 
design on the canvas.
"""

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    welcome_user()
    draw_quilt_background(canvas)
    quilt_patchwork_color = select_patchwork_color()
    design_row(canvas, quilt_patchwork_color)

def welcome_user():
    # welcomes the user to the program
    print("Welcome to Patch.py, a quilt design app!")
    # adds a line break before the next line of text in the terminal
    print("")
    print(f"You can design your own two color, 4x4 block quilt using this app. It contains " + str(QUILT_BLOCKS_LIST_SIZE) + " classic, public domain blocks for you to choose from and use in your design:")
    for i in range (QUILT_BLOCKS_LIST_SIZE):
        print(AVAILABLE_QUILT_BLOCKS[i])
    print("")
    print(f"You will be given position options for some blocks when designing your quilt.")
    print("")

def draw_quilt_background(canvas):
    # gets the user's quilt background color input
    print("First things first:")
    print("")
    while True:
        quilt_background_color = input("What color would you like the background of your quilt to be? ").lower()
        # validates user's color choice is supported by Tkinter GUI library
        if quilt_background_color in TK_COLOR_NAMES:
            break # valid input, exit loop
        else:
            print("")
            print("Invalid color. Please enter another color name.")
            print("")
    # adds a line break before the next line of text in the terminal
    print("")
    # draws one square over the entire canvas to fill the quilt background color
    canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, quilt_background_color)
    return quilt_background_color

def select_patchwork_color():
    # gets the user's quilt patchwork color input to use when drawing all quilt blocks
    while True:
        quilt_patchwork_color = input("What color would you like the patchwork of your quilt to be? ").lower()
        # validates user's color choice is supported by Tkinter GUI library
        if quilt_patchwork_color in TK_COLOR_NAMES:
            break # valid input, exit loop
        else:
            print("")
            print("Invalid color. Please enter another color name.")
            print("")
    # adds a line break before the next line of text in the terminal
    print("")
    return quilt_patchwork_color

def draw_one_patch_square(canvas, start_x, start_y, color):
    # draws a one patch square at (start_x, start_y)
    end_x = start_x + PATCH_SIZE
    end_y = start_y + PATCH_SIZE
    canvas.create_rectangle(start_x, start_y, end_x, end_y, color)

def draw_four_patch_square(canvas, start_x, start_y, color):
    # draws a four patch square at (start_x, start_y)
    end_x = start_x + PATCH_SIZE
    end_y = start_y + PATCH_SIZE
    # draw a square in the upper left corner
    canvas.create_rectangle(start_x, start_y, start_x + (PATCH_SIZE/2), start_y + (PATCH_SIZE/2), color)
    # draw a square in the lower right corner
    canvas.create_rectangle(start_x + (PATCH_SIZE/2), start_y + (PATCH_SIZE/2), end_x, end_y, color)

def draw_four_patch_square_inverted(canvas, start_x, start_y, color):
    # draws a four patch square at (start_x, end_y)
    end_x = start_x + PATCH_SIZE
    end_y = start_y + PATCH_SIZE
    # draw a square in the lower left corner
    canvas.create_rectangle(start_x, end_y, start_x + (PATCH_SIZE/2), start_y + (PATCH_SIZE/2), color)
    # draw a square in the upper right corner
    canvas.create_rectangle(start_x + (PATCH_SIZE/2), start_y + (PATCH_SIZE/2), end_x, start_y, color)

def draw_half_square_triangle_upper_left(canvas, start_x, start_y, color):
    # draws a half square triangle at (start_x, start_y) in the upper left corner of the patch
    end_x = start_x + PATCH_SIZE
    end_y = start_y + PATCH_SIZE
    # draw a half square triangle on top in the upper left corner
    canvas.create_polygon(start_x, start_y, start_x, end_y, end_x, start_y,
    color=color)

def draw_half_square_triangle_upper_right(canvas, start_x, start_y, color):
    # draws a half square triangle at (start_x, start_y) in the upper right corner of the patch
    end_x = start_x + PATCH_SIZE
    end_y = start_y + PATCH_SIZE
    # draw a half square triangle on top in the upper right corner
    canvas.create_polygon(start_x, start_y, end_x, start_y, end_x, end_y,
    color=color)

def draw_half_square_triangle_lower_left(canvas, start_x, start_y, color):
    # draws a half square triangle at (start_x, start_y) in the lower left corner of the patch
    end_x = start_x + PATCH_SIZE
    end_y = start_y + PATCH_SIZE
    # draw a half square triangle on top in the lower left corner
    canvas.create_polygon(start_x, start_y, start_x, end_y, end_x, end_y,
    color=color)

def draw_half_square_triangle_lower_right(canvas, start_x, start_y, color):
    # draws a half square triangle at (start_x, end_y) in the lower right corner of the patch
    end_x = start_x + PATCH_SIZE
    end_y = start_y + PATCH_SIZE
    # draw a half square triangle on top in the lower right corner
    canvas.create_polygon(start_x, end_y, end_x, start_y, end_x, end_y,
    color=color)

def draw_quarter_square_triangle_horizontal(canvas, start_x, start_y, color):
    # draws a horizontal quarter square triangle at (start_x, start_y) in the patch
    end_x = start_x + PATCH_SIZE
    end_y = start_y + PATCH_SIZE
    # draw a quarter square triangle on the left
    canvas.create_polygon(start_x, start_y, start_x + (PATCH_SIZE/2), start_y + (PATCH_SIZE/2), start_x, end_y,
    color=color)
    # draw a quarter square triangle on the right
    canvas.create_polygon(end_x, start_y, start_x + (PATCH_SIZE/2), start_y + (PATCH_SIZE/2), end_x, end_y,
    color=color)

def draw_quarter_square_triangle_vertical(canvas, start_x, start_y, color):
    # draws a vertical quarter square triangle at (start_x, start_y) in the patch
    end_x = start_x + PATCH_SIZE
    end_y = start_y + PATCH_SIZE
    # draw a quarter square triangle on top
    canvas.create_polygon(start_x, start_y, start_x + (PATCH_SIZE/2), start_y + (PATCH_SIZE/2), end_x, start_y,
    color=color)
    # draw a quarter square triangle on bottom
    canvas.create_polygon(start_x, end_y, start_x + (PATCH_SIZE/2), start_y + (PATCH_SIZE/2), end_x, end_y,
    color=color)

"""
draw flying_geese(canvas, start_x, start_y, color):
    # draws flying geese (three vertical triangles) in the patch
    end_x = start_x + PATCH_SIZE
    end_y = start_y + PATCH_SIZE
    # draw the first triangle

    # draw the second triangle

    # draw the third triangle
"""

def design_row(canvas, quilt_patchwork_color):
    # accumulator variable to track which row the user is currently designing and stop the loop when row > 4
    current_row = 0
    # using a custom loop variable in for loops solves variable shadowing bug
    for row in range (4):
        for column in range (4):
            while True:
                user_block_design_choice = input("Which block design would you like to use for row " + str(current_row + 1) + ", column " + str(column + 1) + "? ").lower()
                # validates user's block design choice is in AVAILABLE_QUILT_BLOCKS
                if user_block_design_choice in AVAILABLE_QUILT_BLOCKS:
                    break # valid input, exit loop
                else:
                    print("")
                    print("Invalid block design. Please choose from:")
                    for i in range (QUILT_BLOCKS_LIST_SIZE):
                        print(AVAILABLE_QUILT_BLOCKS[i])
                    print("")
            # adds a line break before the next line of text in the terminal
            print("")
            if user_block_design_choice == "one patch":
                draw_one_patch_square(canvas, PATCH_SIZE * column, current_row * PATCH_SIZE, quilt_patchwork_color)
            if user_block_design_choice == "four patch":
                print(f"There are " + str(FOUR_PATCH_POSITIONS_LIST_SIZE) + " " + (user_block_design_choice) + " positions to choose from:")
                for len in range (FOUR_PATCH_POSITIONS_LIST_SIZE):
                    print(FOUR_PATCH_POSITIONS[len])
                print("")
                while True:
                    user_block_position_choice = input("Which block position would you like to use? ").lower()
                    # validates user's block position choice is in FOUR_PATCH_POSITIONS
                    if user_block_position_choice in FOUR_PATCH_POSITIONS:
                        break # valid input, exit loop
                    else:
                        print("")
                        print("Invalid block position. Please choose from:")
                        for len in range (FOUR_PATCH_POSITIONS_LIST_SIZE):
                            print(FOUR_PATCH_POSITIONS[len])
                        print("")
                # adds a line break before the next line of text in the terminal
                print("")
                if user_block_position_choice == FOUR_PATCH_POSITIONS[0]:
                    draw_four_patch_square(canvas, PATCH_SIZE * column, current_row * PATCH_SIZE, quilt_patchwork_color)
                if user_block_position_choice == FOUR_PATCH_POSITIONS[1]:
                    draw_four_patch_square_inverted(canvas, PATCH_SIZE * column, current_row * PATCH_SIZE, quilt_patchwork_color)
            if user_block_design_choice == "half square triangle":
                print(f"There are " + str(HALF_SQUARE_TRIANGLE_POSITIONS_LIST_SIZE) + " " + (user_block_design_choice) + " positions to choose from:")
                for len in range (HALF_SQUARE_TRIANGLE_POSITIONS_LIST_SIZE):
                    print(HALF_SQUARE_TRIANGLE_POSITIONS[len])
                print("")
                while True:
                    user_block_position_choice = input("Which block position would you like to use? ").lower()
                    # validates user's block position choice is in HALF_SQUARE_TRIANGLE_POSITIONS
                    if user_block_position_choice in HALF_SQUARE_TRIANGLE_POSITIONS:
                        break # valid input, exit loop
                    else:
                        print("")
                        print("Invalid block position. Please choose from:")
                        for len in range (HALF_SQUARE_TRIANGLE_POSITIONS_LIST_SIZE):
                            print(HALF_SQUARE_TRIANGLE_POSITIONS[len])
                        print("")
                # adds a line break before the next line of text in the terminal
                print("")
                if user_block_position_choice == HALF_SQUARE_TRIANGLE_POSITIONS[0]:
                    draw_half_square_triangle_upper_left(canvas, PATCH_SIZE * column, current_row * PATCH_SIZE, quilt_patchwork_color)
                if user_block_position_choice == HALF_SQUARE_TRIANGLE_POSITIONS[1]:
                    draw_half_square_triangle_upper_right(canvas, PATCH_SIZE * column, current_row * PATCH_SIZE, quilt_patchwork_color)
                if user_block_position_choice == HALF_SQUARE_TRIANGLE_POSITIONS[2]:
                    draw_half_square_triangle_lower_left(canvas, PATCH_SIZE * column, current_row * PATCH_SIZE, quilt_patchwork_color)
                if user_block_position_choice == HALF_SQUARE_TRIANGLE_POSITIONS[3]:
                    draw_half_square_triangle_lower_right(canvas, PATCH_SIZE * column, current_row * PATCH_SIZE, quilt_patchwork_color)
            if user_block_design_choice == "quarter square triangle":
                print(f"There are " + str(QUARTER_SQUARE_TRIANGLE_POSITIONS_LIST_SIZE) + " " + (user_block_design_choice) + " positions to choose from:")
                for len in range (QUARTER_SQUARE_TRIANGLE_POSITIONS_LIST_SIZE):
                    print(QUARTER_SQUARE_TRIANGLE_POSITIONS[len])
                print("")
                while True:
                    user_block_position_choice = input("Which block position would you like to use? ").lower()
                    # validates user's block position choice is in QUARTER_SQUARE_TRIANGLE_POSITIONS
                    if user_block_position_choice in QUARTER_SQUARE_TRIANGLE_POSITIONS:
                        break # valid input, exit loop
                    else:
                        print("")
                        print("Invalid block position. Please choose from:")
                        for len in range (QUARTER_SQUARE_TRIANGLE_POSITIONS_LIST_SIZE):
                            print(QUARTER_SQUARE_TRIANGLE_POSITIONS[len])
                        print("")
                # adds a line break before the next line of text in the terminal
                print("")
                if user_block_position_choice == QUARTER_SQUARE_TRIANGLE_POSITIONS[0]:
                    draw_quarter_square_triangle_horizontal(canvas, PATCH_SIZE * column, current_row * PATCH_SIZE, quilt_patchwork_color)
                if user_block_position_choice == QUARTER_SQUARE_TRIANGLE_POSITIONS[1]:
                    draw_quarter_square_triangle_vertical(canvas, PATCH_SIZE * column, current_row * PATCH_SIZE, quilt_patchwork_color)
        # add 1 to accumulator variable for each completion of the outer row loop
        current_row = current_row + 1
    # congratulates user on finishing their quilt design
    print("Congratulations! You just designed a beautiful quilt.")

if __name__ == '__main__':
    main()