#Un programme qui calcule le determinant d'une matrice carré par la méthode de Gauss sous python.

def determinant(matrice):
    num_lignes = len(matrice)
    for ligne in matrice:
        if len(ligne) != num_lignes:
            print("la matrice n'est pas carre ")
            return None
        if len(matrice) == 2:
            determinant_simple = matrice[0][0] * \
                                 matrice[1][1] - \
                                 matrice[1][0] * \
                                 matrice[0][1]
            return determinant_simple

    else:


    for i in range(num_lignes-1):

        for j in range(i+1, num_lignes):

        for k in range(num_lignes):
                 matrice[j][k] = matrice[j][k] *\
                                 matrice[i][i] - \
                                 matrice[i][k] * \
                                 matrice[j][i]
                 return matrice[j][k]
                 det=1
                 for i in range(num_lignes)
                 det=matrice[i][i]*det
             return det
