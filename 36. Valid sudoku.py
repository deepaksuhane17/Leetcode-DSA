from typing import List


def isValidSudoku(board: List[List[str]]) -> bool:
    
    i_sets, j_sets = [set()]*9, [set()]*9
    
    i_sets = [set() for i in range(9)]
    j_sets = [set() for i in range(9)]
    
    grids = {(i,j): set() for i in range(3) for j in range(3)}

    for i in range(9):
        for j in range(9):

            num = board[i][j]

            if num == ".":
                continue

            if num in i_sets[i]:
                print("i")
                print(i, j)
                print(i_sets[i])
                print(j_sets[i])
                return False
            if num in j_sets[j]:
                print("j")
                print(i, j)
                print(i_sets[j])
                print(j_sets[j])
                return False
            if num in grids[(i//3, j//3)]:
                print(i, j)
                print(grids[(i//3, j//3)])
                return False

            i_sets[i].add(num)
            j_sets[j].add(num)
            grids[(i//3, j//3)].add(num)

    return True


board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))