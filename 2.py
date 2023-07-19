with open('17-2.txt') as f:
    a = [int(x) for x in f]
k = 0
mina = 10**10
for i in range(0, len(a)-1):
    if (a[i]%5 == 0 or a[i+1]%5 == 0) and a[i]+a[i+1]>500:
        k+=1
        mina = min(mina, a[i]+a[i+1])
print(k, mina)