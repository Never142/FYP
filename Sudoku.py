import sys
import pygame
import random
global GameBoard
global screentrack
class Sudoku:
    def __init__(self,Board,Time,Points,Answerboard):
        self.Board = Board
        self.Time = Time
        self.Points = Points
        self.Answerboard = Answerboard

    def BoardCreate(self):
        blank = []
        for x in range(9):
            blank.append([0,0,0,0,0,0,0,0,0])
        self.Board = blank
        self.Answerboard = blank

    def Save(self):
        file = open("Boardsave.txt","w")
        savetext = ""
        for i in self.Board:
            for j in i:
                savetext = savetext+","+str(j)
        for i in self.Answerboard:
            for j in i:
                savetext = savetext+","+str(j)        
        savetext = savetext+","+str(self.Time)
        savetext = savetext+","+str(self.Points)
        file.write(savetext)        
        file.close()
        return True
    def Load(self):
        print('a')
        global screentrack
        screentrack = 'Game'
        global gencheck
        gencheck = False
        global SelectedNum
        SelectedNum = 0
        try:
            file=open("Boardsave.txt","r")
            templist = file.readline().split(",")
            if len(templist) >0:
                del templist[0]
                NewBoard = []
                for y in range(9):
                    NewBoard.append([])
                    for x in range(9):
                        NewBoard[y].append(int(templist[(y*9)+(x)]))
                self.Board = NewBoard        
                NewBoard = []
                for y in range(9):
                    NewBoard.append([])
                    for x in range(9):
                        NewBoard[y].append(int(templist[81+(y*9)+(x)])) 
                self.Answerboard = NewBoard
                self.Time = int(templist[len(templist)-2])
                self.Points = int(templist[len(templist)-1])
                return True         
            file.close()
            return False
        except FileNotFoundError:
            return False

def LeaderBoardSave(LeaderBoardList):
    file = open("LeaderBoardsave.txt","w")
    savetext = ""
    for i in LeaderBoardList:#saving points and time
        for j in i:
            savetext=savetext+","+str(j)
    file.write(savetext)        
    file.close()
def LeaderBoardLoad():
    LeaderboardList = []
    try:
        file = open("LeaderBoardsave.txt","r")
        templist = file.readline().split(",")
        if len(templist)>0:
            del templist[0]
            count = 0

            LeaderboardItem = []
            for i in templist:
                LeaderboardItem.append(int(i))
                count+=1
                if count == 2:
                    count = 0
                    LeaderboardList.append(LeaderboardItem)
                    print(LeaderboardList)
                    LeaderboardItem = []
        file.close()
        print(LeaderboardList)
        return LeaderboardList
    except FileNotFoundError:
        LeaderBoardSave(LeaderboardList)
        return LeaderboardList
def SolverBrute(InputList):

    for y in range(9):
        for x in range(9):
            if InputList[y][x] !=0:
                x+=1
                if x == 9:
                    y+=1
                    x = 0
                if y ==9:
                    return True    
            if InputList[y][x] == 0:
                for i in range(InputList[y][x],9):
                    InputList[y][x] = i+1
                    if BoardValidity(InputList):
                        #for Row in InputList:
                        #    print(Row)
                        #print("-")    
                        if SolverBrute(InputList):
                            return True
                
                InputList[y][x] = 0
                return False

    return False        

                      

def BoardValidity(InputBoard):
    rows = []
    columns = []
    boxes = []
    #[x]  [0-2,  3-5,  6-8] y
    #[0-2][box1, box2, box3]
    #[3-5][box4, box5, box6]
    #[6-8][box7, box8, box9]
    constraints = [rows,columns,boxes]
    for i in constraints:
        for j in range(9):
            i.append([1,2,3,4,5,6,7,8,9])
    for y in range(9):#checking for duplicates
        for x in range(9):
            if InputBoard[y][x] != 0: #check full row i and an item j in each column
                if InputBoard[y][x] in columns[y]:
                    columns[y][InputBoard[y][x]-1] = 0
                else:
                    return False    
                if InputBoard[y][x] in rows[x]:
                    rows[x][InputBoard[y][x]-1] = 0    
                else:
                    return False
                if 0<=x<=2:
                    boundX = {1,4,7}
                elif 3<=x<=5:
                    boundX = {2,5,8}
                elif 6<=x<=8:  
                    boundX = {3,6,9}
                if 0<=y<=2:
                    boundY = {1,2,3}
                elif 3<=y<=5:
                    boundY = {4,5,6}
                elif 6<=y<=8:  
                    boundY = {7,8,9}
                BoxIndex = list(boundX.intersection(boundY))[0]-1
                if InputBoard[y][x] in boxes[BoxIndex]:
                    boxes[BoxIndex][InputBoard[y][x]-1] = 0    
                else:
                    return False
    return True                   
