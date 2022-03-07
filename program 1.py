def vizual(nr1,nr2,nr3):
    print(nr1[0]," | ",nr1[1]," | ",nr1[2])
    print("---+-----+----")
    print(nr2[0], " | ", nr2[1], " | ", nr2[2])
    print("---+-----+----")
    print(nr3[0], " | ", nr3[1], " | ", nr3[2])

def start_joc():
    inceput = 0
    while inceput not in ["Y", "N"]:
        inceput = input("Salut, vrei sa incepi jocul? (Y/N) ")
        if inceput == "Y":
            print("Sa inceapa jocul")
        if inceput == "N":
            return False

def verificare(nr1,nr2,nr3):
    if (nr1[0] == "X" and nr1[1] == "X" and nr1[2] == "X") or (nr2[0] == "X" and nr2[1] == "X" and nr2[2] == "X") or (nr3[0] == "X" and nr3[1] == "X" and nr3[2] == "X") or (nr1[0] == "X" and nr2[1] == "X" and nr3[2] == "X") or (nr3[0] == "X" and nr2[1] == "X" and nr1[2] == "X"):
        return True
    elif (nr1[0] == "O" and nr1[1] == "O" and nr1[2] == "O") or (nr2[0] == "O" and nr2[1] == "O" and nr2[2] == "O") or (nr3[0] == "O" and nr3[1] == "O" and nr3[2] == "O") or (nr1[0] == "O" and nr2[1] == "O" and nr3[2] == "O") or (nr3[0] == "O" and nr2[1] == "O" and nr1[2] == "O"):
        return True
    else:
        return False

def verirficare_supra(nr1,nr2,nr3,x):
    while x not in range(1, 10):
        x = int(input("P1: alege o valoare intre 1-9: "))
    nota = False
    while nota != True:
        if x in [1,2,3]:
            if nr1[x-1] == "X" or nr1[x-1] == "O":
                x = int(input("P1: alege o alta varianta intre 1-9 care nu e luata: "))
            else:
                nota = True
        if x in [4,5,6]:
            if nr2[x-4] == "X" or nr2[x-4] == "O":
                x = int(input("P1: alege o alta varianta intre 1-9 care nu e luata: "))
            else:
                nota = True
        if x in [7,8,9]:
            if nr3[x-7] == "X" or nr3[x-7] == "O":
                x = int(input("P1: alege o alta varianta intre 1-9 care nu e luata: "))
            else:
                nota = True
    return x

def egalitate(nr1,nr2,nr3):
    for i in range(0,3):
        if nr1[i] == " ":
            a = False
        elif nr2[i] == " ":
            a = False
        elif nr3[i] == " ":
            a = False
        else:
            a = True
    return a




def joc():
    nr1 = [" "," "," "]
    nr2 = [" "," "," "]
    nr3 = [" "," "," "]
    castigator = False
    egal = False
    if start_joc() == False:
        print("Jocul s-a inchis")
        return 0
    vizual(nr1,nr2,nr3)
    while castigator != True:
        a = int(input("P1: alege o valoare intre 1-9: "))
        a = verirficare_supra(nr1, nr2, nr3, a)
        if a in [1,2,3]:
            nr1[a-1] = "X"
            print('\n' * 100)
            vizual(nr1,nr2,nr3)
        if a in [4,5,6]:
            nr2[a-4] = "X"
            print('\n' * 100)
            vizual(nr1,nr2,nr3)
        if a in [7,8,9]:
            nr3[a-7] = "X"
            print('\n' * 100)
            vizual(nr1,nr2,nr3)
        if verificare(nr1,nr2,nr3):
            castigator = True
            print("P1 a castigat")
            break
        egal = egalitate(nr1,nr2,nr3)
        if egal == True:
            print("Egalitate")
            break
        b = int(input("P2: alege o valoare intre 1-9: "))
        b = verirficare_supra(nr1,nr2,nr3,b)
        if b in [1, 2, 3]:
            nr1[b - 1] = "O"
            print('\n' * 100)
            vizual(nr1, nr2, nr3)
        if b in [4, 5, 6]:
            nr2[b - 4] = "O"
            print('\n' * 100)
            vizual(nr1, nr2, nr3)
        if b in [7, 8, 9]:
            nr3[b - 7] = "O"
            print('\n' * 100)
            vizual(nr1, nr2, nr3)
        if verificare(nr1,nr2,nr3):
            castigator = True
            print("P2 a castigat")
            break

joc()