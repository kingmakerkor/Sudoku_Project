import random

def generate_sudoku():

    puzzle = []
    # 0의 확률을 50%으로 고정 - 전체 18개 중 9개가 0이므로!
    numbers = [0] * 9 + list(range(1, 10))
    for _ in range(9):
        row = []
        for _ in range(9):
            #rand_int = random.randint(0, 9)
            rand_int = random.choice(numbers)
            row.append(rand_int)
        puzzle.append(row)

    return puzzle

sudoku_puzzle = generate_sudoku()
print_board(sudoku_puzzle)