from .settings import *

class Button:
    def __init__(self, x, y, width, height, color, text = None, text_color = BLACK):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.text_color = text_color

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(win, WHITE, (self.x, self.y, self.width, self.height), 1)
        '''draws a rectangle that's NOT filled in with border colr as the one mentioned as second argument
            when we pass the last argument : a rectangle is with with a border of the mentioned pixel(s)'''

        if self.text:
            button_font = get_font(17)
            text_surface = button_font.render(self.text, 1, self.text_color)
            '''To draw text in pygame,
            > we create font object[that we did in settings file by creating the function: get_font(size)]
            > than we use that object to render text '''
            win.blit(text_surface, (self.x + self.width/2 - text_surface.get_width() /2, self.y + self.height/2 - text_surface.get_height()/2))


    def clicked(self, pos):
        x, y = pos

        if not (x >= self.x and x <= self.x + self.width):
            return False
        if not (y >= self.y and y <= self.y + self.width):
            return False

        return True





