semih = 1
while(semih == 1):
    try:
        secenek = int(input("Enter 3 For Triangle , 4 for Rectangle :"))
    except ValueError:
        print("Please Enter Number , Not Letter or Symbol or String")
        continue
    if(secenek != 3 and secenek != 4):
        print("Please Enter 3 or 4")
        continue
    semih = 0

class çokgen():

    def __init__(self,açı = "0" ,kenar1 = "0" ,kenar2 = "0" ,kenar3 ="0" ,kenar4 ="0"):
        self.açı = açı
        self.kenar1 = kenar1
        self.kenar2 = kenar2
        self.kenar3 = kenar3
        self.kenar4 = kenar4

    def açı_girişi(self ,x):
        self.açı = x

    def kenar_girişi1(self ,y):
        self.kenar1 = y

    def kenar_girişi2(self ,z):
        self.kenar2 = z

    def kenar_girişi3(self ,t):
        self.kenar3 = t

    def kenar_girişi4(self ,a):
        self.kenar4 = a


toplam = 0


üçgen = çokgen()

dörtgen = çokgen()

if (secenek == 3):

    kontrol = 1
    while (kontrol == 1):
        try:
            karar = int(input("Enter 1 For Angle , 2 For Edge : "))
        except ValueError:
            print("Please Enter Number , Not Letter or Symbol or String")
            continue
        if (karar != 1 and karar != 2):
            print("Please Enter 1 or 2")
            continue
        kontrol = 0

    if(karar == 1):

        while (True):
            flag = 0
            toplam = 0
            try:
                üçgen.açı_girişi(float(input(" Enter the 1'st Angle :")))
                if(üçgen.açı <= 0 or üçgen.açı >= 180):
                    print("Entered Angle Value Can Not Equal to 0 or Higher Than 180 degrees")
                    flag = 1


            except ValueError:
                print("Please Enter Number , Not Letter or Symbol or String")
                flag = 1

            if (flag == 1):
                continue

            toplam = toplam + üçgen.açı

#**************************************************************************


            try:
                üçgen.açı_girişi(float(input(" Enter the 2'nd Angle :")))
                if(üçgen.açı <= 0 or üçgen.açı >= 180):
                    print("Entered Angle Value Can Not Equal to 0 or Higher Than 180 degrees")
                    flag = 1
            except ValueError:
                print("Please Enter Number , Not Letter or Symbol or String")
                flag = 1

            if (flag == 1):
                continue

            toplam = toplam + üçgen.açı


#***********************************************************************************
            try:
                üçgen.açı_girişi(float(input(" Enter the 3'rd Angle :")))
                if(üçgen.açı <= 0 or üçgen.açı >= 180):
                    print("Entered Angle Value Can Not Equal to 0 or Higher Than 180 degrees")
                    flag = 1
            except ValueError:
                print("Please Enter Number , Not Letter or Symbol or String")
                flag = 1

            if (flag == 1):
                continue

            elif (flag == 0):

                toplam = toplam + üçgen.açı

                if(toplam == 180):
                    print("There  Can Be a Triangle With Angles You Have Entered")
                elif(toplam != 180):
                    print("There  Can Not Be a Triangle With Angles You Have Entered")

                break

    elif(karar == 2):

        while (True):
            flag = 0
            toplam = 0
            try:
                üçgen.kenar_girişi1(float(input(" Enter the 1'st Angle :")))
                if (üçgen.kenar1 <= 0):
                    print("Entered Edge Value Can Not Equal to 0 or Less Than 0")
                    flag = 1


            except ValueError:
                print("Please Enter Number , Not Letter or Symbol or String")
                flag = 1

            if (flag == 1):
                continue

#***************************************************************************************

            try:
                üçgen.kenar_girişi2(float(input(" Enter the 2'nd Angle :")))
                if (üçgen.kenar2 <= 0):
                    print("Entered Edge Value Can Not Equal to 0 or Less Than 0")
                    flag = 1
            except ValueError:
                print("Please Enter Number , Not Letter or Symbol or String")
                flag = 1

            if (flag == 1):
                continue

#****************************************************************************************
            try:
                üçgen.kenar_girişi3(float(input(" Enter the 3'rd Angle :")))
                if (üçgen.kenar3 <= 0):
                    print("Entered Edge Value Can Not Equal to 0 or Less Than 0")
                    flag = 1
            except ValueError:
                print("Please Enter Number , Not Letter or Symbol or String")
                flag = 1

            if (flag == 1):
                continue

            elif (flag == 0):

                if (üçgen.kenar1 + üçgen.kenar2 > üçgen.kenar3 and üçgen.kenar2 + üçgen.kenar3 > üçgen.kenar1 and üçgen.kenar1 + üçgen.kenar3 > üçgen.kenar2):
                    print("There  Can Be a Triangle With Edge Values You Have Entered")
                else:
                    print("There  Can Not Be a Triangle With Edge Values You Have Entered")

                break


