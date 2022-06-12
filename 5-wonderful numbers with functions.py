all = [*range(1,1001) ]

def control (i):

    little = [*range(1,i)]

    divisorSum = 0

    a = 1

    for a in little:
        if(i % a == 0):
            divisorSum = divisorSum + a

    if(divisorSum == i):
        return True

for i in all:
    if(control(i) == True):
        print(i)
