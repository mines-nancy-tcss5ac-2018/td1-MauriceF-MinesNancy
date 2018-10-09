def euler16(n):
    nombre=2**n
    n=str(nombre)
    s=0
    for k in range (len(n)):
        s+=int(n[k])
    return s

print (euler16(1000))


def euler16correction(n):
    
    s=0
    while n%10!=0:
        s+=n%10
        n=n//10
    return s

print (euler16correction(2**1000))

### le programme euleur corrigé au tableau ne renvoie pas le bon résultat, a moins que j'ai mal recopié ###    