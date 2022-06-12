first = int(input("Please Enter The First Number"))

second = int(input("Please Enter The Second Number"))

if(second < first):
    high = first
elif(first < second):
    high = second
elif(first == second):
    high = first


while(True):
    if(high % first == 0 and high % second == 0):
        print("Least Common Floor is {}".format(high))
        break
    high += 1
