with open('noel15data.txt') as file:
    data = [d[61:-1].split(' ') for d in file.readlines()]
print(data)
result = 0
for d in data :
    datatemp = list(map(lambda x : len(x) in (2,3,4,7), d))
    result += sum(datatemp)
print(result)

