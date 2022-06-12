x = int(input("Enter a Number Please"))
digits = []
counter = 1
z = x
while(1):
    z = z / 10
    z = int(z)
    if(z == 0):
        break
    counter += 1

digits.append(x % 10)
x = x / 10
x = int(x)
digits.append(x % 10)


print(digits)

if(digits[1] == 1):
    print("on")
elif(digits[1] == 2):
    print("yirmi")
elif(digits[1] == 3):
    print("otuz")
elif(digits[1] == 4):
    print("kırk")
elif (digits[1] == 5):
    print("elli")
elif(digits[1] == 6):
    print("altmış")
elif(digits[1] == 7):
    print("yetmiş")
elif(digits[1] == 8):
    print("seksen")
elif(digits[1] == 9):
    print("doksan")

if(digits[0] == 1):
    print("bir")
elif(digits[0] == 2):
    print("iki")
elif(digits[0] == 3):
    print("üç")
elif(digits[0] == 4):
    print("dört")
elif(digits[0] == 5):
    print("beş")
elif(digits[0] == 6):
    print("altı")
elif(digits[0] == 7):
    print("yedi")
elif(digits[0] == 8):
    print("sekiz")
elif(digits[0] == 9):
    print("dokuz")