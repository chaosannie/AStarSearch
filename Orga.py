import MazeHandling
import AStarSearch


originalMaze = MazeHandling.readMazeToArray("blatt3_environment.txt")
startCoordinates = MazeHandling.findCoordinates(originalMaze, 's')
startX, startY = startCoordinates[0][0], startCoordinates[0][1]


goals = MazeHandling.findCoordinates(originalMaze, 'g')

if not goals:# Prüft ob ein Ziel enthalten ist
    print("Kein Ziel gefunden")
    exit()


for goal in goals:
    goalX = goal[0]
    goalY = goal[1]
    originalMaze[goalX][goalY] = 'g'
    print(AStarSearch.aStar(startX, startY, goalX, goalY, originalMaze))