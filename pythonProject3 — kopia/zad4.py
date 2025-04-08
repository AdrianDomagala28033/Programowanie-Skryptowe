def Zaszyfrowanie(tekst, przesuniecie):
    nowyTekst = ""
    for i in tekst:
        nowyTekst += chr(ord(i)+int(przesuniecie))
    print(nowyTekst)

tekst = input("Podaj tekst do zaszyfrowania: ")
przesuniecie = input("Podaj przesuniecie szyfru: ")
Zaszyfrowanie(tekst, przesuniecie)