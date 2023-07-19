with open('17-1.txt') as f:
    a = [int(x) for x in f]
k = 0
maxa = 0
for i in range(0, len(a)):
    if a[i]%10 == 9 and a[i]>150:
        k+=1
        maxa = max(maxa, a[i])
print(k, maxa)
        