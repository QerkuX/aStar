import math
import copy

def occupied(position, moves):
    for move in moves:
        if move[0] == position[0] and move[1] == position[1]:
            return True
    return False

def inBoundries(position, mapSize):
    if position[0] > mapSize or position[0] < 0 or position[1] > mapSize or position[1] < 0:
        return False
    return True

def addMoves(moves, position, explored, around, start, end, mapSize):
    for newMove in around:
        newPos = [position[0] + newMove[0], position[1] + newMove[1]]
        if not occupied(newPos, explored) and not occupied(newPos, moves) and inBoundries(newPos, mapSize):
            score = round(math.dist(newPos, start) + math.dist(newPos, end), 2)
            moves.append([newPos[0], newPos[1], score, len(explored)-1])


def aStar(start, end, mapSize, obsticles):
    explored = copy.copy(obsticles)
    moves = [[start[0], start[1], 0, len(explored)]]
    around = [
        [0,-1],
        [0,1],
        [1,0],
        [-1,0],
        [1,1],
        [1,-1],
        [-1,1],
        [-1,-1],
    ]

    while True:
        smallest = 0
        for option in range(len(moves)):
            if moves[option][2] < moves[smallest][2]:
                smallest = option
        explored.append([moves[smallest][0], moves[smallest][1], moves[smallest][3]])
        addMoves(moves, moves[smallest], explored, around, start, end, mapSize)

        if moves[smallest][0] == end[0] and moves[smallest][1] == end[1]:
            break
        
        moves.pop(smallest)

    path = [[moves[smallest][0], moves[smallest][1]]]
    iterate = moves[smallest][3]
    
    while True:
        path.append([explored[iterate][0], explored[iterate][1]])
        iterate = explored[iterate][2]
        if explored[iterate][0] == start[0] and explored[iterate][1] == start[1]:
            break

    path.reverse()    
    return path

# Example   ([0, 0], [10, 10], 10, [[5, 5]])
path = aStar()

