n = int(input())
countin = 0
countout = 0
for i in range(n):
    x = int(input())
    if  x >=10 and x <= 20:
        countin += 1
    else :
        countout +=1

print(countin, "in")
print(countout, "out")