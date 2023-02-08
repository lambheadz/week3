def solve(numheads, numlegs):
    err_msg = "no solution"
    cntc = 0
    cntr = 0

    if (numheads >= numlegs):
        print(err_msg)
    elif (numlegs % 2 != 0):
        print(err_msg)
    else:
        cntr = (numlegs - 2 * numheads) / 2
        cntc = numheads - cntr
        print(int(cntc), int(cntr))        

'''
heads = int(input())
legs = int(input())
solve(heads, legs)
'''
solve(35, 94)       