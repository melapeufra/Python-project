#Recherche séquentielle(exhaustive)

def recherche (N, K):
    trouve = -1
    i=0
    n=len(N) 
    while (i < n and trouve == -1) :
        if N[i] == Y :
            trouve = i
        else 
            i = i + 1
    return (trouve) 
