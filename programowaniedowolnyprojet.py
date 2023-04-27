import random
import time
print("Nieprawidłowa długość liczb, spróbuj ponownie.")
while True:
    nrdlugosc = input("Podaj długość liczb do wyświetlenia (od 1 do 10): ")
    try:
        nrdlugosc = int(nrdlugosc)
        if nrdlugosc < 1 or nrdlugosc > 10:
            raise x
        break
    except x:
        print("Nieprawidłowa długość liczb, spróbuj ponownie.")

while True:
    czaswyswietlania = input("Podaj czas wyświetlania liczb (w sekundach): ")
    try:
        czaswyswietlania = int(czaswyswietlania)
        if czaswyswietlania < 1:
            raise x
        break
    except x:
        print("Nieprawidłowy czas wyświetlania, spróbuj ponownie.")

nrwys = 1

wyswietlanenr = []

for i in range(nrwys):
    number = ''.join(str(random.randint(0, 9)) for _ in range(nrdlugosc))
    wyswietlanenr.append(number)

for number in wyswietlanenr:
    print(number, end=' \n')
    time.sleep(1)
bb=0
for i in range(czaswyswietlania):
    print(" \n")
    print("-")
    time. sleep(1)
for i in range(100):
    print("-")
odp = 0


for i in range(nrwys):
    pdj = input("Podaj " + str(i + 1) + ". liczbę: ")
    if pdj == wyswietlanenr[i]:
        odp += 1


print("Poprawne odpowiedzi: " + str(odp) + " na " + str(nrwys) + " próbe.")
