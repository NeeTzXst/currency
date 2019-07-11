print("currency converter test")
print("press 00 for change THB to some currency \npress 99 for change EUR to some current")
choice = int(input("enter number you press : "))
result = float()
if choice == 00:
    print("PRESS 1 to change THB to EUR\nPRESS 2 to change THB to USB\nPRESS 3 to change THB to GBP")
    print("PRESS 4 to change THB to VND\nPRESS 5 to change THB to BND\nPRESS 6 to change THB to KHR")
    print("PRESS 7 to change THB to IDR\nPRESS 8 to change THB to LAK\nPRESS 9 to change THB to MYR")
    print("PRESS 10 to change THB to MMK\nPRESS 11 to change THB to PHP\nPRESS 12 to change THB to SGD")
    currency = int(input("ENTER number : "))
    num1 = float(input("THB : "))
    if currency==1:
        result = num1*0.0290
        print('%.2f' %result+" EUR")
    elif currency==2:
        result = num1*0.0325
        print('%.2f'%result+" USB")
    elif currency==3:
        result = num1*0.0261
        print('%.2f'%result+" GBP")
    elif currency==4:
        result = num1*753.65
        print('%.2f'%result+" VND")
    elif currency==5:
        result = num1*0.0442
        print('%.2f'%result+" BND")
    elif currency==6:
        result = num1*131.8080
        print('%.2f'%result+" KHR")
    elif currency==7:
        result = num1*458.4550
        print('%.2f'%result+" IDR")
    elif currency==8:
        result = num1*282.6000
        print('%.2f'%result+" LAK")
    elif currency==9:
        result = num1*0.1344
        print('%.2f'%result+" MYR")
    elif currency==10:
        result = num1*48.9127
        print('%.2f'%result+" MMK")
    elif currency==11:
        result = num1*1.6676
        print('%.2f'%result+" PHP")
    elif currency==12:
        result = num1*0.0442
        print('%.2f'%result+" SGD")
    else:
        print("ERROR")
else:
    print("ERROR")
    
if choice == 99:
    print("PRESS 1 to change EUR to EUR\nPRESS 2 to change EUR to USB\nPRESS 3 to change EUR to GBP")
    print("PRESS 4 to change EUR to VND\nPRESS 5 to change EUR to BND\nPRESS 6 to change EUR to KHR")
    print("PRESS 7 to change EUR to IDR\nPRESS 8 to change EUR to LAK\nPRESS 9 to change EUR to MYR")
    print("PRESS 10 to change EUR to MMK\nPRESS 11 to change EUR to PHP\nPRESS 12 to change EUR to SGD")
    currency = int(input("ENTER number : "))
    num1 = float(input("EUR : "))
    if currency==1:
        result = num1*34.5066
        print('%.2f' %result+" THB")
    elif currency==2:
        result = num1*1.1256
        print('%.2f'%result+" USB")
    elif currency==3:
        result = num1*0.8972
        print('%.2f'%result+" GBP")
    elif currency==4:
        result = num1*26085.2312
        print('%.2f'%result+" VND")
    elif currency==5:
        result = num1*1.5266
        print('%.2f'%result+" BND")
    elif currency==6:
        result = num1*4581.7460
        print('%.2f'%result+" KHR")
    elif currency==7:
        result = num1*15823.9476
        print('%.2f'%result+" IDR")
    elif currency==8:
        result = num1*9799.8620
        print('%.2f'%result+" LAK")
    elif currency==9:
        result = num1*4.6308
        print('%.2f'%result+" MYR")
    elif currency==10:
        result = num1*1699.4410
        print('%.2f'%result+" MMK")
    elif currency==11:
        result = num1*57.5470
        print('%.2f'%result+" PHP")
    elif currency==12:
        result = num1*1.5262
        print('%.2f'%result+" SGD")
    else:
        print("ERROR")
else:
    print("ERROR")