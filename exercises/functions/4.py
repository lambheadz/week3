mylist = []
n = int(input())
for i in range(0, n):
    e = int(input())
    mylist.append(e)

def prime(num):
    flag = True
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                flag = False
    if flag == True:
        print(num)            

output_list = list(map(prime, mylist))