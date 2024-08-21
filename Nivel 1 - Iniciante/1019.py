sec = int(input())
h = sec/3600
m = sec % 3600 / 60
s = sec % 3600 % 60
h = str("%d"%h)
m = str("%d"%m)
s = str("%d"%s)

print(h+":"+m+":"+s)