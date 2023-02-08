def spy_game(num):
    for i in range(0, len(num)):
        if num[i] == 0:
            for x in range(i + 1, len(num)):
                if num[x] == 0:
                    for y in range(i + 2, len(num)):
                        if num[y] == 7:
                            return True
                else:
                    return False        
                
l = []
n = int(input())
for i in range(0, n):
    e = int(input())
    l.append(e)

print(spy_game(l))    