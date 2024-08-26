v = int(input())

count = 0
for i in range (1,v+1):
    count += 1
    quadrado = count ** 2
    if quadrado % 2 == 0:
        print(f'{count}^2 = {quadrado}')