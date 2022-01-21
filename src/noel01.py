with open('noel01data.txt') as file:
    data = file.readlines()
    data2=[]
    for i in range(1,len(data)):
        data2.append(int(data[i].rstrip('\n'))>int(data[i-1].rstrip('\n')))
    print(sum(data2))