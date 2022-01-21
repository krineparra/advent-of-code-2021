with open('06-data.txt') as file:
    fish=list(map(int,(file.readlines())[0].split(',')))
timer = 80
for day in range(timer):
    for i in range(len(fish)):
        if fish[i] == 0:
            fish.append(8)
            fish[i] = 6
        else:
            fish[i] -= 1
print(len(fish))