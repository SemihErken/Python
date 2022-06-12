
number = int(input("Please Enter a Number:"))

range(1,number)

liste = []

for i in range(1,number):
    if (number % i == 0):
        liste.append(i)

print("{}'s divisors are = {}".format(number,liste))

sum = 0

for x in liste:
    sum = sum + x

if sum == number:
    print("Thats a Fucking Wonderful Number")
else :
    print("Thats Not a Fucking Wonderful Number")