def SudokuGen(num):
    startrow = [1,2,3,4,5,6,7,8,9]
    random.shuffle(startrow)
    Board = []
    Board.append(startrow)
    Board.append(startrow[3:9]+startrow[0:3])
    Board.append(startrow[6:9]+startrow[0:6])
    Board.append(startrow[1:9])
    Board[3].append(startrow[0])
    Board.append(startrow[4:9]+startrow[0:4])
    Board.append(startrow[7:9]+startrow[0:7])
    Board.append(startrow[2:9]+startrow[0:2])
    Board.append(startrow[5:9]+startrow[0:5])
    Board.append(startrow[0:8])
    Board[8].insert(0,startrow[8])
    numcount = 0
    
    while numcount < (81- num):
        x = random.randint(0,8)
        y = random.randint(0,8)
        if Board[y][x]!= 0:
            Board[y][x] =0
            numcount+=1
    if BoardValidity(Board):
        return Board                   


pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))

font = pygame.font.SysFont('Arial', 40)
LeaderBoardlist = []
objects = []
class Button():
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.buttonText = buttonText
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
def NumSelect(num):
        global SelectedNum
        SelectedNum = int(num)  
def SudokuBoardChange(x,y,num):
    print(x,y)
    if GameBoard.Board[y][x] == 0 and SelectedNum != 0:
        GameBoard.Answerboard[y][x] = num
        if BoardValidity(GameBoard.Answerboard):
            print("Correct Choice")
            GameBoard.Points += 10
        else:
            GameBoard.Points -= 10   
            print("Incorrect Choice")
    elif GameBoard.Board[y][x] != 0:#cant delete original puzzle
        GameBoard.Answerboard[y][x] = 0
    else:
        GameBoard.Answerboard[y][x] = 0  
def Validate(InputBoard):
    global ValidateCheck
    ValidateCheck = True
    global IsFeasible
    count = 0
    for i in InputBoard:
        for j in i:
            if j != 0:
                count+=1
    if count<17:
        print("Too Few Clues")
        IsFeasible = False
        return False        
    if not BoardValidity(InputBoard):
        print("Given Board does not obey sudoku rules")
        IsFeasible = False
        return False
    SolverBrute(InputBoard)
    for i in InputBoard:
        if 0 in i:
            print("Not Solvable")
        IsFeasible = False
        return False
    IsFeasible = True
    return True    

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
def ScreenGameEasy():
    global screentrack 
    screentrack = 'Game'
    global gencheck
    gencheck = True
    global clues
    clues = 45
def ScreenGameMedium():
    global screentrack 
    screentrack = 'Game'
    global gencheck
    gencheck = True
    global clues
    clues = 35
def ScreenGameHard():
    global screentrack 
    screentrack = 'Game'
    global gencheck
    gencheck = True
    global clues
    clues = 25         
def ScreenValidator():
    global screentrack 
    screentrack = 'Validator'
    global gencheck
    gencheck = True
    global ValidateCheck
    ValidateCheck = False   
def Quit():
    pygame.quit()
    sys.exit()
               
