from modules import isLevelCompleted, isMoveValid, moveBox

def BFS(gameTable, playerPositions, goals, boxPositions):
    rootNode = [[playerPositions[0], playerPositions[1]], [i[:] for i in boxPositions], '']
    queue = []
    queue.append(rootNode)
    nextNodes = []

    for node in queue:
        playerRow = node[0][0]
        playerColumn = node[0][1]
        boxPositions = [i[:] for i in node[1]]
        movements = node[2]
        
        if isLevelCompleted(goals, boxPositions):
            print("Breadth First Search:")
            return movements
        
        if isMoveValid(gameTable, goals, playerRow-1, playerColumn,'U',boxPositions):
            moveBox(playerRow-1, playerColumn,'U', boxPositions)
            movements += 'U'
            nextNodes = [[playerRow-1, playerColumn], [i[:] for i in boxPositions], movements]
            flag = True
            
            for visitedNode in queue:
                if (visitedNode[1]== nextNodes[1]):
                    if(visitedNode[0]== nextNodes[0]):
                        flag = False
            
            if flag:
                queue.append(nextNodes)
            
            movements = movements[:len(movements) - 1]
            boxPositions = [i[:] for i in node[1]]

        if isMoveValid(gameTable, goals, playerRow+1, playerColumn, 'D', boxPositions):
            moveBox(playerRow+1,playerColumn,'D',boxPositions)
            movements += 'D'
            nextNodes = [[playerRow+1,playerColumn], [i[:] for i in boxPositions], movements]
            flag = True

            for visitedNode in queue:
                if (visitedNode[1]== nextNodes[1]):
                    if(visitedNode[0]== nextNodes[0]):
                        flag=False
            if flag:
                queue.append(nextNodes)
            
            movements = movements[:len(movements) - 1]
            boxPositions = [i[:] for i in node[1]]

        if isMoveValid(gameTable, goals, playerRow,playerColumn-1,'L',boxPositions):
            moveBox(playerRow,playerColumn-1,'L',boxPositions)
            movements += 'L'
            nextNodes = [[playerRow,playerColumn-1], [i[:] for i in boxPositions], movements]
            flag = True

            for visitedNode in queue:
                if (visitedNode[1]== nextNodes[1]):
                    if(visitedNode[0]== nextNodes[0]):
                        flag=False
            if flag:
                queue.append(nextNodes)
            
            movements = movements[:len(movements) - 1]
            boxPositions = [i[:] for i in node[1]]

        if isMoveValid(gameTable, goals, playerRow,playerColumn+1,'R',boxPositions):
            moveBox(playerRow,playerColumn+1,'R',boxPositions)
            movements += 'R'
            nextNodes = [[playerRow,playerColumn+1], [i[:] for i in boxPositions], movements]
            flag = True
            for visitedNode in queue:
                if (visitedNode[1]== nextNodes[1]):
                    if(visitedNode[0]== nextNodes[0]):
                        flag=False
            if flag:
                queue.append(nextNodes)
            
            movements = movements[:len(movements) - 1]
            boxPositions = [i[:] for i in node[1]]

    return False