with open('05-data.txt') as file:
    data = [i[:-1] if i[-1] == '\n' else i for i in file.readlines()]
    zones_temp = [d.split(' -> ') for d in data]
    zones = [[list(map(int, zone[0].split(','))), list(map(int, zone[1].split(',')))] for zone in zones_temp]
    carte = [[0 for i in range(1000)] for j in range(1000)]
    for d in zones:
        if d[0][0] == d[1][0]:
            for i in range(min(d[0][1], d[1][1]), max(d[0][1], d[1][1]) + 1):
                carte[i][d[0][0]] += 1
        elif d[0][1] == d[1][1]:
            for i in range(min(d[0][0], d[1][0]), max(d[0][0], d[1][0]) + 1):
                carte[d[0][1]][i] += 1
        else:
            y1 = d[0][1]
            y2 = d[1][1]
            x1 = d[0][0]
            x2 = d[1][0]
            for i in range(max(y1,y2)-min(y1,y2)+1):
                if (x1 < x2 and y1 < y2) or (x1 > x2 and y1 > y2):
                    carte[min(y1,y2)+i][min(x1,x2)+i] += 1
                else:
                    carte[min(y1,y2)+i][max(x1,x2)-i] += 1
    result = 0
    for ligne in carte:
        for colonne in ligne:
            result += (colonne >= 2)
    print(result)