
first = int(input("Please Enter The First Number"))

second = int(input("Please Enter The Second Number"))

def finder(x , y):
    if(x < y):
        little = x
    elif(y < x):
        little = y
    else:
        print(x)
        return

    roster = [*range(1,little+1)]

    divisors = []
    for a in roster:
        if(x % a == 0 and y % a == 0):
            divisors.append(a)

    divisors.sort(reverse = True)
    print(divisors[0])

finder(first,second)