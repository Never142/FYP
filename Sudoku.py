

class Sudoku:
    def __init__(self, Name,Board,Date,Time,Points,Answerboard):
        self.Name = Name
        self.Board = Board
        self.Date = Date
        self.Time = Time
        self.Points = Points
        self.Answerboard = Answerboard

    def BoardCreate(self):
        blank = []
        for x in range(9):
            row = []
            for y in range(9):
                row.append([0,0,0,0,0,0,0,0,0])
            blank.append(row)
        self.Board = blank
        self.Answerboard = blank

    def BoardValidity(self):
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
        for x in range(9):#checking for duplicates
            for y in range(9):
                if self.board[x][y] != 0: #check full row i and an item j in each column
                    if self.board[x][y] in columns[y]:
                        columns[y][self.board[x][y]-1] = 0
                    elif self.board[x][y] in rows[x]
                        rows[x][self.board[x][y]-1] = 0    
                    else:
                       return False
                    if 0 <= x <=2:
                        if 0 <= y <=2:#box1
                            if self.board[x][y] in boxes[0]:
                                boxes[0][self.board[x][y]-1] = 0
                            else:
                                return False
                        elif 3 <= y <=5:#box2
                            if self.board[x][y] in boxes[1]:
                                boxes[0][self.board[x][y]-1] = 0
                            else:
                                return False
                        elif 6 <= y <=8:#box3
                            if self.board[x][y] in boxes[2]:
                                boxes[2][self.board[x][y]-1] = 0
                            else:
                                return False
                    elif 3 <= x <=5:
                        if 0 <= y <=2:#box4
                            if self.board[x][y] in boxes[3]:
                                boxes[3][self.board[x][y]-1] = 0
                            else:
                                return False
                        elif 3 <= y <=5:#box5
                            if self.board[x][y] in boxes[4]:
                                boxes[4][self.board[x][y]-1] = 0
                            else:
                                return False
                        elif 6 <= y <=8:#box6
                            if self.board[x][y] in boxes[5]:
                                boxes[5][self.board[x][y]-1] = 0
                            else:
                                return False
                    elif 6 <= x <=8:
                        if 0 <= y <=2:#box7
                            if self.board[x][y] in boxes[6]:
                                boxes[6][self.board[x][y]-1] = 0
                            else:
                                return False
                        elif 3 <= y <=5:#box8
                            if self.board[x][y] in boxes[7]:
                                boxes[7][self.board[x][y]-1] = 0
                            else:
                                return False
                        elif 6 <= y <=8:#box9
                            if self.board[x][y] in boxes[8]:
                                boxes[8][self.board[x][y]-1] = 0
                            else:
                                return False
         return True                   
    def Solver(self):
        SolverBoard = []
        for i in range(9):
            Blank = []
            for j in range(9):
                Blank.append([1,2,3,4,5,6,7,8,9])
            SolverBoard.append(Blank)
        output = []
        for x in range(9):
            row = []
            for y in range(9):
                row.append([0,0,0,0,0,0,0,0,0])
            output.append(row)    
        for x in range(9):
            for y in range(9):
                if self.Board[x][y] != 0:
                   for i in range(9):#Rows
                       pass
                   for i in range(9):#Columns
                       pass
                   for i in range(9):#Boxes
                       pass
        
        #create a copy of board
        #use existing numbers to cut possible numbers that need to be filled in
        #from numbers on board try to extrapolate some numbers that are valid
        #repeat until can no longer certain
        #iterate filling with remaining numbers whilst checking validity till solved
    def Generator(self):
        pass
    def Save(self):
        pass
    def Load(self):
        pass
                    
                    
                
                
