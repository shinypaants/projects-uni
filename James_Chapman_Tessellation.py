
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n10260439
#    Student name: James Chapman
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  TESSELLATION
#
#  This assignment tests your skills at processing data stored in
#  lists, creating reusable code and following instructions to display
#  a complex visual image.  The incomplete Python program below is
#  missing a crucial function, "tessellate".  You are required to
#  complete this function so that when the program is run it fills
#  a rectangular space with differently-shaped tiles, using data
#  stored in a list to determine which tiles to place and where.
#  See the instruction sheet accompanying this file for full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  your final solution as a single Python 3 file, whether or not you
#  complete both parts of the assignment.
#
#--------------------------------------------------------------------#



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.  In
# particular, your solution must not rely on any non-standard Python
# modules that need to be downloaded and installed separately,
# because the markers will not have access to such modules.

from turtle import *
from math import *
from random import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

cell_size = 100 # pixels (default is 100)
grid_width = 10 # squares (default is 10)
grid_height = 7 # squares (default is 7)
x_margin = cell_size * 2.75 # pixels, the size of the margin left/right of the grid
y_margin = cell_size // 2 # pixels, the size of the margin below/above the grid
window_height = grid_height * cell_size + y_margin * 2
window_width = grid_width * cell_size + x_margin * 2
small_font = ('Arial', 18, 'normal') # font for the coords
big_font = ('Arial', 24, 'normal') # font for any other text

# Validity checks on grid size - do not change this code
assert cell_size >= 80, 'Cells must be at least 80x80 pixels in size'
assert grid_width >= 8, 'Grid must be at least 8 squares wide'
assert grid_height >= 6, 'Grid must be at least 6 squares high'

