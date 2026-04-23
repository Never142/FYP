import copy
import random
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
def SudokuUniqueSolutions(Board):
    count = 0 
    for y in range(9):
        for x in range(9):
            newBoard = copy.deepcopy(Board)
            if newBoard[8-y][8-x] == 0:
                    break
            for i in range(9):
                newBoard[8-y][8-x] = i+1 
                if SolverBrute(newBoard):
                    count+=1
    return count     
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
Board = [[0,0,7,0,0,0,0,0,3],
         [1,5,9,0,0,0,0,0,0],
         [0,0,8,0,0,0,2,0,7],
         [0,0,0,2,0,0,0,4,6],
         [0,4,0,0,0,7,0,0,0],
         [5,0,0,8,0,0,0,0,0],
         [0,8,0,0,5,0,9,0,0],
         [0,0,0,0,0,0,1,0,0],
         [0,0,0,0,9,1,0,7,0]]
           
            
def Save(Board):
    file = open("Boardsave.txt","w")
    savetext = ""
    for i in Board:
        for j in i:
            savetext = savetext+","+str(j)
    for i in Board:
        for j in i:
            savetext = savetext+","+str(j)        
    #savetext = savetext+","+str(self.Time)
    #savetext = savetext+","+str(self.Points)
    file.write(savetext)        
    file.close()
    return True
Save(Board)
file=open("Boardsave.txt","r")
templist = file.readline().split(",")
del templist[0]
NewBoard = []
for y in range(9):
    NewBoard.append([])
    for x in range(9):
        NewBoard[y].append(int(templist[(y*9)+(x)]))
NewBoard = []
for y in range(9):
    NewBoard.append([])
    for x in range(9):
        NewBoard[y].append(int(templist[81+(y*9)+(x)]))        
for i in NewBoard:
    print(i)                       

file.close()