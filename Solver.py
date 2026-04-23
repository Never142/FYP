def Solver(InputBoard):
    SolverBoard = []
    rows = []
    columns = []
    boxes = []
    constraints = [rows,columns,boxes]
    for i in constraints:
        for j in range(9):
            i.append([1,2,3,4,5,6,7,8,9])
    for i in range(9):
        Blank = []
        for j in range(9):
            Blank.append([1,2,3,4,5,6,7,8,9])
        SolverBoard.append(Blank)
    OutputBoard = []
    for x in range(9):
        OutputBoard.append([0,0,0,0,0,0,0,0,0])
    for x in range(9):
        for y in range(9):
            if InputBoard[y][x] != 0:
                SolverBoard[y][x] = [InputBoard[y][x]]
                if InputBoard[y][x] in rows:
                    rows[y].remove(InputBoard[y][x])
                if InputBoard[y][x] in columns:    
                    columns[x].remove(InputBoard[y][x])
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
                    boxes[BoxIndex].remove(InputBoard[y][x])  


    for times in range(3):     
        for x in range(9):
            for y in range(9):
                if InputBoard[y][x] != 0 or len(SolverBoard[y][x]) > 1:
                    for i in range(9):
                        if i != x and (InputBoard[y][x] in SolverBoard[y][i]):#Rows
                            SolverBoard[y][i].remove(InputBoard[y][x])
                        if i != y and (InputBoard[y][x] in SolverBoard[i][x]):#Columns
                            SolverBoard[i][x].remove(InputBoard[y][x])
                    #[x]  [0-2,  3-5,  6-8] y
                    #[0-2][box1, box2, box3]
                    #[3-5][box4, box5, box6]
                    #[6-8][box7, box8, box9]
                    if 0<=x<=2:#defining the boxes start
                        BoxX=0
                    elif 3<=x<=5:
                        BoxX=3
                    elif 6<=x<=8:
                        BoxX=6
                        
                    if 0<=y<=2:
                        BoxY = 0
                    elif 3<=y<=5:
                        BoxY = 3
                    elif 6<=y<=8:
                        BoxY = 6

                    for i in range(BoxY,BoxY+3):
                        for j in range(BoxX,BoxX+3):
                            if i != y and j != x and (InputBoard[y][x] in SolverBoard[i][j]):
                                SolverBoard[i][j].remove(InputBoard[y][x])
    for x in range(9):
        for y in range(9):
            RowList = []
            ColumnList = []
            BoxList = []
            for i in range(9):#find the difference between each set in SolverBoard
                #Row
                #Column
                pass

    #check if 1 instance exists in row/column/box In SolverBoard
    #take results to output
    for x in range(9):
        for y in range(9):                    
            if len(SolverBoard[y][x]) == 1:
                OutputBoard[y][x] = SolverBoard[y][x][0]
  
  
                       


    return OutputBoard
Board = [[0,0,7,0,0,0,0,0,3],
         [1,5,9,0,0,0,0,0,0],
         [0,0,8,0,0,0,2,0,7],
         [0,0,0,2,0,0,0,4,6],
         [0,4,0,0,0,7,0,0,0],
         [5,0,0,8,0,0,0,0,0],
         [0,8,0,0,5,0,9,0,0],
         [0,0,0,0,0,0,1,0,0],
         [0,0,0,0,9,1,0,7,0]]
           
            
        

for i in Board:
    print(i)
for i in range(3):
    Board = Solver(Board)
    print ("-")
    for j in Board:
        print(j)
   