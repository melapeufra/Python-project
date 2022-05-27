#Un programme qui calcule le determinant d'une matrice carré par la méthode des cofacteurs sous python.

from copy import deepcopy

def sous_matrice(matrice_org, ligne, colonne):
    nouv_matrice = deepcopy(matrice_org)
    nouv_matrice.remove(matrice_org[ligne])
    for i in range(len(nouv_matrice)):
        nouv_matrice[i].remove(nouv_matrice[i][colonne])
        return nouv_matrice

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
        result = 0
    num_colonnes = num_lignes
    for j in range(num_colonnes):
        cofacteur = (-1) ** (0+j) * matrice[0][j] \
                   * determinant(sous_matrice(matrice, 0, j))
        result += cofacteur
        return result
