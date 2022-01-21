from pprint import pprint

with open('noel07data.txt') as file:
    data_temp = list(filter(lambda x: x != '\n', file.readlines()))
    data = [i[:-1] if i[-1] == '\n' else i for i in data_temp]
    # CONSTRUCTION DONNEES
    # numéros gagnants : 1ere ligne
    num_winers = list(map(int, (data.pop(0)).split(',')))
    print(num_winers)
    # grilles : lignes suivantes. 25 numéros par grille
    num_ligne_grille = 0
    grilles = []
    sous_grille = []
    # print(data)
    for i in range(0, len(data)):
        # 1 elmt = 1 ligne = 5 numéros. 5 elmts = 5 lignes = 1 grilles
        ligne = list(filter(lambda x: x != '', data[i].split(' ')))
        # print(ligne)
        for num in ligne:
            sous_grille.append([int(num), 0])
            if num_ligne_grille < 24:
                num_ligne_grille += 1
            elif num_ligne_grille == 24:
                grilles.append(sous_grille)
                # print(sous_grille)
                sous_grille = []
                num_ligne_grille = 0
    print(grilles)

    # C'EST PARTI POUR LE BINGO
    stop = False
    # on tire un numéro
    for n in num_winers:
        # on regarde s'il est dans chaque grille
        for grille in grilles:
            if not stop:
                for num_grille in grille:
                    if num_grille[0] == n:
                        num_grille[1] = 1
                #on teste si une ligne est ok
                for i in range(5):
                    if not stop:
                        somme_ligne = sum(grille[5*i+j][1] for j in range(5))
                        if somme_ligne == 5:
                            winner = grille
                            stop = True
                        #on teste si une colonne est ok
                        else:
                            somme_colonne = sum(grille[i+5*j][1] for j in range(5))
                            if somme_colonne == 5:
                                winner = grille
                                stop = True
                        if stop:
                            score = n * sum(d[0] for d in winner if d[1]==0)
                            print('Gagné!', score, winner)
