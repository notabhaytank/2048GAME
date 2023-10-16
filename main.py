import random
import msvcrt
import os

GRID_SIZE = 4
grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]


def add_new_2(grid):
    r = random.randint(0, 3)
    c = random.randint(0, 3)
    while grid[r][c] != 0:
        r = random.randint(0, 3)
        c = random.randint(0, 3)
    grid[r][c] = 2
    return grid


def reverse(grid):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(grid[i][4 - j - 1])

    return new_mat


def transpose(grid):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(grid[j][i])
    return new_mat


def merge(grid):
    for i in range(4):
        for j in range(3):
            if grid[i][j] == grid[i][j + 1] and grid[i][j] != 0:
                grid[i][j] = grid[i][j] * 2
                grid[i][j + 1] = 0
    return grid


def compress(grid):
    new_mat = []
    for i in range(4):
        new_mat.append([0] * 4)

    for i in range(4):
        pos = 0
        for j in range(4):
            if grid[i][j] != 0:
                new_mat[i][pos] = grid[i][j]
                pos += 1
    return new_mat


def move_up(grid):
    transposed_grid = transpose(grid)
    new_grid = compress(transposed_grid)
    new_grid = merge(new_grid)
    new_grid = compress(new_grid)
    final_grid = transpose(new_grid)
    return final_grid


def move_down(grid):
    transposed_grid = transpose(grid)
    reversed_grid = reverse(transposed_grid)
    new_grid = compress(reversed_grid)
    new_grid = merge(new_grid)
    new_grid = compress(new_grid)
    final_reversed_grid = reverse(new_grid)
    final_grid = transpose(final_reversed_grid)
    return final_grid


def move_right(grid):
    reversed_grid = reverse(grid)
    new_grid = compress(reversed_grid)
    new_grid = merge(new_grid)
    new_grid = compress(new_grid)
    final_grid = reverse(new_grid)
    return final_grid


def move_left(grid):
    new_grid = compress(grid)
    new_grid = merge(new_grid)
    new_grid = compress(new_grid)
    return new_grid


def get_current_state(grid):
    # Anywhere 2048 is present
    for i in range(4):
        for j in range(4):
            if (grid[i][j] == 2048):
                return 'WON'
    # Anywhere 0 is present
    for i in range(4):
        for j in range(4):
            if (grid[i][j] == 0):
                return 'GAME NOT OVER'
    # Every Row and Column except last row and last column
    for i in range(3):
        for j in range(3):
            if (grid[i][j] == grid[i + 1][j] or grid[i][j] == grid[i][j + 1]):
                return 'GAME NOT OVER'
    # Last Row
    for j in range(3):
        if grid[3][j] == grid[3][j + 1]:
            return 'GAME NOT OVER'
    # Last Column

    for i in range(3):
        if grid[i][3] == grid[i + 1][3]:
            return 'GAME NOT OVER'

    return 'LOST'

def print_grid():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("2048 Game!")
    print("-" * 20)
    for row in grid:
        for val in row:
            print(f'{val:5}', end=' ')
        print()

if __name__ == '__main__':
    add_new_2(grid)
    while True:
        print_grid()
        key = ord(msvcrt.getch())
        if key == 72:  # Up arrow
            grid = move_up(grid)
            add_new_2(grid)
        elif key == 80:  # Down arrow
            grid = move_down(grid)
            add_new_2(grid)
        elif key == 77:  # Right arrow
            grid = move_right(grid)
            add_new_2(grid)
        elif key == 75:  # Left arrow
            grid = move_left(grid)
            add_new_2(grid)

        state = get_current_state(grid)
        if state == "WON":
            print("You Won")
            break
        elif state == "LOST":
            print("You Lose")
            break
        elif state == "GAME NOT OVER":
            continue






