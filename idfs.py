from modules import isLevelCompleted, isMoveValid, moveBox, alreadyVisited

def IDFS(gameTable, playerPositions, goals, boxPositions):
    nextNode = []
    rootNode = [[playerPositions[0], playerPositions[1]], [i[:] for i in boxPositions], '']
    queue = []
    queue.append(rootNode)
    depth = 0
    
    while(len(queue)>0):
        for node in queue:
            if(len(node[2]) <= depth):
                playerRow = node[0][0]
                playerColumn = node[0][1]
                boxPositions = [i[:] for i in node[1]]
                movements = node[2]

                if isMoveValid(gameTable, goals, playerRow - 1, playerColumn, 'U', boxPositions):
                    moveBox(playerRow - 1, playerColumn, 'U', boxPositions)
                    movements += 'U'
                    nextNode = [[playerRow - 1, playerColumn], [i[:] for i in boxPositions], movements]
                    
                    if not alreadyVisited(nextNode, queue):
                        queue.insert(0,nextNode)
            
                    movements = movements[:len(movements) - 1]
                    boxPositions = [i[:] for i in node[1]]

                if isMoveValid(gameTable, goals, playerRow + 1, playerColumn, 'D', boxPositions):
                    moveBox(playerRow + 1, playerColumn, 'D', boxPositions)
                    movements += 'D'
                    nextNode = [[playerRow + 1, playerColumn], [i[:] for i in boxPositions], movements]
                    
                    if not alreadyVisited(nextNode, queue):
                        queue.insert(0,nextNode)
                    
                    movements = movements[:len(movements) - 1]
                    boxPositions = [i[:] for i in node[1]]

                if isMoveValid(gameTable, goals, playerRow, playerColumn - 1, 'L', boxPositions):
                    moveBox(playerRow, playerColumn - 1, 'L', boxPositions)
                    movements += 'L'
                    nextNode = [[playerRow, playerColumn - 1], [i[:] for i in boxPositions], movements]
                    
                    if not alreadyVisited(nextNode, queue):
                        queue.insert(0,nextNode)
                    
                    movements = movements[:len(movements) - 1]
                    boxPositions = [i[:] for i in node[1]]

                if isMoveValid(gameTable, goals, playerRow, playerColumn + 1, 'R', boxPositions):
                    moveBox(playerRow,playerColumn + 1, 'R', boxPositions)
                    movements += 'R'
                    nextNode = [[playerRow, playerColumn + 1], [i[:] for i in boxPositions], movements]

                    if not alreadyVisited(nextNode, queue):
                        queue.insert(0,nextNode)

                    movements = movements[:len(movements) - 1]
                    boxPositions = [i[:] for i in node[1]]
                
                if isLevelCompleted(goals, boxPositions):
                    return movements
        depth+=1

    return "Not solution was found"