bound = []
for y in range(9):
    bound.append([])
    for x in range(9):
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
        bound[y].append(list(boundX.intersection(boundY))[0]-1)
for i in bound:
    print(i)            
            