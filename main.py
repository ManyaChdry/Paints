from utils import *
from utils import button

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paints")

#This function would initialize our grid
def init_grid(rows, cols, color):
    grid = [] #is a list

    #making a 2D list
    for i in range(rows):
        grid.append([]) #when we move on to next row we add a row
        for _ in range(cols):  #since we don't need the other variable to be used anywhere else, we use _ instead of a new variable
            grid[i].append(color) 
    '''what the above loop is doing is adding all of our rows
    once that is done, we adding all our colors into that row into our column'''

    return grid



def draw_grid(win, grid):
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pygame.draw.rect(win, pixel, (j* PIXEL_SIZE, i* PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE)) #draws pixels
            #     (where to draw, color, (x,y,width, height)=position)
            # since color is what the pixel is we tell to take the pixel!
            '''loop through all the pixels I have, since its a 2D list i would have to loop 
                through all the rows and columns, than draw all the pixels

                *enumerate* is cobination of two styles of for loop
                we use it when we want the index at which we are as well as the row
                to get both, we use enumerate
            ''' 

    if DRAW_GRID_LINES:
        for i in range(ROWS + 1):
            pygame.draw.line(win, GREY,(0, i* PIXEL_SIZE), (WIDTH, i* PIXEL_SIZE)) #we used *i* since y needs to be same 
            '''                                |                    |
                                [starting position of line] [ending position of line]
            '''
        for i in range(COLS + 1):
            pygame.draw.line(win, GREY,(i* PIXEL_SIZE, 0), (i* PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))



def draw(win, grid, buttons):
    win.fill(BG_COLOR)
    draw_grid(win, grid)

    for button in buttons:
        button.draw(win)

    pygame.display.update()


def get_row_col_from_pos(pos): 
    x, y = pos #this would decompose our tupple in x and y position
    row = y // PIXEL_SIZE
    col = x // PIXEL_SIZE

    if row >= ROWS:
        raise IndexError
    #that's how we raise an exception in python

    return row, col

run = True
clock = pygame.time.Clock()

grid = init_grid(ROWS, COLS, BG_COLOR) 
#here we are passing the bg color becuz we want all pixels to be initialized to our bg color

paint = BLACK

button_y = HEIGHT - TOOLBAR_HEIGHT +1
button_yy = HEIGHT - 51
buttons = [ 
    Button(1, button_y, 50, 50, BLACK),
    Button(51, button_y, 50, 50, PURPLE),
    Button(101, button_y, 50, 50, BLUE),
    Button(151, button_y, 50, 50, AQUA),
    Button(201, button_y, 50, 50, GREEN),
    Button(251, button_y, 50, 50, GREEEN),
    Button(301, button_y, 50, 50, YELLOW),
    Button(351, button_y, 50, 50, ORANGE),
    Button(401, button_y, 50, 50, RED),
    Button(451, button_y, 50, 50, MAROON),
    Button(501, button_y, 50, 50, WHITE, "Erase", BLACK),
    Button(551, button_y, 50, 50, GREY, "Clear", BLACK),
    Button(1, button_yy, 50, 50, WHITE),
    Button(51, button_yy, 50, 50, L_P),
    Button(101, button_yy, 50, 50, L_BLUE),
    Button(151, button_yy, 50, 50, L_AQUA),
    Button(201, button_yy, 50, 50, L_GREEEN),
    Button(251, button_yy, 50, 50, L_GREEN),
    Button(301, button_yy, 50, 50, L_Y),
    Button(351, button_yy, 50, 50, SKIN),
    Button(401, button_yy, 50, 50, BABY_RED),
    Button(451, button_yy, 50, 50, BROWN),
    Button(501, button_yy, 50, 50, D_BROWN),
    Button(551, button_yy, 50, 50, D_GREY)
    ] #is a list

while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        #we check if the user has pressed their mouse using the following command
        if pygame.mouse.get_pressed()[0]: #if there was 1 or 2, 1 = index/middle and 2 = right button
            #the no. zero tells if they pressed the left mouse button
            pos = pygame.mouse.get_pos() #this gives us the x,y position of which pixel the user clicked
            
            try:
                row, col = get_row_col_from_pos(pos) 
                grid[row][col] = paint #here what we did is if we get a valid row-col, we change the color
            except IndexError:
                for button in buttons:
                    if not button.clicked(pos):
                        continue
                    
                    paint = button.color

                    if button.text == "Clear":
                        grid = init_grid(ROWS, COLS, BG_COLOR)
                        paint = BLACK

    draw(WINDOW, grid, buttons)

pygame.quit()

