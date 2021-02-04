'''
This module checks if the table for the game is valid. 
'''


def rows(board):
    '''
    Checks rows.
    >>> rows([
"**** ****",
"***1 ****",
"**  3****",
"* 4 1****",
"     9 5 ",
" 6  83  *",
"3   1  **",
"  8  2***",
"  2  ****"
])
    True
    '''
    element_united = []
    for line in board:
        element_united = [s.replace('*', '') for s in line]

        while ' ' in element_united:
            element_united.remove(' ')
        while '' in element_united:
            element_united.remove('')

        len_start = len(element_united)
        len_end = len(set(element_united))

        if len_start > len_end:
            return False

    return True


# print(rows([
#     "**** ****",
#     "***1 ****",
#     "**  3****",
#     "* 4 1****",
#     "     9 5 ",
#     " 6  83  *",
#     "3   1  **",
#     "  8  2***",
#     "  2  ****"
# ]))


def kolonku(board):
    '''
    Checks columns.
    >>> kolonku([
"**** ****",
"***1 ****",
"**  3****",
"* 4 1****",
"     9 5 ",
" 6  83  *",
"3   1  **",
"  8  2***",
"  2  ****"
])
    False
    '''
    all_lines = []
    for line in board:
        all_lines.append([x for x in line])

    column = []
    all_columns = []
    for i in range(len(all_lines)):
        for line in all_lines:
            column.append(line[i])
            column_str = ''.join(column)
        all_columns.append(column_str)
        column = []
    # print(all_columns)

    if rows(all_columns) == False:
        return False
    return True


# print(kolonku([
#     "**** ****",
#     "***1 ****",
#     "**  3****",
#     "* 4 1****",
#     "     9 5 ",
#     " 6  83  *",
#     "3   1  **",
#     "  8  2***",
#     "  2  ****"
# ]))


def blocks(board):
    '''
    Checks color blocks.
    >>> blocks([
"**** ****",
"***1 ****",
"**  3****",
"* 4 1****",
"     9 5 ",
" 6  83  *",
"3   1  **",
"  8  2***",
"  2  ****"
])
    True
    '''
    board1 = []
    for line in board:
        line1 = [x for x in line]
        board1.append(line1)

    block = []
    purple = []
    blue = []
    mint = []
    green = []
    yellow = []

    for i in range(5):
        purple.append(board1[i][4])
    for k in range(5, 9):
        purple.append(board1[4][k])
    block.append(''.join(purple))

    for i in range(1, 6):
        blue.append(board1[i][3])
    for k in range(4, 8):
        blue.append(board1[5][k])
    block.append(''.join(blue))

    for i in range(2, 7):
        mint.append(board1[i][2])
    for k in range(3, 7):
        mint.append(board1[6][k])
    block.append(''.join(mint))

    for i in range(3, 8):
        green.append(board1[i][1])
    for k in range(2, 6):
        green.append(board1[7][k])
    block.append(''.join(green))

    for i in range(4, 9):
        yellow.append(board1[i][0])
    for k in range(1, 5):
        yellow.append(board1[8][k])
    block.append(''.join(yellow))

    block1 = []
    for line in block:
        line1 = ''.join(line.split())
        block1.append(line1)

    for element in block1:
        element2 = [x for x in element]
        len_start = len(element2)
        len_end = len(set(element2))

        if len_start > len_end:
            return False
        return True


print(blocks([
    "**** ****",
    "***1 ****",
    "**  3****",
    "* 4 1****",
    "     9 5 ",
    " 6  83  *",
    "3   1  **",
    "  8  2***",
    "  2  ****"
]))


def validate_board(board):
    '''
    Checks the whole table.
    >>> validate_board([
"**** ****",
"***1 ****",
"**  3****",
"* 4 1****",
"     9 5 ",
" 6  83  *",
"3   1  **",
"  8  2***",
"  2  ****"
])
    False
    '''
    if rows(board) == False or kolonku(board) == False or blocks(board) == False:
        return False
    return True


# print(validate_board([
#     "**** ****",
#     "***1 ****",
#     "**  3****",
#     "* 4 1****",
#     "     9 5 ",
#     " 6  83  *",
#     "3   1  **",
#     "  8  2***",
#     "  2  ****"
# ]))
