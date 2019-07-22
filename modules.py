
def isBox(boxPosition, row, column):
    result = False
    for coords in boxPosition:
        if coords[0] == row and coords[1] == column:
            result = True
    return result

def isMoveValid(gameTable, goals, row, column, direction, nodeBoxPos):
    if gameTable[row][column] == 'W':
        return False
    
    if direction == 'U':
        if isBox(nodeBoxPos, row, column):
            if isBox(nodeBoxPos, row - 1, column):
                return False

            if gameTable[row - 1][column] == 'W':
                return False

            if (gameTable[row - 2][column] == 'W' and gameTable[row - 1][column - 1] == 'W'):
                if not (goals.__contains__([row - 1, column])):
                    return False

            if (gameTable[row - 2][column] == 'W' and gameTable[row - 1][column + 1] == 'W'):
                if not (goals.__contains__([row - 1, column])):
                    return False

        return True
        
    if direction == 'D':
        if isBox(nodeBoxPos, row, column):
            if isBox(nodeBoxPos, row + 1, column):
                return False

            if gameTable[row + 1][column] == 'W':
                return False

            if (gameTable[row + 2][column] == 'W' and gameTable[row + 1][column - 1] == 'W'):
                if not (goals.__contains__([row+1,column])):
                    return False

            if (gameTable[row + 2][column] == 'W' and gameTable[row + 1][column + 1] == 'W'):
                if not (goals.__contains__([row + 1, column])):
                    return False
            
        return True

    if direction == 'R':
        if isBox(nodeBoxPos, row, column): 
            if isBox(nodeBoxPos, row, column + 1):
                return False

            if gameTable[row][column + 1] == 'W':
                return False

            if (gameTable[row][column + 2] == 'W' and gameTable[row + 1][column + 1] == 'W'):
                if not (goals.__contains__([row, column + 1])):
                    return False

            if (gameTable[row][column + 2] == 'W' and gameTable[row - 1][column + 1] == 'W'):
                if not (goals.__contains__([row, column + 1])):
                    return False
            
        return True

    if direction == 'L':
        if isBox(nodeBoxPos, row, column):
            if isBox(nodeBoxPos, row, column - 1):
                return False

            if gameTable[row][column - 1] == 'W':
                return False

            if (gameTable[row][column - 2] == 'W' and gameTable[row + 1][column - 1] == 'W'):
                if not (goals.__contains__([row,column - 1])):
                    return False

            if (gameTable[row][column - 2] == 'W' and gameTable[row - 1][column - 1] == 'W'):
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
            return nodeBoxPos

        if box[0] == row and box[1] == column and direction == 'D':
            nodeBoxPos.remove(box)
            nodeBoxPos.append([row + 1,column])
            return nodeBoxPos

        if box[0] == row and box[1] == column and direction == 'L':
            nodeBoxPos.remove(box)
            nodeBoxPos.append([row,column - 1])
            return nodeBoxPos

        if box[0] == row and box[1] == column and direction == 'R':
            nodeBoxPos.remove(box)
            nodeBoxPos.append([row, column + 1])
            return nodeBoxPos


def alreadyVisited(node, queue):
    for visitedNode in queue:
        if visitedNode[0] == node[0] and visitedNode[1] == node[1]:
            return True
    
    return False

def isLevelCompleted(goals, boxPositions):
    for goal in goals:
        if not boxPositions.__contains__(goal):
            return False
    return True