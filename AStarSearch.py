import queue as q
from math import fabs as abs
import MazeHandling


def aStar(startX, startY, goalX, goalY, maze):

    frontier = q.PriorityQueue()
    frontier.put_nowait((heuristic(startX, startY, goalX, goalY), 0, startX, startY, startX, startY))
    usedNodes = dict()

    def expandNode(heur, c, currX, currY, prevX, prevY):

        successors = {(currX + 1, currY), (currX - 1, currY), (currX, currY + 1), (currX, currY - 1)}

        costs = c + 1
        for successor in successors:
            if maze[successor[0]][successor[1]] == 'x':
                continue

            if usedNodes.__contains__((successor[0], successor[1])):
                usedNode = usedNodes.get((currX, currY))

                if c + 1 < usedNode[1]:
                    costs = c + 1
                    usedNodes[(currX, currY)] = (0, costs, currX, currY, prevX, prevY)
                continue

            frontier.put_nowait((heuristic(currX, currY, goalX, goalY), costs, successor[0], successor[1], currX, currY))

    while True:

        currentNode = frontier.get_nowait()
        heu_value = currentNode[0]
        curr_cost = currentNode[1]
        curr_x = currentNode[2]
        curr_y = currentNode[3]
        prev_x = currentNode[4]
        prev_y = currentNode[5]

        usedNodes[(curr_x, curr_y)] = ((currentNode))

        if curr_x == goalX and curr_y == goalY:
            print("Das Ziel wurde gefunden auf x = ", curr_x, " und y = ", curr_y)
            drawPath(usedNodes, goalX, goalY, startX, startY, maze)
            break

        expandNode(heu_value, curr_cost, curr_x, curr_y, prev_x, prev_y)

        if frontier.empty():
            print("Es wurden alle Felder abgelaufen. Kein Ziel konnte gefunden werden.")
            exit()


#Heuristik der Manhattan-Abschätzung
def heuristic(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


#Markiert gelaufenen Pfad mit '-'
def drawPath(closedList, goalX, goalY, startX, startY, maze):
    prevX = goalX
    prevY = goalY
    prevNode = closedList[prevX, prevY]

    while prevNode[1] != 1:

        prevX = prevNode[4]
        prevY = prevNode[5]

        maze[prevX][prevY] = '-'
        print(prevX, prevY)
        prevNode = closedList[prevX, prevY]

    MazeHandling.printMaze(maze)


