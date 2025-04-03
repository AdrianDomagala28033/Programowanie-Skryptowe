import csv

print("Książka telefoniczna")
print("Wybierz co chcesz zrobić w swojej własnej książce telefonicznej: \n1 - Dodaj nowy kontakt, \n2 - Wyświetl wszystkie kontakty, \n3 - usuń użytkownika \n")

plik = "ksiazka.csv"
ksiazka = dict()

def wczytajKontakty():
    try:
        with open(plik, newline='', encoding='UTF-8') as p1:
            reader = csv.reader(p1)
            for i in reader:
                if(len(i) == 2):
                    ksiazka[i[0]] = i[1]
    except FileNotFoundError:
        pass

def zapiszKontakty():
    with open(plik, newline='', encoding='UTF-8') as p1:
        writer = csv.writer()
        for key, value in ksiazka.items():
            writer.writerow([key, value])

wczytajKontakty()

while True:
    tryb = input("Podaj numer: ")
    if(int(tryb) == 1):
        imie = input("Podaj imie: ")
        numer = input("Podaj numer telefonu: ")
        ksiazka.update({
            imie : numer
            })
        zapiszKontakty()
    elif(int(tryb) == 2):
        for key, value in ksiazka.items():
            print(f"Imię: {key}, Numer: {value}")
    elif(int(tryb) == 3):
        imie = input("Podaj imię do usunięcia: ")
        if imie in ksiazka:
            del ksiazka[imie]
            print(f"Kontakt {imie} usunięty.")
            zapiszKontakty()
        else:
            print("Kontakt nie istnieje.")
    else:
        break