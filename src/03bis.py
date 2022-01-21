# https://adventofcode.com/2021/day/3#part2
# oxygen_generator_rating = 0

with open('03-data.txt') as file:
    data = list(map(lambda x: x.rstrip('\n'), file.readlines()))
    for i in range(len(data[0])):
        print('-----------------------')
        nb_bin = len(data)
        print('nb_bin = ', nb_bin)

        print('car numero', i)

        nb_1 = sum(int(num[i]) for num in data)
        print('nb de 1 = ', nb_1)
        # caractère le moins représenté :
        bin_moins_represente = str(int(nb_bin - nb_1 > nb_1))
        print('bin_moins_represente = ',bin_moins_represente)
        data2 = []
        for d in data:
            if d[i] != bin_moins_represente:
                # oxygen_generator_rating : on le garde
                data2.append(d)
        data = data2
oxygen_generator_rating = int(data[0],2)
print(oxygen_generator_rating)
