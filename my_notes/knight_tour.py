N = 5
visited = [[0 for _ in range(N)] for _ in range(N)]

# Knight's steps
row = [2, 1, -1, -2, -2, -1,  1,  2]
col = [1, 2,  2,  1, -1, -2, -2, -1]
knight_moves = 8
assert len(row) == knight_moves
assert len(col) == knight_moves


def is_valid(x, y):
    return False if x < 0 or y < 0 or x >= N or y >= N else True


def knight_tour(x, y, steps):
    visited[x][y] = steps
    if steps >= (N*N):
        # fin, reset the state for the next backtracking iteration
        print(visited)
        visited[x][y] = 0
        return

    for i in range(knight_moves):
        new_x = x + row[i]
        new_y = y + col[i]
        if is_valid(new_x, new_y) and visited[new_x][new_y] == 0:
            knight_tour(new_x, new_y, steps + 1)

    # backtracking has been  pass (x,y) and remove it from the current path
    visited[x][y] = 0


def main():
    knight_tour(0, 0, 1)


if __name__ == '__main__':
    main()
