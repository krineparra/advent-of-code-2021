with open('noel22data.txt') as file:
    data = [line.split('-') for line in [d[:-1] for d in file.readlines()]]
    data = data + [d[::-1] for d in data if 'start' not in d and 'end' not in d and d[0].isupper()]
print(data)
print('--------------------')
data_mid = [d for d in data if 'start' not in d]
data_start = [d for d in data if 'start' in d]
way = []
ways = []
depart = []

def end_way(data_mid):
    end_point = way[-1]
    data_temp = data_mid.copy()
    data_mid = [d for d in data_mid if end_point in d]
    print('***DEBUT FONCTION - points possibles pour le chemin ', way, ' :' , data_mid)
    trouve = 0
    for d in data_mid :
        if way[-1] in d :
            print('chemin', way, 'point', d)
            print('')
            new_point = d[0] if d[0] != end_point else d[1]
            if new_point == 'end':
                print('STEP1 - prochaine étape pour ', way, ':', new_point)
                chemin_final = way.copy()
                chemin_final.append('end')
                ways.append(chemin_final)
                print('-----------fin du voyage :', ways[-1], '------------')
                trouve = 0
            elif new_point.isupper():
                print('STEP2 - prochaine étape pour ', way, ':', new_point)
                way.append(new_point)
                data_temp.remove(d)
                end_way(data_temp)
                trouve = 1
            elif new_point not in way:
                print('STEP3 - prochaine étape pour ', way, ':', new_point)
                way.append(new_point)
                data_temp.remove(d)
                end_way(data_temp)
                trouve = 1
    if trouve == 0:
        way.pop()
        print('suppression')
    print('***sortie de fonction. Chemin = ', way)
    return

for d in data_start:
    print('nouveau départ : ', d)
    print('-----------------------')
    end = d[0] if d[0] != 'start' else d[1]
    depart = end
    way = ['start', end]
    end_way(data_mid)


print(ways)
