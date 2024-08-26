testes = int(input())


for i in range (testes):
    x, y, z = input().split()

    xf = float(x)
    yf = float(y)
    zf = float(z)

    mediap = ((xf * 2) + (yf * 3) + (zf * 5)) / 10
   
    print(f'{mediap:.1f}')
