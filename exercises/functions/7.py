def has_33(num):
    for i  in range(0, len(num) - 1):
        if num[i:i+2] == [3,3]:
            return True
    return False

n = int(input())
l = []
for i in range(0, n):
    e = int(input())        
    l.append(e)
print(has_33(l))    