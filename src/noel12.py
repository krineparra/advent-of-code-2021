with open('noel11data.txt') as file:
    data=list(map(int,(file.readlines())[0].split(',')))

fish = 9*[0]
for i in range(9):
    fish[i] = data.count(i)
print(fish)
timer = 256
for day in range(timer):
    fishtemp = 9*[0]
    fishtemp[8] = fish[0]
    fishtemp[6] = fish[0]
    for i in range(8):
        fishtemp[i] += fish[i+1]
    for i in range(9):
        fish[i] = fishtemp[i]
print(sum(fish))
