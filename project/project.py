'''
 This program uses Python Lists to create a path-finding app using colours and calculates the respective cost of a given path
'''
# We use the turtle module to display the path of the turtle
import turtle

# This function changes the text file that contains the colours and returns a dictionary that 
# stores the colour as the key and the colour's respective cost depending on the line number as the value
def change_to_colour_and_costs(filename):
    contents = {}
    cost = 0 # This variable keeps track of the line number that is associated with the colour
    file = open(filename,'r')
    for colour in file:
        colour = colour.strip() # Removes the end of line character and any potential leading spaces
        if colour.isalpha(): # This condition avoids adding empty lines as keys
            contents[colour.lower()] = cost # Lower method call here to ensure case sensitivity is not an issue
            cost += 1
    file.close()
    return contents

# This function changes the text file that contains the matrix and
# returns a nested list which contains each row of colours as a nested list 
def change_matrix_to_nested(filename):
    contents = []
    file = open(filename,'r')
    for row in file:
        row = row.strip() # Removes the end of line character and any potential leading spaces
        row = row.split(" ") # This line splits the colours separated by the space
        contents.append(row)
    file.close()
    return contents

# This function returns a list that contains the directions of the path that the turtle will follow
def obtain_path(filename):
    directions = []
    file = open(filename,'r')
    for direction in file:
        direction = direction.strip()
        if direction.isalpha(): # Check if the characters are of the alphabet because we do not want to append the digits
            directions.append(direction.lower()) # Lower method call here to ensure case sensitivity is not an issue
    file.close()
    return directions

# This function obtains the row index and column index of the file and returns the row and column index as a tuple 
# which will be the turtle's starting position on the grid
def obtain_coords(filename):
    file = open(filename,'r')
    row = file.readline().strip() # This line reads the row index of the file
    col = file.readline().strip() # This line reads the column index of the file
    file.close()
    return (int(row),int(col)) # Since the row and column were initially strings, we want to change them to integer data types for later use
    
# This function uses the turtle module to draw a square which reflects one grid square
def draw_square(turt,size):
    for i in range(4):
        turt.forward(size)
        turt.right(90)

# This function draws the grid using the turtle module
def draw_grid(num_rows,num_cols,turt,size):
    for r in range(num_rows):
        for c in range(num_cols):
            draw_square(turt,size)
            turt.forward(size)
        # The lines below move the turtle to the next row to draw the next grid row
        turt.backward(num_cols*size)
        turt.right(90)
        turt.forward(size)
        turt.left(90)

# This function takes the matrix list and returns a nested listed which contains 
# a tuple including the colour and its associated x and y location on the grid
def colour_and_coords(size,matrix,start_x,start_y,num_row,num_col):
    row_list = list(range(num_row))
    col_list = list(range(num_col))
    colour_and_xy = [] # This is the main nested list for this function which stores the colour and their associated x and y location on the grid
    count1 = 0 # Keeps track of which row is being calculated
    for row in matrix:
        count2 = 0 # This variable resets after each column in the row has been recorded
        row_colours = []
        square_y = (start_y - (size/2)) - (size * row_list[count1]) # This line calculates the y position of the middle of the row
        for col in row:
            square_x = (start_x + (size/2)) + (size * col_list[count2]) # This line calculates the x position of the middle of the column
            row_colours.append((col,square_x,square_y)) # This line appends the (colour,x,y) location as a tuple
            count2 += 1 # Incremented to keep track of which column is being calculated
        count1 += 1 # Incremented to keep track of which row is being calculated
        colour_and_xy.append(row_colours) # Once a row has been completed, this line appends the row to the main list which stores the nested list
    return colour_and_xy

