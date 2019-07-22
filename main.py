import sys
from bfs import BFS
from dfs import DFS
from idfs import IDFS

gameTable = []
goals = []
boxPositions = []
playerPositions = []

def readLevel(txtFile):
    j = 0
    i = 0

    for line in txtFile.splitlines():
        try:
            if line[1] == ',': 
                if len(playerPositions) == 0:
                    playerPositions.append(int(line[0]))
                    playerPositions.append(int(line[2]))
                else:
                    boxPositions.append([int(line[0]), int(line[2])])
            else:
                j = 0
                temp = []
                for a in line.replace('\n',''):
                    temp.append(a)
                    if a == 'X':
                        goals.append([i, j])
                    j += 1
                gameTable.append(temp)
            i += 1
        
        except IndexError:
            pass

readLevel(sys.argv[1])

print(BFS(gameTable, playerPositions, goals, boxPositions))

print(DFS(gameTable, playerPositions, goals, boxPositions))

print(IDFS(gameTable, playerPositions, goals, boxPositions))
