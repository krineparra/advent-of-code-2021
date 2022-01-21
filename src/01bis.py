with open('01-data.txt') as file:
    data = file.readlines()
    data2=[]
    for i in range(3,len(data)):
        sum1 = int(data[i-3].rstrip('\n')) + int(data[i-2].rstrip('\n')) + int(data[i-1].rstrip('\n'))
        sum2 = int(data[i].rstrip('\n')) + int(data[i-2].rstrip('\n')) + int(data[i-1].rstrip('\n'))
        data2.append(sum2 > sum1)
    print(sum(data2))