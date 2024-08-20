id, quantidade = map(int, input().split())
if id==1:
    v = 4.0
elif id==2:
    v = 4.5
elif id==3:
    v = 5.0
elif id==4:
    v = 2.0
elif id==5:
    v= 1.5
x= v*quantidade
print("TOTAL: R$", "%.2f"%x)