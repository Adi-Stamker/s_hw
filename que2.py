# targil 2
# tic-tac-toe
def tic_tac_toe(mat):
    if mat[0][0] == mat[1][1] and mat[1][1] == mat[2][2]:
        return mat[0][0]
    if mat[0][2] == mat[1][1] and mat[2][1] == mat[2][0]:
        return mat[0][2]
    else:
        if is_found(mat, 1):
             return 1
        if is_found(mat, 2):
            return 2
    return 0

def is_found(mat, num):
    count_column = [0,0,0]
    count_row = 0
    # found in row
    for row in mat:
        count_row = 0
        for i in range(3):
            if row[i] == num:
                count_column[i]+=1 # found in column
        for j in row:
            if j == num:
                count_row+=1
        if count_row == 3:
            break

    if count_row == 3:
        return True
    for item in count_column:
        if item == 3:
            return True
    return False

game = [[1,2,0],
        [2,1,0],
        [2,1,1]]

print("winner is:", tic_tac_toe(game))