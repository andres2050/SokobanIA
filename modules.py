
def isBox(boxPosition, row, column):
    result = False
    for coords in boxPosition:
        if coords[0] == row and coords[1] == column:
            result = True
    return result

def isMoveValid(gameTable, goals, row, column, direction, nodeBoxPos):
    if direction == 'U':
        if gameTable[row][column] == 'W':
            return False
        elif isBox(nodeBoxPos, row, column):
            if isBox(nodeBoxPos, row - 1,column):
                return False
            elif gameTable[row - 1][column] == 'W':
                return False
            elif (gameTable[row - 2][column] == 'W' and gameTable[row - 1][column - 1] == 'W'):
                if not (goals.__contains__([row - 1, column])):
                    return False
            elif (gameTable[row - 2][column] == 'W' and gameTable[row - 1][column + 1] == 'W'):
                if not (goals.__contains__([row - 1, column])):
                    return False
            
        return True
    elif direction == 'D':
        if gameTable[row][column] == 'W':
            return False
        elif isBox(nodeBoxPos, row, column):
            if isBox(nodeBoxPos, row + 1, column):
                return False
            elif gameTable[row + 1][column] == 'W':
                return False
            elif (gameTable[row + 2][column] == 'W' and gameTable[row + 1][column - 1] == 'W'):
                if not (goals.__contains__([row+1,column])):
                    return False
            elif (gameTable[row + 2][column] == 'W' and gameTable[row + 1][column + 1] == 'W'):
                if not (goals.__contains__([row + 1, column])):
                    return False
            
        return True
    elif direction == 'R':
        if gameTable[row][column] == 'W':
            return False
        elif isBox(nodeBoxPos, row, column): 
            if isBox(nodeBoxPos, row, column + 1):
                return False
            elif gameTable[row][column + 1] == 'W':
                return False
            elif (gameTable[row][column + 2] == 'W' and gameTable[row + 1][column + 1] == 'W'):
                if not (goals.__contains__([row, column + 1])):
                    return False
            elif (gameTable[row][column + 2] == 'W' and gameTable[row - 1][column + 1] == 'W'):
                if not (goals.__contains__([row,column + 1])):
                    return False
            
        return True
    elif direction == 'L':
        if gameTable[row][column] == 'W':
            return False
        elif isBox(nodeBoxPos, row, column):
            if isBox(nodeBoxPos, row, column - 1):
                return False
            elif gameTable[row][column - 1] == 'W':
                return False
            elif (gameTable[row][column - 2] == 'W' and gameTable[row + 1][column - 1] == 'W'):
                if not (goals.__contains__([row,column - 1])):
                    return False
            elif (gameTable[row][column - 2] == 'W' and gameTable[row - 1][column - 1] == 'W'):
                if not (goals.__contains__([row, column - 1])):
                    return False
        return True

def moveBox(row, column, direction, nodeBoxPos):
    if not isBox(nodeBoxPos, row, column):
        return nodeBoxPos
    
    for box in nodeBoxPos:
            if box[0] == row and box[1] == column and direction == 'U':
                nodeBoxPos.remove(box)
                nodeBoxPos.append([row - 1,column])
            elif box[0] == row and box[1] == column and direction == 'D':
                nodeBoxPos.remove(box)
                nodeBoxPos.append([row + 1,column])
            elif box[0] == row and box[1] == column and direction == 'L':
                nodeBoxPos.remove(box)
                nodeBoxPos.append([row,column - 1])
            elif box[0] == row and box[1] == column and direction == 'R':
                nodeBoxPos.remove(box)
                nodeBoxPos.append([row, column + 1])
    
    return nodeBoxPos

def alreadyVisited(node, queue):
    for visitedNode in queue:
        if (visitedNode[1]== node[1]):
            if(visitedNode[0]== node[0]):
                return True
    
    return False

def isLevelCompleted(goals, boxPositions):
    result = True
    for goal in goals:
        if not boxPositions.__contains__(goal):
            result = False
    return result