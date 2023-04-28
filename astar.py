import math
import copy
import time
import os

def main():
    answer = int(input("WHAT DO YOU WANT TO DO: \n1. First test map \n2. Second test map \n3. Third test map \n4. Map creator \n"))

    data = []
    match(answer):
        case 1:
            data = [
                [0,0],
                [10,10],
                10,
                [
                    [3,5],
                    [4,5],
                    [5,5],
                    [6,5],
                    [7,5],
                ],
                0.1
            ]
        case 2:
            data = [
                [0,0],
                [5,5],
                5,
                [
                    [2,1],
                    [1,1],
                    [1,2],
                    [0,2]
                ],
                0.1
            ]
        case 3:
            data = [
                [2,1],
                [7, 8],
                10,
                [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [0, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [0, 2], [9, 2], [0, 3], [4, 3], [5, 3], [6, 3], [7, 3], [9, 3], [0, 4], [2, 4], [3, 4], [4, 4], [7, 4], [9, 4], [0, 5], [2, 5], [3, 5], [4, 5], [5, 5], [6, 5], [7, 5], [8, 5], [9, 5], [0, 6], [2, 6], [3, 6], [8, 6], [0, 7], [2, 7], [3, 7], [5, 7], [6, 7], [8, 7], [0, 8], [5, 8], [6, 8], [8, 8], [0, 9], [1, 9], [2, 9], [3, 9], [4, 9], [5, 9], [6, 9], [7, 9], [8, 9]],
                0.05
            ]
        case 4:
            data = mapCreator()
    
    return aStar(data[0], data[1], data[2], data[3], data[4])


def mapCreator():
    mapSize = int(input("Enter map size: "))
    speed = float(input("Enter time between frames (0 for instant)"))
    print("WRITE COORDINATES USING COMMA (e.g. 5,3)")
    start = list(map(int, input("Enter start coordinates: ").split(',')))
    end = list(map(int, input("Enter end coordinates: ").split(',')))
    obsticles = []
    print("WRITE 'S' TO QUIT")
    while True:
        temp = input("Enter obsticle coordinates: ")

        if temp == 'S' or temp == 's':
            break

        obsticles.append(list(map(int, temp.split(','))))

    return [start, end, mapSize, obsticles, speed]


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


def aStar(start, end, mapSize, obsticles, speed):
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
        
        for y in range(mapSize+1):
            for x in range(mapSize+1):
                if start[0] == x and start[1] == y or end[0] == x and end[1] == y:
                    print("@", end=" ")
                elif occupied([x, y], obsticles):
                    print("\U000025FC", end=" ")
                elif occupied([x, y], explored):
                    print("x", end=" ")
                elif occupied([x, y], moves):
                    print("o", end=" ")
                else:
                    print(" ", end=" ")
            print()

        if moves[smallest][0] == end[0] and moves[smallest][1] == end[1]:
            break
        
        moves.pop(smallest)
        
        time.sleep(speed)
        os.system("cls")

    path = [[moves[smallest][0], moves[smallest][1]]]
    iterate = moves[smallest][3]
    while True:
        path.append([explored[iterate][0], explored[iterate][1]])
        iterate = explored[iterate][2]
        if explored[iterate][0] == start[0] and explored[iterate][1] == start[1]:
            break
    
    os.system("cls")
    for y in range(mapSize+1):
        for x in range(mapSize+1):
            if start[0] == x and start[1] == y or end[0] == x and end[1] == y:
                print("@", end=" ")
            elif occupied([x, y], obsticles):
                print("\U000025FC", end=" ")
            elif occupied([x, y], path):
                print("o", end=" ")
            else:
                print(" ", end=" ")
        print()

    path.reverse() 
    return path

if __name__ == '__main__':
    print(main())
    x = input("Press anything to exit...")
