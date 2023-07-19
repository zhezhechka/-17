with open('17-3.txt') as f:
    a = [int(x) for x in f]
k = 0
n = 0
for i in range(0, len(a)-1):
    for j in range(i+1, len(a)):
        if ((a[i]%10 == 0 and a[j]%10 != 0) or (a[j]%10 == 0 and a[i]%10 != 0)) and a[i]//100 == a[j]//100:
            k+=1
            n = max(n, a[i]//100)
print(k, n)
            