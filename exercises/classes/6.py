n = int(input())
l = []
for i in range(0, n):
    e = int(input())
    l.append(e)
res = list(filter(lambda x : (x % i != 0), l))
print(res)