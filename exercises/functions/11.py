def isPol(s):
    return s == s[::-1]

s = input()
answer = isPol(s)

if answer:
    print("YES")
else:
    print("NO")    