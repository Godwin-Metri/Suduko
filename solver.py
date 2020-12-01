board =[
    [8, 1, 0, 0, 3, 0, 0, 2, 7],
    [0, 6, 2, 0, 5, 0, 0, 9, 0],
    [0, 7, 0, 0, 0, 0, 0, 0, 0],
    [0, 9, 0, 6, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 2, 0, 0, 0, 4],
    [0, 0, 8, 0, 0, 5, 0, 7, 0],
    [0, 0, 0, 0, 0, 0, 0, 8, 0],
    [0, 2, 0, 0, 1, 0, 7, 5, 0],
    [3, 8, 0, 0, 7, 0, 0, 4, 2]
]

def solve(bor):
    pos = check_Zeros(bor)
    if pos == None:
        print("The Board is solved")
        return True
    else:
        row, col = pos
    for i in range(1, 10):
        if valid(bor, (row, col), i):
            bor[row][col] = i

            if solve(bor) == True:
                return True
            bor[row][col] = 0
    return False



def valid(bor, pos, num):

    #Checking for rows
    for j in range(len(bor[0])):
        if bor[pos[0]][j] == num:
            return False

    # Checking for columns
    for i in range(len(bor[0])):
        if bor[i][pos[1]] == num:
            return False

    # Checking for Box
    y = pos[0] // 3
    x = pos[1] // 3
    for i in range(y*3, y*3+3):
        for j in range(x*3, x*3+3):
            if bor[i][j] == num:
                return False

    return True

def draw(bor):
    h_line = 0
    v_line = 0
    for i in range(len(bor)):
        h_line += 1
        for j in range(len(bor[i])):
            v_line += 1
            print(bor[i][j], end=' ')
            if v_line % 3 == 0 and v_line % 9 != 0:
                print('', end='| ')
            if j == 8:
                print()
        if h_line == 3 or h_line == 6:
            print('-----------------------')

def check_Zeros(bor):
    for i in range(len(bor)):
        for j in range(len(bor[0])):
            if bor[i][j] == 0:
                return (i, j)
    return None

draw(board)
print('-------------------------------------------------')
solve(board)
draw(board)