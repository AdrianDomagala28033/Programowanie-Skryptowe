def Zaszyfrowanie(tekst, przesuniecie):

    for i in tekst:
        i += przesuniecie
        print(i)

tekst = input("Podaj tekst do zaszyfrowania: ")
przesuniecie = input("Podaj przesuniecie szyfru: ")
Zaszyfrowanie(tekst, przesuniecie)