#Méthode iterative Dichotomie

def rech_dich_iter( Y, A ):
    a = 0
    b = len(A)-1
    m = (a+b)//2
    while a < b :
        if A[m] == Y :
            return m
        elif A[m] > Y :
            b = m-1
        else :
            a = m+1
        m = (a+b)//2
    return a
