import time
start_time = time.time()

def stairs(n):
    #check if n > 0
    if n < 1:
        return 0
    return 1 + stairs(n-1) + stairs(n-2) + stairs (n-3)

climbedCount = {}

def stairsDyn(n):
    if n < 1:
        return 0
    #check if we've calculated this number before
    elif n in climbedCount:
        return climbedCount[n]
    climbedCount[n] = 1 + stairsDyn(n-1) + stairsDyn(n-2) + stairsDyn(n-3)
    return climbedCount[n]


def main ():
    x = 0
    while(x != -1):
        x = input('Enter a number of stairs')
        print("Non DP way: " + str(stairs(int(x))) + "TIME: " + str(time.time() - start_time))
        old_timey = time.time() - start_time
        print("DP way: " + str(stairsDyn(int(x)))  + "TIME: " + str(time.time() - start_time))
        new_timey = time.time() - start_time
        print ("speedup of DP over non-DP: " + str(old_timey/new_timey)) 
         
if __name__ == '__main__':
    main()
