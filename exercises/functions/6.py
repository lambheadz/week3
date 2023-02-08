'''s = input()
words = s.split()
res = []
for word in words:
    res.insert(0, word)

print(" ".join(res))
'''
def reverse(s):
    words = s.split()
    res = []
    for word in words:
        res.insert(0, word)
    print(" ".join(res))    

s = input()
reverse(s)    