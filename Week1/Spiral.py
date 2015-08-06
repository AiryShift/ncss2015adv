RIGHT = 1
DOWN = 2
LEFT = 3
UP = 4
spiral = int(input('Enter size: '))
spiral = [['.'] * spiral for _ in range(spiral)]
x, y = 0, 0
spiral[y][x] = '-'
instruct = RIGHT


def isValid(n):
    if 0 <= n < len(spiral):
        return True
    return False


def printSpiral():
    for i in spiral:
        print(' '.join(i))


while True:
    tempX, tempY = x, y
    if instruct == RIGHT:
        tempX += 1
        if isValid(tempX) and spiral[tempY][tempX] == '.':
            bound = tempX
            while isValid(bound + 1) and spiral[tempY][bound + 1] == '.':
                bound += 1
            spiral[tempY][bound] = '\\'
            for i in range(tempX, bound):
                spiral[tempY][i] = '-'
            instruct = DOWN
            x, y = bound, tempY
        else:
            break
    elif instruct == DOWN:
        tempY += 1
        if isValid(tempY) and spiral[tempY][tempX] == '.':
            bound = tempY
            while isValid(bound + 1) and spiral[bound + 1][tempX] == '.':
                bound += 1
            spiral[bound][tempX] = '/'
            for i in range(tempY, bound):
                spiral[i][tempX] = '|'
            instruct = LEFT
            x, y = tempX, bound
        else:
            break
    elif instruct == LEFT:
        tempX -= 1
        if isValid(tempX) and spiral[tempY][tempX] == '.':
            bound = tempX
            while isValid(bound - 1) and spiral[tempY][bound - 1] == '.':
                bound -= 1
            spiral[tempY][bound] = '\\'
            for i in range(tempX, bound, -1):
                spiral[tempY][i] = '-'
            instruct = UP
            x, y = bound, tempY
        else:
            break
    elif instruct == UP:
        tempY -= 1
        if isValid(tempY) and spiral[tempY][tempX] == '.':
            bound = tempY
            while isValid(bound - 1) and spiral[bound - 1][tempX] == '.':
                bound -= 1
            spiral[bound][tempX] = '/'
            for i in range(tempY, bound, -1):
                spiral[i][tempX] = '|'
            instruct = RIGHT
            x, y = tempX, bound
        else:
            break

printSpiral()
