from random import randint

oyin = [

    ['_','_','_'],

    ['_','_','_'],

    ['_','_','_'],

]


for qator in oyin:
    for ustun in qator:
        print(ustun.center(10,' '), end='')
    print("\n")

oyinchi = input("Qaysi belgini tanlaysiz: x/0: ")
if oyinchi=="X":
    komp="0"
elif oyinchi=="0":
    komp="X"

bosh_joy = 9
while bosh_joy>0:
    if oyinchi==komp:
        while True:
            qator = randint(0,3)
            ustun = randint(0,3)
            if oyin[qator-1][ustun-1] == '_':
                oyin[qator-1][ustun-1] = oyinchi
                bosh_joy-=1
                for qator in oyin:
                    for ustun in qator:
                        print(ustun.center(10,' '), end='')
                    print("\n")
                break

    else:
        qator = int(input(f"{oyinchi} uchun qator: "))
        ustun = int(input(f"{oyinchi} uchun ustun: "))

        if oyin[qator-1][ustun-1] == '_':
            oyin[qator-1][ustun-1] = oyinchi
            bosh_joy-=1
        else:
            print("Bu joy band!")
            continue


    if oyin[0][0]=='X' and oyin[0][1]=='X' and oyin[0][2]=='X':
        print("X yutti")
        break
    elif oyin[1][0]=='X' and oyin[1][1]=='X' and oyin[1][2]=='X':
        print("X yutti")
        break
    elif oyin[2][0]=='X' and oyin[2][1]=='X' and oyin[2][2]=='X':
        print("X yutti")
        break
    elif oyin[0][0]=='X' and oyin[1][0]=='X' and oyin[2][0]=='X':
        print("X yutti")
        break
    elif oyin[0][1]=='X' and oyin[1][1]=='X' and oyin[2][1]=='X':
        print("X yutti")
        break
    elif oyin[0][2]=='X' and oyin[1][2]=='X' and oyin[2][2]=='X':
        print("X yutti")
        break
    elif oyin[0][0]=='X' and oyin[1][1]=='X' and oyin[2][2]=='X':
        print("X yutti")
        break
    elif oyin[0][2]=='X' and oyin[1][1]=='X' and oyin[2][0]=='X':
        print("X yutti")
        break


    elif oyin[0][0]=='0' and oyin[0][1]=='0' and oyin[0][2]=='0':
        print("0 yutti")
        break
    elif oyin[1][0]=='0' and oyin[1][1]=='0' and oyin[1][2]=='0':
        print("0 yutti")
        break
    elif oyin[2][0]=='0' and oyin[2][1]=='0' and oyin[2][2]=='0':
        print("0 yutti")
        break
    elif oyin[0][0]=='0' and oyin[1][0]=='0' and oyin[2][0]=='0':
        print("0 yutti")
        break
    elif oyin[0][1]=='0' and oyin[1][1]=='0' and oyin[2][1]=='0':
        print("0 yutti")
        break
    elif oyin[0][2]=='0' and oyin[1][2]=='0' and oyin[2][2]=='0':
        print("0 yutti")
        break
    elif oyin[0][0]=='0' and oyin[1][1]=='0' and oyin[2][2]=='0':
        print("0 yutti")
        break
    elif oyin[0][2]=='0' and oyin[1][1]=='0' and oyin[2][0]=='0':
        print("0 yutti")
        break
    else:
        if bosh_joy==0:
            print("Durrang !")
            break

    
    if oyinchi=='X':
        oyinchi='0'
    else:
        oyinchi='X'
