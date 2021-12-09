
from icecream import ic


def create_matrix(data):
    matrix = []
    for row in data.strip().split("\n"):
        matrix.append(list(map(int,row.strip())))

    return matrix


def find_basin(matrix, i, j):
    basin = set()
    coordinates = [(i,j)]
    row_count = len(matrix)
    col_count = len(matrix[0])
    while len(coordinates) > 0:
        i, j = coordinates.pop()
        if (i, j) in basin:
            continue

        basin.add((i,j))

        x, y = i - 1, j
        if x >= 0 and matrix[x][y] != 9:
            coordinates.append((x, y))

        x, y = i + 1, j
        if x <= row_count - 1 and matrix[x][y] != 9:
            coordinates.append((x, y))

        x, y = i, j - 1
        if y >= 0 and matrix[x][y] != 9:
            coordinates.append((x, y))

        x, y = i, j + 1
        if y <= col_count - 1 and matrix[x][y] != 9:
            coordinates.append((x, y))

    return basin


def part1(matrix):
    low_points = []
    row_count = len(matrix)
    col_count = len(matrix[0])
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            neighbors = []
            if i != 0:
                neighbors.append(matrix[i-1][j])
            if i != row_count - 1:
                neighbors.append(matrix[i+1][j])
            if j != 0:
                neighbors.append(matrix[i][j-1])
            if j != col_count - 1:
                neighbors.append(matrix[i][j+1])

            if all([x > col for x in neighbors]):
                low_points.append(col)

    return sum(low_points) + len(low_points)


def part2(matrix):
    # find all basins

    basin_sizes = []
    checked_coordinates = set()
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if col == 9:
                checked_coordinates.add((i,j))
                continue
            if (i,j) not in checked_coordinates:
                basin = find_basin(matrix, i, j)
                basin_sizes.append(len(basin))
                checked_coordinates = checked_coordinates | basin

    a, b, c = list(reversed(sorted(basin_sizes)))[0:3]

    return a * b * c

def read_input():
    with open("input") as f:
        return create_matrix(f.read())


if __name__ == "__main__":
    data = read_input()
    print(part1(data))
    print(part2(data))