#
#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# manage the drawing canvas for your image.  You should not change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image
def create_drawing_canvas(bg_colour = 'light grey',
                          line_colour = 'slate grey',
                          draw_grid = True, mark_legend = False):

    # Set up the drawing canvas with enough space for the grid and
    # legend
    setup(window_width, window_height)
    bgcolor(bg_colour)

    # Draw as quickly as possible
    tracer(False)

    # Get ready to draw the grid
    penup()
    color(line_colour)
    width(2)

    # Determine the left-bottom coords of the grid
    left_edge = -(grid_width * cell_size) // 2
    bottom_edge = -(grid_height * cell_size) // 2

    # Optionally draw the grid
    if draw_grid:

        # Draw the horizontal grid lines
        setheading(0) # face east
        for line_no in range(0, grid_height + 1):
            penup()
            goto(left_edge, bottom_edge + line_no * cell_size)
            pendown()
            forward(grid_width * cell_size)

        # Draw the vertical grid lines
        setheading(90) # face north
        for line_no in range(0, grid_width + 1):
            penup()
            goto(left_edge + line_no * cell_size, bottom_edge)
            pendown()
            forward(grid_height * cell_size)

        # Draw each of the labels on the x axis
        penup()
        y_offset = 27 # pixels
        for x_label in range(0, grid_width):
            goto(left_edge + (x_label * cell_size) + (cell_size // 2), bottom_edge - y_offset)
            write(chr(x_label + ord('A')), align = 'center', font = small_font)

        # Draw each of the labels on the y axis
        penup()
        x_offset, y_offset = 7, 10 # pixels
        for y_label in range(0, grid_height):
            goto(left_edge - x_offset, bottom_edge + (y_label * cell_size) + (cell_size // 2) - y_offset)
            write(str(y_label + 1), align = 'right', font = small_font)

        # Mark centre coordinate (0, 0)
        home()
        dot(15)

    # Optionally mark the spaces for drawing the legend
    if mark_legend:
        # Left side
        goto(-(grid_width * cell_size) // 2 - 75, -25)
        #write('Put your\nlegend here', align = 'right', font = big_font)
        # Right side
        goto((grid_width * cell_size) // 2 + 75, -25)
        #write('Put your\nlegend here', align = 'left', font = big_font)

    # Reset everything ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas to the operating
# system.  By default the cursor (turtle) is hidden when the
# program ends - call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor = True):
    tracer(True) # ensure any drawing still in progress is displayed
    if hide_cursor:
        hideturtle()
    done()

#
#--------------------------------------------------------------------#



#-----Test Data for Use During Code Development----------------------#
#
# The "fixed" data sets in this section are provided to help you
# develop and test your code.  You can use them as the argument to
# the "tesselate" function while perfecting your solution.  However,
# they will NOT be used to assess your program.  Your solution will
# be assessed using the "random_pattern" function appearing below.
# Your program must work correctly for any data set that can be
# generated by the random_pattern function.
#
# Each of the data sets is a list of instructions, each specifying
# where to place a particular tile.  The general form of each
# instruction is
#
#     [squares, mystery_value]
#
# where there may be one, two or four squares in the grid listed
# at the beginning.  This tells us which grid squares must be
# filled by this particular tile.  This information also tells
# us which shape of tile to produce.  A "big" tile will occupy
# four grid squares, a "small" tile will occupy one square, a
# "wide" tile will occupy two squares in the same row, and a
# "tall" tile will occupy two squares in the same column.  The
# purpose of the "mystery value" will be revealed in Part B of
# the assignment.
#
# Note that the fixed patterns below assume the grid has its
# default size of 10x7 squares.
#

# Some starting points - the following fixed patterns place
# just a single tile in the grid, in one of the corners.

# Small tile
fixed_pattern_0 = [['A1', 'O']]
fixed_pattern_1 = [['J7', 'X']]

# Wide tile
fixed_pattern_2 = [['A7', 'B7', 'O']]
fixed_pattern_3 = [['I1', 'J1', 'X']]

# Tall tile
fixed_pattern_4 = [['A1', 'A2', 'O']]
fixed_pattern_5 = [['J6', 'J7', 'X']]

# Big tile
fixed_pattern_6 = [['A6', 'B6', 'A7', 'B7', 'O']]
fixed_pattern_7 = [['I1', 'J1', 'I2', 'J2', 'X']]

# Each of these patterns puts multiple copies of the same
# type of tile in the grid.

# Small tiles
fixed_pattern_8 = [['E1', 'O'],
                   ['J4', 'O'],
                   ['C5', 'O'],
                   ['B1', 'O'],
                   ['I1', 'O']]
fixed_pattern_9 = [['C6', 'X'],
                   ['I4', 'X'],
                   ['D6', 'X'],
                   ['J5', 'X'],
                   ['F6', 'X'],
                   ['F7', 'X']]

# Wide tiles
fixed_pattern_10 = [['A4', 'B4', 'O'],
                    ['C1', 'D1', 'O'],
                    ['C7', 'D7', 'O'],
                    ['A7', 'B7', 'O'],
                    ['D4', 'E4', 'O']]
fixed_pattern_11 = [['D7', 'E7', 'X'],
                    ['G7', 'H7', 'X'],
                    ['H5', 'I5', 'X'],
                    ['B3', 'C3', 'X']]

# Tall tiles
fixed_pattern_12 = [['J2', 'J3', 'O'],
                    ['E5', 'E6', 'O'],
                    ['I1', 'I2', 'O'],
                    ['E1', 'E2', 'O'],
                    ['D3', 'D4', 'O']]
fixed_pattern_13 = [['H4', 'H5', 'X'],
                    ['F1', 'F2', 'X'],
                    ['E2', 'E3', 'X'],
                    ['C4', 'C5', 'X']]

# Big tiles
fixed_pattern_14 = [['E5', 'F5', 'E6', 'F6', 'O'],
                    ['I5', 'J5', 'I6', 'J6', 'O'],
                    ['C2', 'D2', 'C3', 'D3', 'O'],
                    ['H2', 'I2', 'H3', 'I3', 'O'],
                    ['A3', 'B3', 'A4', 'B4', 'O']]
fixed_pattern_15 = [['G2', 'H2', 'G3', 'H3', 'X'],
                    ['E5', 'F5', 'E6', 'F6', 'X'],
                    ['E3', 'F3', 'E4', 'F4', 'X'],
                    ['B3', 'C3', 'B4', 'C4', 'X']]

# Each of these patterns puts one instance of each type
# of tile in the grid.
fixed_pattern_16 = [['I5', 'O'],
                    ['E1', 'F1', 'E2', 'F2', 'O'],
                    ['J5', 'J6', 'O'],
                    ['G7', 'H7', 'O']]
fixed_pattern_17 = [['G7', 'H7', 'X'],
                    ['B7', 'X'],
                    ['A5', 'B5', 'A6', 'B6', 'X'],
                    ['D2', 'D3', 'X']]

# If you want to create your own test data sets put them here,
# otherwise call function random_pattern to obtain data sets
# that fill the entire grid with tiles.

#
#--------------------------------------------------------------------#



#-----Function for Assessing Your Solution---------------------------#
#
# The function in this section will be used to assess your solution.
# Do not change any of the code in this section.
#
# The following function creates a random data set specifying a
# tessellation to draw.  Your program must work for any data set that
# can be returned by this function.  The results returned by calling
# this function will be used as the argument to your "tessellate"
# function during marking.  For convenience during code development
# and marking this function also prints the pattern to be drawn to the
# shell window.  NB: Your solution should not print anything else to
# the shell.  Make sure any debugging calls to the "print" function
# are disabled before you submit your solution.
#
# This function attempts to place tiles using a largest-to-smallest
# greedy algorithm.  However, it randomises the placement of the
# tiles and makes no attempt to avoid trying the same location more
# than once, so it's not very efficient and doesn't maximise the
# number of larger tiles placed.  In the worst case, only one big
# tile will be placed in the grid (but this is very unlikely)!
#
# As well as the coordinates for each tile, an additional value which
# is either an 'O' or 'X' accompanies each one.  The purpose of this
# "mystery" value will be revealed in Part B of the assignment.
#
def random_pattern(print_pattern = True):
    # Keep track of squares already occupied
    been_there = []
    # Initialise the pattern
    pattern = []
    # Percent chance of the mystery value being an X
    mystery_probability = 8

    # Attempt to place as many 2x2 tiles as possible, up to a fixed limit
    attempts = 10
    while attempts > 0:
        # Choose a random bottom-left location
        column = randint(0, grid_width - 2)
        row = randint(0, grid_height - 2)
        # Try to place the tile there, provided the spaces are all free
        if (not [column, row] in been_there) and \
           (not [column, row + 1] in been_there) and \
           (not [column + 1, row] in been_there) and \
           (not [column + 1, row + 1] in been_there):
            been_there = been_there + [[column, row], [column, row + 1],
                                       [column + 1, row], [column + 1, row + 1]]
            # Append the tile's coords to the pattern, plus the mystery value
            pattern.append([chr(column + ord('A')) + str(row + 1),
                            chr(column + ord('A') + 1) + str(row + 1),
                            chr(column + ord('A')) + str(row + 2),
                            chr(column + ord('A') + 1) + str(row + 2),
                            'X' if randint(1, 100) <= mystery_probability else 'O'])
        # Keep track of the number of attempts
        attempts = attempts - 1

    # Attempt to place as many 1x2 tiles as possible, up to a fixed limit
    attempts = 15
    while attempts > 0:
        # Choose a random bottom-left location
        column = randint(0, grid_width - 1)
        row = randint(0, grid_height - 2)
        # Try to place the tile there, provided the spaces are both free
        if (not [column, row] in been_there) and \
           (not [column, row + 1] in been_there):
            been_there = been_there + [[column, row], [column, row + 1]]
            # Append the tile's coords to the pattern, plus the mystery value
            pattern.append([chr(column + ord('A')) + str(row + 1),
                            chr(column + ord('A')) + str(row + 2),
                            'X' if randint(1, 100) <= mystery_probability else 'O'])
        # Keep track of the number of attempts
        attempts = attempts - 1

    # Attempt to place as many 2x1 tiles as possible, up to a fixed limit
    attempts = 20
    while attempts > 0:
        # Choose a random bottom-left location
        column = randint(0, grid_width - 2)
        row = randint(0, grid_height - 1)
        # Try to place the tile there, provided the spaces are both free
        if (not [column, row] in been_there) and \
           (not [column + 1, row] in been_there):
            been_there = been_there + [[column, row], [column + 1, row]]
            # Append the tile's coords to the pattern, plus the mystery value
            pattern.append([chr(column + ord('A')) + str(row + 1),
                            chr(column + ord('A') + 1) + str(row + 1),
                            'X' if randint(1, 100) <= mystery_probability else 'O'])
        # Keep track of the number of attempts
        attempts = attempts - 1

    # Fill all remaining spaces with 1x1 tiles
    for column in range(0, grid_width):
        for row in range(0, grid_height):
            if not [column, row] in been_there:
                been_there.append([column, row])
                # Append the tile's coords to the pattern, plus the mystery value
                pattern.append([chr(column + ord('A')) + str(row + 1),
                                'X' if randint(1, 100) <= mystery_probability else 'O'])

    # Remove any residual structure in the pattern
    shuffle(pattern)
    # Print the pattern to the shell window, nicely laid out
    print('Draw the tiles in this sequence:')
    print(str(pattern).replace('],', '],\n'))
    # Return the tessellation pattern
    return pattern

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "tessellate" function.
#

# Fill the grid with tiles as per the provided dataset

# Function for drawing the entire project.
def tessellate(pattern):
    legend_name()
    legend()

    # Deciding which shapes are being generated.
    for shapes in pattern:
        if len(shapes) == 2:
            x = convert_x[shapes[0][0]]
            y = convert_y[shapes[0][1]]
            forward(x)
            setheading(90)
            forward(y)
            small(shapes[-1])
            home()
        elif len(shapes) == 5:
            x = convert_x[shapes[0][0]]
            y = convert_y[shapes[0][1]]
            forward(x)
            setheading(90)
            forward(y)
            big(shapes[-1])
            home()
        else:
            x = convert_x[shapes[0][0]]
            y = convert_y[shapes[0][1]]
            forward(x)
            setheading(90)
            forward(y)
            if shapes[0][0] == shapes[1][0]:
                tall(shapes[-1])
            else:
                long(shapes[-1])
            home()

# Switch cases for converting coordinates into usable values.
convert_x = {
       "A" : -500,
       "B" : -400,
       "C" : -300,
       "D" : -200,
       "E" : -100,
       "F" : 0,
       "G" : 100,
       "H" : 200,
       "I" : 300,
       "J" : 400,
}

convert_y = {
       "1" : -350,
       "2" : -250,
       "3" : -150,
       "4" : -50,
       "5" : 50,
       "6" : 150,
       "7" : 250,
}

# General function for drawing quadrilaterals.
def quad(height, width, colour):
    fillcolor(colour)
    begin_fill()
    pendown()
    setheading(0)
    forward(width)
    left(90)
    forward(height)
    left(90)
    forward(width)
    left(90)
    forward(height)
    penup()
    end_fill()

# Function for drawing the broken effect for broken tiles (part B).
def broken(start, length, height):
    fillcolor('light grey')
    pencolor('black')
    width(1)
    choose = randint(1,2)

    # Variable 'choose' decides whether the top or bottom of the tile is broken.
    if choose == 1:
        goto(start)
        pendown()
        begin_fill()
        goto(start[0], start[1] + randint(height//4, height-height//4))
    else:
        goto(start[0], start[1] + height)
        pendown()
        begin_fill()
        goto(start[0], start[1] + randint(height//4, height-height//4))

    # Creates a jaggered edge where the tile has broken.
    for jag in range(4):
        count = jag + 1
        goto(start[0] + length/4*count, start[1] + randint(height//4, height-height//4))

    # Finishes the broken tile depending on which half is broken.
    if choose == 1:
        goto(start[0] + length, start[1])
        goto(start)
        end_fill()
        goto(start[0], start[1] + height)
    else:
        goto(start[0] + length, start[1] + height)
        goto(start[0], start[1] + height)
        end_fill()
        goto(start)

# Function for drawing the 1x1 tile.
def small(status):
    quad(100, 100, '#F5F5F5')
    start = pos()
    
    # Mercedes logo
    pencolor('black')
    width(8)

    for layer in range(2):
        penup()
        setheading(0)
        forward(50)
        setheading(90)
        forward(7)
        setheading(0)
        circle(43, -60)
        pendown()

        for segments in range(3):
            circle(43, 120)
            left(90)
            forward(43)
            right(180)
            forward(43)
            left(90)
        
        penup()
        goto(start)
        width(5)
        pencolor('grey')
    penup()

    if status == 'X':
        broken(start, 100, 100)

    penup()
    pencolor('black')
    width(1)

# Function for drawing the 2x2 tile.
def big(status):
    quad(200, 200, '#F5F5F5')
    start = pos()
    
    # BMW logo
    penup()
    setheading(0)
    forward(100)
    setheading(90)
    forward(7)
    setheading(0)
    pendown()
    width(6)
    pencolor('black')
    circle(93)
    width(3)
    pencolor('silver')
    fillcolor('#282828')
    begin_fill()
    circle(93)
    end_fill()
    penup()
    
    setheading(90)
    forward(20)
    setheading(0)
    fillcolor('#3498DB')
    begin_fill()
    pendown()
    circle(73, 90)
    left(90)
    forward(146)
    setheading(270)
    circle(73, -90)
    setheading(270)
    forward(146)
    end_fill()

    setheading(0)
    fillcolor('white')
    begin_fill()
    pendown()
    circle(73, -90)
    setheading(0)
    forward(146)
    setheading(90)
    circle(73, 90)
    setheading(270)
    forward(146)
    end_fill()
    penup()

    if status == 'X':
        broken(start, 200, 200)

    penup()
    pencolor('black')
    width(1)

# Function for drawing the 2x1 tile.
def long(status):
    start = pos()
    quad(100, 200, '#F5F5F5')
    width(8)
    pencolor('black')
    
    # Audi logo
    for logo in range(2):
        setheading(0)
        penup()
        forward(40)
        left(90)
        forward(20)
        setheading(0)

        for circles in range(4):
            pendown()
            circle(30)
            penup()
            forward(40)
        
        width(5)
        pencolor('silver')
        goto(start)

    if status == 'X':
        broken(start, 200, 100)

    penup()
    pencolor('black')
    width(1)

# Function for drawing the 1x2 tile.
def tall(status):
    start = pos()
    quad(200, 100, '#F5F5F5')
    pencolor('black')
    
    # Rolls Royce logo (Depends on the computer as the placements of the R could be off.
    width(3)
    penup()
    setheading(0)
    forward(50)
    setheading(90)
    forward(7)
    pendown()
    setheading(180)
    forward(50-14)
    setheading(0)
    circle(7, -90)
    setheading(90)
    forward(200-28)
    circle(-7, 90)
    forward(100-28)
    circle(-7, 90)
    forward(200-28)
    circle(-7, 90)
    forward(50-14)
    penup()

    goto(start[0] + 7, start[1] + 40)
    setheading(0)
    pendown()
    forward(100-14)
    penup()
    goto(start[0] + 7, start[1] + 160)
    setheading(0)
    pendown()
    forward(100-14)
    penup()

    goto(start[0] + 25, start[1] + 35)
    
    pencolor('black')
    write('R', move=False, align="left", font=("Courier New", 80, "normal"))
    setheading(180)
    forward(15)
    setheading(90)
    forward(6)
    pencolor('white')
    write('R', move=False, align="left", font=("Courier New", 87, "normal"))
    setheading(90)
    forward(3)
    setheading(0)
    forward(4)
    pencolor('black')
    write('R', move=False, align="left", font=("Courier New", 80, "normal"))

    if status == 'X':
        broken(start, 100, 200)

    penup()
    pencolor('black')
    width(1)

# Function for drawing the legend logos.
def legend():
    goto(-690, -125)
    small('O')
    goto(-735, 100)
    big('O')
    goto(540, -150)
    long('O')
    goto(600, 50)
    tall('O')
    home()

# Function for drawing the legends' names.
def legend_name():
    goto(-725, -160)
    write('Mercedes-Benz', align='left', font=small_font)
    goto(-665,70)
    write('BMW', align='left', font=small_font)
    goto(590, 20)
    write('Rolls Royce', align='left', font=small_font)
    goto(615, -180)
    write('Audi', align='left', font=small_font)

# Legends
# for 2 x 2 goto(-735, 100)
# for 1 x 1 goto(-690, -125)
# for 1 x 2 goto(600, 50)
# for 2 x 1 goto(540, -150)

#
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing your solution.  Do not change any of this code except
# as indicated by the comments marked '*****'.
#

# Set up the drawing canvas
# ***** You can change the background and line colours, and choose
# ***** whether or not to draw the grid and mark the places for the
# ***** legend, by providing arguments to this function call
create_drawing_canvas()

# Control the drawing speed
# ***** Change the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** forever while the cursor moves slowly around the screen
tracer(False)

# Give the drawing canvas a title
# ***** Replace this title with a description of your solution's theme
# ***** and its tiles
title("Car Logos by James Chapman")

### Call the student's function to follow the path
### ***** While developing your program you can call the tessellate
### ***** function with one of the "fixed" data sets, but your
### ***** final solution must work with "random_pattern()" as the
### ***** argument.  Your tessellate function must work for any data
### ***** set that can be returned by the random_pattern function.
#tessellate(fixed_pattern_0) # <-- used for code development only, not marking
tessellate(random_pattern()) # <-- used for assessment

# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible at the end of the
# ***** program as a debugging aid
release_drawing_canvas()

#
#--------------------------------------------------------------------#
