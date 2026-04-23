
import sys
import pygame

pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))

font = pygame.font.SysFont('Arial', 40)

objects = []
class Button():
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }
        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))
    def process(self):
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                if self.onePress:
                    self.onclickFunction()
                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False
        self.buttonSurface.blit(self.buttonSurf, [
        self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
        self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2])
        screen.blit(self.buttonSurface, self.buttonRect)        
def myFunction():
    print('Button Pressed')
def ScreenDifficulty():
    global screentrack 
    screentrack = 'Difficulty'   
def ScreenMain():
    global screentrack 
    screentrack = 'main' 
def ScreenLeaderboard():
    global screentrack 
    screentrack = 'Leaderboard' 
def ScreenGame():
    global screentrack 
    screentrack = 'Game' 
def ScreenValidator():
    global screentrack 
    screentrack = 'Validator'   
def Quit():
    pygame.quit()
    sys.exit()           
screentrack = 'main'
while True:
    if screentrack == 'main':
        objects = []
        objects.append(Button(440, 30, 400, 100, 'Game', ScreenDifficulty))
        objects.append(Button(440, 140, 400, 100, 'Validator', ScreenValidator))
        objects.append(Button(440, 250, 400, 100, 'Leaderboard', ScreenLeaderboard))
        objects.append(Button(440, 360, 400, 100, 'End', Quit))
    elif screentrack == 'Difficulty':
        objects = []
        objects.append(Button(440, 30, 400, 100, 'Back', ScreenMain))
        objects.append(Button(440, 140, 400, 100, 'Easy', ScreenGame))
        objects.append(Button(440, 250, 400, 100, 'Medium', ScreenGame))
        objects.append(Button(440, 360, 400, 100, 'Hard', ScreenGame))
    elif screentrack == 'Leaderboard':
        objects = []
        objects.append(Button(440, 30, 400, 100, 'Back', ScreenMain))
    elif screentrack == 'Game':
        objects = []
        objects.append(Button(440, 30, 400, 100, 'Back', ScreenMain))
    elif screentrack == 'Validator':
        objects = []        
        objects.append(Button(440, 30, 400, 100, 'Back', ScreenMain))    

    screen.fill((20, 20, 20))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    for object in objects:
        object.process()
    pygame.display.flip()
    fpsClock.tick(fps)