screentrack = 'main'
while True:
    if screentrack == 'main':
        objects = []
        objects.append(Button(440, 30, 400, 100, 'Game', ScreenDifficulty,True))
        objects.append(Button(440, 140, 400, 100, 'Validator', ScreenValidator,True))
        objects.append(Button(440, 250, 400, 100, 'Leaderboard', ScreenLeaderboard,True))
        objects.append(Button(440, 360, 400, 100, 'End', Quit,True))
    elif screentrack == 'Difficulty':
        objects = []
        objects.append(Button(440, 30, 400, 100, 'Back', ScreenMain,True))
        objects.append(Button(440, 140, 400, 100, 'Easy', ScreenGameEasy,True))
        objects.append(Button(440, 250, 400, 100, 'Medium', ScreenGameMedium,True))
        objects.append(Button(440, 360, 400, 100, 'Hard', ScreenGameHard,True))
        GameBoard = Sudoku([],0,0,[])
        objects.append(Button(440, 470, 400, 100, 'Load', GameBoard.Load,True))
    elif screentrack == 'Leaderboard':
        objects = []
        objects.append(Button(440, 30, 400, 100, 'Main Menu', ScreenMain,True))
        LeaderBoardlist = []
        LeaderBoardlist = LeaderBoardLoad()
        count = 0
        while count <5 and count < len(LeaderBoardlist):
            objects.append(Button(140, 30+(count*100), 1000, 100, str(count+1)+". Points:"+str(LeaderBoardlist[count][0])+" Time:"+str(LeaderBoardlist[count][1]), myFunction,True))
            count+=1
    elif screentrack == 'Game':
        if gencheck:
            GameBoard = Sudoku([],0,0,[])
            GameBoard.BoardCreate()
            GameBoard.Board = SudokuGen(clues)
            gencheck = False
            SelectedNum = 0
            for y in range(9):
                for x in range(9):
                    GameBoard.Answerboard[y][x] = GameBoard.Board[y][x]
            startingtime = pygame.time.get_ticks()
        else:
            startingtime = 1000                    
        GameBoard.Time = int((pygame.time.get_ticks()-startingtime)/100)
        objects = []
        for y in range(9):
            for x in range(9):
                numlist = [0,1,2,3,4,5,6,7,8]
                text = ''
                if GameBoard.Answerboard[y][x] != 0:
                    text = str(GameBoard.Answerboard[y][x])
                objects.append(Button(180+(60*x), 30+(60*y), 50, 50, text, lambda x=x,y=y: SudokuBoardChange(x,y,SelectedNum),True))
        objects.append(Button(1200, (60*0), 50, 50, str('X'), lambda: NumSelect(0),True))
        objects.append(Button(1200, (60*1), 50, 50, str(1), lambda: NumSelect(1),True))
        objects.append(Button(1200, (60*2), 50, 50, str(2), lambda: NumSelect(2),True))
        objects.append(Button(1200, (60*3), 50, 50, str(3), lambda: NumSelect(3),True))
        objects.append(Button(1200, (60*4), 50, 50, str(4), lambda: NumSelect(4),True))
        objects.append(Button(1200, (60*5), 50, 50, str(5), lambda: NumSelect(5),True))
        objects.append(Button(1200, (60*6), 50, 50, str(6), lambda: NumSelect(6),True))
        objects.append(Button(1200, (60*7), 50, 50, str(7), lambda: NumSelect(7),True))
        objects.append(Button(1200, (60*8), 50, 50, str(8), lambda: NumSelect(8),True))
        objects.append(Button(1200, (60*9), 50, 50, str(9), lambda: NumSelect(9),True))
        text = str(SelectedNum)
        if text == '0':
            text = 'X'
        objects.append(Button(1090, 30, 100, 100, text, myFunction))
        objects.append(Button(1090, 135, 100, 50, str(GameBoard.Points), myFunction))   
        objects.append(Button(1000, 240, 190, 50, str(GameBoard.Time), myFunction))
        objects.append(Button(1000, 135, 100, 50, "Points:", myFunction))   
        objects.append(Button(900, 240, 100, 50, "Time:", myFunction))
        objects.append(Button(990, 600, 200, 100, 'Main Menu', ScreenMain,True))
        objects.append(Button(880, 600, 100, 100, 'Save', GameBoard.Save,True))
        count = 0
        for i in GameBoard.Answerboard:
            if 0 not in i:
                count += 1
        if count ==9:
            screentrack = "Victory"
            LeaderBoardlist.append([GameBoard.Points,GameBoard.Time])
            LeaderBoardlist.sort()
            LeaderBoardSave(LeaderBoardlist)
    elif screentrack  == "Victory":
        objects = []        
        objects.append(Button(440, 30, 400, 100, 'Main Menu', ScreenMain))
        objects.append(Button(440, 140, 400, 100, 'You solved this Puzzle!', myFunction))
        objects.append(Button(440, 250, 400, 100, 'Accruing '+str(GameBoard.Points)+' Points!', myFunction))
        objects.append(Button(440, 360, 400, 100, 'In '+str(GameBoard.Time)+' Seconds!', myFunction))            
    elif screentrack == 'Validator':      
        objects = []
        if gencheck:
            GameBoard = Sudoku([],0,0,[])
            GameBoard.BoardCreate()
            gencheck = False
            SelectedNum = 0
        for y in range(9):
            for x in range(9):
                text = ''
                if GameBoard.Answerboard[y][x] != 0:
                    text = str(GameBoard.Answerboard[y][x])
                objects.append(Button(180+(60*x), 30+(60*y), 50, 50, text, lambda x=x,y=y: SudokuBoardChange(x,y,SelectedNum),True))
        objects.append(Button(1200, (60*0), 50, 50, str('X'), lambda: NumSelect(0),True))
        objects.append(Button(1200, (60*1), 50, 50, str(1), lambda: NumSelect(1),True))
        objects.append(Button(1200, (60*2), 50, 50, str(2), lambda: NumSelect(2),True))
        objects.append(Button(1200, (60*3), 50, 50, str(3), lambda: NumSelect(3),True))
        objects.append(Button(1200, (60*4), 50, 50, str(4), lambda: NumSelect(4),True))
        objects.append(Button(1200, (60*5), 50, 50, str(5), lambda: NumSelect(5),True))
        objects.append(Button(1200, (60*6), 50, 50, str(6), lambda: NumSelect(6),True))
        objects.append(Button(1200, (60*7), 50, 50, str(7), lambda: NumSelect(7),True))
        objects.append(Button(1200, (60*8), 50, 50, str(8), lambda: NumSelect(8),True))
        objects.append(Button(1200, (60*9), 50, 50, str(9), lambda: NumSelect(9),True))
        text = str(SelectedNum)
        if text == '0':
            text = 'X'
        objects.append(Button(1090, 30, 100, 100, text, myFunction))
        objects.append(Button(990, 600, 200, 100, 'Main Menu', ScreenMain,True))
        objects.append(Button(780, 600, 200, 100, 'Validate', lambda: Validate(GameBoard.Answerboard),True))
        if ValidateCheck:
            if IsFeasible:
                text = 'Solvable'
            else:
                text = 'Not Solvable'
        objects.append(Button(780, 490, 200, 100, text, myFunction,True))
        


    screen.fill((20, 20, 20))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    for object in objects:
        object.process()
    pygame.display.flip()
    fpsClock.tick(fps)  
                
