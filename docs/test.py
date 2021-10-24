# funkce operace
def scitani(c1, c2):
    r = c1 + c2
    print("result je " + str(r))


def odecitani(c1, c2):
    r = c1 - c2
    print("result je " + str(r))


def nasobeni(c1, c2):
    r = c1 * c2
    print("result je " + str(r))


def deleni(c1, c2):
    r = c1 / c2
    print("result je " + str(r))

# funkce vstup cisla


def vstupCisla():
    num = int(input("zadej cislo: "))
    print("zadal jsi cislo: " + str(num))
    return num


""""
# kontrola operace
def kontrolaOperace(oper):
        if oper == '+' or oper == '-' or oper == '*' or oper == '/':
            #vystup operace
            print("zadal jsi operace: " + oper)
        else:
            # vystup chyby
            oper = input("chyba pravopisu! zvol operace znovu: ")
"""


# spusk programu
print("vitam ti v kalkulacce!")

# start or q
start = input("zadej start aby spustit kalkulacku nebo q aby program skoncil ")

# prvni cislo
num1 = vstupCisla()

# operace
print("muzes zvolit operace: +, -, *, /")

# zadani operace
operation = input("napis operace, kterou chces pouzit: ")

# kontrola operace

if operation == "+":
    num2 = vstupCisla()
    res = num1 + num2

if operation == "-":
    num2 = vstupCisla()
    res = num1 - num2

if operation == "*":
    num2 = vstupCisla()
    res = num1 * num2

if operation == "/":
    num2 = vstupCisla()
    res = num1 / num2
else:
    print("chyba zadani operace")


# druhe cislo
#num2 = vstupCisla()


# vysledek
print("vysledek je")
print(res)
