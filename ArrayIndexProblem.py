ip = eval(input())
n = len(ip)
o = []
e = []
for i in range(n):
    if i%2 == 0:
        e.append(ip[i])
    else:
        o.append(ip[i])
so = o.sort(reverse = True)
se = e.sort()
for i in range(n):
    if i%2 == 0:
        x = se.pop(0)
        ip.append(x)
    else:
        x = so.pop(0)
        ip.append(x)
print(ip)