with open('noel20data.txt') as file :
    data = [list(map(int,list(d[:-1]))) for d in file.readlines()]
len_data = len(data)
not_flash = 1
i = 0
while not_flash:
    nb_flashes = 0
    i += 1
    data = [list(map((lambda x : x+1),d)) for d in data]
    while sum([sum(d) for d in list(list(filter(lambda x : x>9, d)) for d in data)]) > 0:
        for x in range(len_data):
            for y in range(len_data) :
                if data[x][y] > 9 :
                    data[x][y] = 0
                    nb_flashes += 1
                    if ((x+1)<len_data and (y+1)<len_data and data[x+1][y+1] != 0) : data[x+1][y+1] += 1
                    if ((x+1)<len_data and data[x+1][y] != 0) : data[x+1][y] += 1
                    if ((y+1)<len_data and data[x][y+1] != 0) : data[x][y+1] += 1
                    if (x>0 and y>0 and data[x-1][y-1] != 0) : data[x-1][y-1] += 1
                    if (x>0 and data[x-1][y] != 0) : data[x-1][y] += 1
                    if (y>0 and data[x][y-1] != 0) : data[x][y-1] += 1
                    if ((x+1)<len_data and y>0 and data[x+1][y-1] != 0) : data[x+1][y-1] += 1
                    if (x>0 and (y+1)<len_data and data[x-1][y+1] != 0) : data[x-1][y+1] += 1
    if nb_flashes == len_data*len_data :
        print(i)
        not_flash = 0
