def readMazeToArray(path):
    with open(path) as f:
        return [list(line.strip()) for line in f]


def printMaze(maze):
    print('\n'.join([''.join(['{:1}'.format(item) for item in row])
                     for row in maze]))


def findCoordinates(maze, target):
    goals = []
    for i in range(0, len(maze)):
        for j in range(0, len(maze[i])):
            if maze[i][j] == target:
                goals.append([i, j])
    return goals

