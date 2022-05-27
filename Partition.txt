#Méthode récursive partition

def p(n,m):
     if n == m:
        return 1 + p(n, m - 1)
    if m == 0 or n < 0:
        return None
    if n == 0 or m == 1:
        return 1
     else
    return p(n, m - 1) + p(n - m, m)
