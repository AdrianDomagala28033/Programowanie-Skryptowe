from operator import index

print("Tabela 5 najlepszych wyników gry")
print(" 1 - dodaj nowy wynik \n 2 - usuń wynik \n 3 - posortuj wynik \n 4 - wyświetl wyniki \n 5 - zakończ")
wyniki = []
while True:
    menu = int(input("Wybierz co chcesz zrobić: "))
    if(menu == 1):
        wynik = int(input("Podaj swój wynik: "))
        a = 0
        for i in range(5):
            if (len(wyniki) < 5):
                wyniki.append(wynik)
                break
            elif (wynik >= wyniki[i]):
                wyniki.insert(a, wynik)
                wyniki.pop(len(wyniki) - 1)
                break
            a += 1
    elif(menu == 2):
        wyniki.pop(int(input("wybierz który numer chcesz usunąć: "))-1)
    elif(menu == 3):
        wyniki.sort(reverse=True)
    elif(menu == 4):
        for i in wyniki:
            print(i)
    elif(menu == 5):
        break

