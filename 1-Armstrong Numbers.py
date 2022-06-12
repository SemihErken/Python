
number = int(input("Please Enter a Number :"))

counter = 0

liste = []

section = number
while(1):
    section = int(section/10)
    counter += 1
    if section == 0:
        break
i = 1

bolum = number
while(i <= counter):
    liste.append(bolum % 10)
    bolum = int(number/(10**i))
    i += 1

toplam = 0

for a in liste:
    toplam = toplam + a**counter

if (toplam == number):
    print("Thats a Fucking Armstrong Number")
else:
    print("Thats Not a Fucking Armstrong Number")
