with open('07-data.txt') as file:
    data = list(map(int, file.readlines()[0].split(',')))
# print(data)
min = min(d for d in data)
max = max(d for d in data)
fuelmin = 0
for d in data:
    fuelmin += d * max
# print(fuelmin)
best_position = 0
for position in range(max):
    # print('-------------------------------')
    # print('position : ', position)
    # on calcule combien il faut de fuel pour que tous les crabes y aillent
    fuel = 0
    for i in range(len(data)):
        # print('de ', i, 'à', position, '=', data[i] * abs(position - i))
        fuel += abs(position - data[i])
    # si ce total est < à fuelmin, on garde en mémoire
    # print('fuel : ', fuel)
    if fuel < fuelmin:
        fuelmin = fuel
        best_position = position
print('best_position : ', best_position)
print('fuelmin : ', fuelmin)
