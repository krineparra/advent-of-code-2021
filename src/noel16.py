import re

with open('noel15data.txt') as file:
    data1 = [d[61:-1].split(' ') for d in file.readlines()]
with open('noel15data.txt') as file:
    data2 = [d[:58].split(' ') for d in file.readlines()]
score = 0
for i in range(len(data2)):

    # on cherche les chiffres
    str_d1d2 = ''.join(sorted(list(filter(lambda x: len(x) == 2, data2[i]))[0]))
    str1 = str_d1d2
    # print(str_d1d2)
    # print(str1)

    str7 = ''.join(sorted(list(filter(lambda x: len(x) == 3, data2[i]))[0]))
    str_h = (re.search("[^" + str1 + "]", str7)).group()
    # print(str7)
    # print(str_h)

    str4 = ''.join(sorted(list(filter(lambda x: len(x) == 4, data2[i]))[0]))
    str_temp = (re.search("([^" + str1 + "])", str4)).group()
    str_g1m = str_temp + (re.search("([^" + str1 + str_temp + "])", str4)).group()
    # print(str4)
    # print(str_g1m)

    str8 = ''.join(sorted(list(filter(lambda x: len(x) == 7, data2[i]))[0]))
    str_temp = (re.search("([^" + str1 + str7 + str4 + "])", str8)).group()
    str_g2b = str_temp + (re.search("([^" + str1 + str7 + str4 + str_temp + "])", str8)).group()
    # print(str8)
    # print(str_g2b)

    str0 = ''.join(sorted(list(filter(
        lambda x: len(x) == 6 and str_h in x and str_d1d2[0] in x and str_d1d2[1] in x and str_g2b[0] in x and str_g2b[
            1] in x, data2[i]))[0]))
    str_g1 = (re.search("([^" + str_g2b + str_h + str_d1d2 + "])", str0)).group()
    str_m = (re.search("([^" + str_g1 + "])", str_g1m)).group()
    # print(str0)
    # print(str_g1)
    # print(str_m)

    str9 = ''.join(sorted(list(filter(
        lambda x: len(x) == 6 and str_h in x and str_d1d2[0] in x and str_d1d2[1] in x and str_g1m[0] in x and str_g1m[
            1] in x, data2[i]))[0]))
    str_b = (re.search("([^" + str_g1m + str_h + str_d1d2 + "])", str9)).group()
    str_g2 = (re.search("([^" + str_b + "])", str_g2b)).group()

    str6 = ''.join(sorted(list(filter(
        lambda x: len(x) == 6 and str_h in x and str_g2b[0] in x and str_g2b[1] in x and str_g1m[0] in x and str_g1m[
            1] in x, data2[i]))[0]))
    str_d2 = (re.search("([^" + str_g2b + str_h + str_g1m + "])", str6)).group()
    str_d1 = (re.search("([^" + str_d2 + "])", str_d1d2)).group()

    str5 = ''.join(sorted(list(
        filter(lambda x: len(x) == 5 and str_h in x and str_m in x and str_b in x and str_g1 in x and str_d2 in x,
               data2[i]))[0]))
    str2 = ''.join(sorted(list(
        filter(lambda x: len(x) == 5 and str_h in x and str_d1 in x and str_m in x and str_g2 in x and str_b in x,
               data2[i]))[0]))
    str3 = ''.join(sorted(list(
        filter(lambda x: len(x) == 5 and str_h in x and str_d1 in x and str_d2 in x and str_m in x and str_b in x,
               data2[i]))[0]))

    # on décode
    dico = {str0: 0, str1: 1, str2: 2, str3: 3, str4: 4, str5: 5, str6: 6, str7: 7, str8: 8, str9: 9}
    result = ''
    # print('------------------------')
    # print(dico)
    # print(data1[i])
    for d in data1[i]:
        # print(''.join(sorted(d)))
        # print(str(dico[''.join(sorted(d))]))
        result += str(dico[''.join(sorted(d))])
    score += int(result)
print(score)
