#Méthode recursive Dichotomie

def rech_dicho_rec(Y, A, a = 0, b = -1 ):
    if a == b : 
        return a
    if b == -1 : 
        b = len(A)-1
    m = (a+b)//2
    if A[m] == Y :
        return m
    elif A[m] > Y :
        return rech_dicho_rec(Y, A, a, m-1)
    else :
        return rech_dicho_rec(Y, A, a, m+1, b)
