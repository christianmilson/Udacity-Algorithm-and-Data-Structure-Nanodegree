from heapq import heappop, heappush
from math import sqrt, pow

def getDistance(origin, dest) -> int :
    x_axis = dest[1] - origin[1]
    y_axis = dest[0] - origin[0]

    return sqrt(pow(x_axis,2) + pow(y_axis,2))

def buildPath(cameFrom, current) -> list :
    route = list()
    node = current
    while node is not None:
        route.append(node)
        node = cameFrom[node]

    route.reverse()
    return route
    
def shortest_path(M,start,goal):
    open = []
    cameFrom = {}
    gScore = {}
    fScore = {}
    heappush(open, (0, start))

    cameFrom[start] = None
    fScore[start] = 0
    gScore[start] = 0

    while len(open) > 0:
        current = heappop(open)[1]

        if (current == goal):
            return buildPath(cameFrom, current)

        for neighbour in M.roads[current]:
            score = gScore[current] + getDistance(M.intersections[current], M.intersections[neighbour])

            if (neighbour not in fScore or score < gScore[neighbour]):
                gScore[neighbour] = score
                fScore[neighbour] = score + getDistance(M.intersections[neighbour], M.intersections[goal])
                cameFrom[neighbour] = current
                heappush(open, (fScore[neighbour], neighbour))
                
    return -1