# This function takes the directions list and moves in the direction of each item in the list and 
# returns the colours the turtle crossed over in the grid
def move_turt(turt,size,directions,colour_and_coord):
    colour_path = []
    dot_size = int(size // 2) # Sets the size of the dot on the grid depending on the size of the grid squares, only accepts integers
    for d in directions:
        current_pos = turt.pos() # This line obtain the turtle's current position on the grid

        # This line matches the turtle's current position with the positions on the grid and 
        # returns the colour the turtle is currently on
        turt_colour = validate_colour_and_coords(current_pos,colour_and_coord)
        colour_path.append(turt_colour)
        turt.dot(dot_size,turt_colour) # This line draws the circle with the corresponding colour in the grid square

        # These conditions move the turtle along the grid
        if d == "up":
            turt.left(90)
            turt.forward(size)
            turt.right(90)
        elif d == "down":
            turt.right(90)
            turt.forward(size)
            turt.left(90)
        elif d == "left":
            turt.left(180)
            turt.forward(size)
            turt.right(180)
        elif d == "right":
            turt.forward(size)
    
    # To obtain the ending colour that the turtle is standing on last
    current_pos = turt.pos() 
    turt_colour = validate_colour_and_coords(current_pos,colour_and_coord)
    colour_path.append(turt_colour)
    turt.dot(dot_size,turt_colour) 
    return colour_path

# This function checks to see if the coordinates of the turtle on the grid matches with a colour from our matrix.
# The tolerance parameter here is used because it specifies the maximum distance between the turtle position 
# and the specified coordinates that is still considered a match which would otherwise return "None" without the tolerance parameter
def validate_colour_and_coords(path_coords,colour_and_coord,tolerance=0.01):
    for item_row in colour_and_coord:
        for item_column in item_row:            
            if (abs(path_coords[0] - item_column[1]) <= tolerance) and (abs(path_coords[1] - item_column[2]) <= tolerance):
                return item_column[0] # This line returns the colour associated with the passed in coordinates

# This function prints out the cost of the turtle's path by taking in the turtle's path and 
# the dictionary that contains the cost of colours
def print_colour_and_cost(colours_path,colour_and_cost):
    count = 0 # Keeps track of the number of iterations so that there is not an additional "+" sign at the end
    for colour in colours_path:
        if count == len(colours_path) - 1: # Condition is used so that there is not an additional "+" sign at the end
            print("cost(" + colour + ") =",end=" ")
            break
        print("cost(" + colour + ") +",end=" ")
        count += 1
    
    count = 0 # Reset the count
    total_cost = 0 # Accumulator variable
    for colour in colours_path:
        total_cost += colour_and_cost[colour] # This line accesses the dictionary with the key as the colour to find the associated value as the cost
        if count == len(colours_path) - 1: # Condition is used so that there is not an additional "+" sign at the end
            print(colour_and_cost[colour], "=", total_cost)
            return
        print(colour_and_cost[colour], "+",end=" ")
        count += 1

# This function runs our program
def main():
    try:
        colour_file = "colorList.txt"
        colour_list = change_to_colour_and_costs(colour_file)

        matrix_file = "matrix.txt"
        matrix_list = change_matrix_to_nested(matrix_file)

        directions_file = "directions.txt"
        directions_list = obtain_path(directions_file)
        row, column = obtain_coords(directions_file)

    except FileNotFoundError: # This exception applies if the files defined above are not found in the same directory as this program
        print('''Please ensure that the "colorList.txt", "matrix.txt", and "directions.txt" files exists within this file's directory.''')
        return
    except: # Applies to any outstanding errors
        print("Error!")
        return
    
    # These variables count the number of rows and columns the grid will have so that they can be passed in the draw_grid function
    grid_rows = len(matrix_list)
    grid_cols = len(matrix_list[0])

    # These variables are the starting positions to draw our grid
    grid_start_x = -240
    grid_start_y = 260
    
    size = 60 # Adjusts the size of the squares in our grid
    t = turtle.Turtle()
    turtle.title("Welcome to the Path-Finding App!") # Sets the title of the turtle screen
    t.shape("turtle")
    t.shapesize(stretch_wid=1.25, stretch_len=1.25, outline=None) # Changes the size of the turtle's shape
    t.color("#438D80") # Sets the colour of the turtle shape
    t.pencolor("#F5F5F5") # Sets the colour of the grid lines
    turtle.bgcolor("#616D7E") # Sets the colour of the background
    turtle.screensize(canvwidth=600, canvheight=600) # Sets the size of the turtle screen when the program is run
    t.width(2) # Adjusts the grid lines size
    t.speed(0) # Speed of the turtle
    
    t.penup()
    t.goto(grid_start_x,grid_start_y) # Starting location of where the turtle begins to draw our grid
    t.pendown()
    draw_grid(grid_rows,grid_cols,t,size)
    t.penup()

    # This line returns a nested list which contains the colour and its associated x and y position on the grid for all the colours in the matrix 
    colour_with_coords = colour_and_coords(size,matrix_list,grid_start_x,grid_start_y,grid_rows,grid_cols)
        
    # These lines specify which grid square the turtle will start in
    grid_square_start_row = (grid_start_x + (size/2)) + (size * column)
    grid_square_start_col = (grid_start_y - (size/2)) - (size * row)
    t.goto(grid_square_start_row,grid_square_start_col)
    t.hideturtle() # Hides the turtle from screen

    try:
        # This line moves the turtle and draws the colours in the grid and also stores the colours the turtle traversed in a list
        colours_crossed = move_turt(t,size,directions_list,colour_with_coords)
    # This exception can apply if the starting position is out of range or if the directions go outside of the grid 
    # or if there exists colours in the matrix which do not exist in the colorList.txt file
    except: 
        print("Out of bounds!")
        return
    
    print_colour_and_cost(colours_crossed,colour_list) # Prints the colours based on the turtle's path and the cost of the path
    return
    
main()
