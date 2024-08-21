vp = 0
vi = 0
vpos = 0
vneg = 0
for i in range (5):
    x = int(input())

    if (x%2==0):
        vp += 1
    elif (x%2!=0):
        vi += 1
    if (x>0):
        vpos += 1
    elif (x<0):
        vneg += 1
print(vp, "valor(es) par(es)")
print(vi, "valor(es) impar(es)")
print(vpos, "valor(es) positivo(s)")
print(vneg, "valor(es) negativo(s)")