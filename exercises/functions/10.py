def uni_l(l):
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    return x 

n = int(input())
l = []
for i in range(0, n):
    e = int(input())
    l.append(e)       
print(uni_l(l))    