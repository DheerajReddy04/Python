#WAP to find the best arrangemnt where the added stciks gives the least sum
'''
n = int(input())
temp = n
if(temp%2 == 1):
    print("Enter even number")
    exit(1)
thislist = []
for i in range(n):
    a = input()
    thislist.append(a)
thislist.sort()
print(thislist)
i = 0
sum = 0
while(i < n/2):
    sum += int(thislist[i])
    i += 1
print(sum)
'''

n = int(input("Enter number of sticks:"))
thislist = []
for i in range(n):
    a = input()
    thislist.append(a)
temp1 = temp2 = None
flag = 0
thislist.sort()
for i in range(n-1):
    if(thislist[i] == thislist[i+1]):
        temp2 = temp1
        temp1 = thislist[i]
        flag += 1
        i+=1
        if(i == n-1):
            break
if(flag < 2):
    print("-1")
else:
    print(int(temp1)*int(temp2))
