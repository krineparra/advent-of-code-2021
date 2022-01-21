with open('09-data.txt') as file:
    data = [list(map(int, list(d))) for d in [d[:-1] for d in file.readlines()]]


def is_end_basin(y, x):
    basin_temp = 1
    data[y][x] = 9
    if (x + 1 < len(data[0])) and data[y][x + 1] != 9:
        basin_temp += is_end_basin(y, x + 1)
    if (x > 0) and data[y][x - 1] != 9:
        basin_temp += is_end_basin(y, x - 1)
    if (y + 1) < len(data) and data[y + 1][x] != 9:
        basin_temp += is_end_basin(y + 1, x)
    if (y > 0) and data[y - 1][x] != 9:
        basin_temp += is_end_basin(y - 1, x)
    return basin_temp


result = []
for xi in range(len(data[0])):
    for yi in range(len(data)):
        value = data[yi][xi]
        right = data[yi][xi - 1] if xi > 0 else 9
        left = data[yi][xi + 1] if xi < (len(data[0]) - 1) else 9
        up = data[yi - 1][xi] if yi > 0 else 9
        down = data[yi + 1][xi] if yi < (len(data) - 1) else 9
        if value < right and value < left and value < down and value < up:
            result.append(is_end_basin(yi, xi))
val_max = 1
for i in range(3):
    val_max *= max(result)
    result.remove(max(result))
print(val_max)
