import numpy
with open('07-data.txt') as file:
    data = list(map(int, file.readlines()[0].split(',')))
max = max(d for d in data)
fuelmin = 0
somme = sum(n for n in range(max-min(d for d in data)+1))
for d in data:
    fuelmin += d * somme
    for position in range(max):
    fuel = 0
    for i in range(len(data)):
        fuel += sum(n for n in range(abs(position - data[i])+1))
    fuelmin = min(fuelmin, fuel)
print('fuelmin : ', fuelmin)


