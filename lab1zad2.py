# zad2
print("----------ZADANIE 2----------")
x = input("Podaj imię: ")
print("Cześć " + x + "!")

# zad3
print("----------ZADANIE 3----------")
x = input("Podaj liczbe pierwsza: ")
y = input("Podaj liczbe druga: ")
print("Suma: ", float(x) + float(y))

# zad4
print("----------ZADANIE 4----------")
s = []
for i in range(8, 81, 1):
    s.append(i)
print(sum(s))

# zad5
print("----------ZADANIE 5----------")
from datetime import date

today = date.today()
data = date(1997, 5, 6)
d = today - data
print(d)

# zad6
print("----------ZADANIE 6----------")
print("---KALKULATOR---")


def dod(x, y):
    return x + y


def od(x, y):
    return x - y


def mn(x, y):
    return x * y


def dz(x, y):
    return x / y


def po(x, y):
    return pow(x, y)


print("MENU")
print("1.Dodawanie")
print("2.Odejmowanie")
print("3.Mnożenie")
print("4.Dzielenie")
print("5.Potęgowanie")

w = input("Wybierz operacje: ")

n1 = int(input("Podaj pierwszą liczbę: "))
n2 = int(input("Podaj drugą liczbę "))

if w == '1':
    print(n1, "+", n2, "=", dod(n1, n2))

elif w == '2':
    print(n1, "-", n2, "=", od(n1, n2))

elif w == '3':
    print(n1, "*", n2, "=", mn(n1, n2))

elif w == '4':
    print(n1, "/", n2, "=", dz(n1, n2))

elif w == '5':
    print(n1, "^", n2, "=", po(n1, n2))
else:
    print("Zły wybór")
