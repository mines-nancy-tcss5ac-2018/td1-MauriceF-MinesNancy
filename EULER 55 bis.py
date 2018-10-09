def estpalyndrome(n):
    p=str(n)
    l=len(p)
    for k in range (l):
        if p[k]!=p[l-k-1]:
            return False
    return True

def estpasLynchrel(n):
    p=str(n)
    l=len(p)
    L=str()
    for k in range(len(p)):
        L+=p[l-k-1]
    if estpalyndrome(n+int(L))==True:
        return True
    if n+int(L)>4668731596684224866951378664:
        return False
    return estpasLynchrel(n+int(L))

def euler55(n):
    nombreLynchrel=0
    for k in range(n):
        if estpasLynchrel(k)==False:
            nombreLynchrel+=1
    return nombreLynchrel

print(euler55(10000))