#***********************************************************************************
#               RECTANGLES                                                         *
#                                                                                  *
#***********************************************************************************
if (secenek == 4):

    kontrol = 1
    while (kontrol == 1):
        try:
            karar = int(input("Enter 1 For Angle , 2 For Edge : "))
        except ValueError:
            print("Please Enter Number , Not Letter or Symbol or String")
            continue
        if (karar != 1 and karar != 2):
            print("Please Enter 1 or 2")
            continue
        kontrol = 0

    if(karar == 1):


        while (True):
            flag = 0
            toplam = 0
            try:
                dörtgen.açı_girişi(float(input(" Enter the 1'st Angle :")))
                if(dörtgen.açı <= 0 or dörtgen.açı >= 180):
                    print("Entered Angle Value Can Not Equal to 0 or Higher Than 180 degrees")
                    flag = 1
            except ValueError:
                print("Please Enter Number , Not Letter or Symbol or String")
                flag = 1

            if (flag == 1):
                continue

            toplam = toplam + dörtgen.açı


#***********************************************************************************************
            try:
                dörtgen.açı_girişi(float(input(" Enter the 2'nd Angle :")))
                if(dörtgen.açı <= 0 or dörtgen.açı >= 180):
                    print("Entered Angle Value Can Not Equal to 0 or Higher Than 180 degrees")
                    flag = 1
            except ValueError:
                print("Please Enter Number , Not Letter or Symbol or String")
                flag = 1

            if (flag == 1):
                continue

            toplam = toplam + dörtgen.açı


#***********************************************************************************************
            try:
                dörtgen.açı_girişi(float(input(" Enter the 3'rd Angle :")))
                if(dörtgen.açı <= 0 or dörtgen.açı >= 180):
                    print("Entered Angle Value Can Not Equal to 0 or Higher Than 180 degrees")
                    flag = 1
            except ValueError:
                print("Please Enter Number , Not Letter or Symbol or String")
                flag = 1

            if (flag == 1):
                continue

            toplam = toplam + dörtgen.açı


#***********************************************************************************************
            try:
                dörtgen.açı_girişi(float(input(" Enter the 4'th Angle :")))
                if(dörtgen.açı <= 0 or dörtgen.açı >= 180):
                    print("Entered Angle Value Can Not Equal to 0 or Higher Than 180 degrees")
                    flag = 1
            except ValueError:
                print("Please Enter Number , Not Letter or Symbol or String")
                flag = 1

            if (flag == 1):
                continue

            elif (flag == 0):
                toplam = toplam + dörtgen.açı

                if(toplam == 360):
                    print("There  Can Be a Rectangle With Angles You Have Entered")
                elif(toplam != 360):
                    print("There  Can Not Be a Triangle With Angles You Have Entered")

                break
#**********************************************************************************************

    if(karar == 2):

        while (True):
            flag = 0
            toplam = 0
            try:
                dörtgen.kenar_girişi1(float(input(" Enter the 1'st Edge :")))
                if (dörtgen.kenar1 <= 0):
                    print("Entered Edge Value Can Not Equal to 0 or Less Than 0")
                    flag = 1


            except ValueError:
                print("Please Enter Number , Not Letter or Symbol or String")
                flag = 1

            if (flag == 1):
                continue

#***************************************************************************************

            try:
                dörtgen.kenar_girişi2(float(input(" Enter the 2'nd Edge :")))
                if (dörtgen.kenar2 <= 0):
                    print("Entered Edge Value Can Not Equal to 0 or Less Than 0")
                    flag = 1
            except ValueError:
                print("Please Enter Number , Not Letter or Symbol or String")
                flag = 1

            if (flag == 1):
                continue

#****************************************************************************************

            try:
                dörtgen.kenar_girişi3(float(input(" Enter the 3'rd Edge :")))
                if (dörtgen.kenar3 <= 0):
                    print("Entered Edge Value Can Not Equal to 0 or Less Than 0")
                    flag = 1
            except ValueError:
                print("Please Enter Number , Not Letter or Symbol or String")
                flag = 1

            if (flag == 1):
                continue

#*******************************************************************************************
            try:
                dörtgen.kenar_girişi4(float(input(" Enter the 4'th Edge :")))
                if (dörtgen.kenar4 <= 0):
                    print("Entered Edge Value Can Not Equal to 0 or Less Than 0")
                    flag = 1
            except ValueError:
                print("Please Enter Number , Not Letter or Symbol or String")
                flag = 1

            if (flag == 1):
                continue

            elif (flag == 0):

                if(dörtgen.kenar1 + dörtgen.kenar2 + dörtgen.kenar3 < dörtgen.kenar4 or dörtgen.kenar1 + dörtgen.kenar2 + dörtgen.kenar4 < dörtgen.kenar3 or dörtgen.kenar1 + dörtgen.kenar3 + dörtgen.kenar4 < dörtgen.kenar2 or dörtgen.kenar2 + dörtgen.kenar3 + dörtgen.kenar4 < dörtgen.kenar1):
                    print("There  Can Not Be a Rectangle With Edge Values You Have Entered")

                else :
                    print(" There  Can Be a Rectangle With Edge Values You Have Entered")

                break


















