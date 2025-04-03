import random
def CzyWygrales(gracz, krupier):
    if(gracz > krupier and gracz < 22):
        print("GRATULACJE!!! WYGRAŁEŚ!!!")
    elif(krupier > 21):
        print("GRATULACJE!!! WYGRAŁEŚ!!!")
    elif(gracz > 21 or gracz == krupier):
        print("Przykro mi przegrałeś")
    else:
        print("Przykro mi przegrałeś")

print("Witaj w kasyno online, rozpoacznijmy gre w kasyno")
input("Naciśnij enter aby rozpocząć")
gracz = 0
krupier = 0
kartyGracza = []
talia = {
    'As Pik': 11, '2 Pik': 2, '3 Pik': 3, '4 Pik': 4, '5 Pik': 5, '6 Pik': 6, '7 Pik': 7, '8 Pik': 8, '9 Pik': 9, '10 Pik': 10, 'Walet Pik': 10, 'Dama Pik': 10, 'Król Pik': 10,
    'As Karo': 11, '2 Karo': 2, '3 Karo': 3, '4 Karo': 4, '5 Karo': 5, '6 Karo': 6, '7 Karo': 7, '8 Karo': 8, '9 Karo': 9, '10 Karo': 10, 'Walet Karo': 10, 'Dama Karo': 10, 'Król Karo': 10,
    'As Trefl': 11, '2 Trefl': 2, '3 Trefl': 3, '4 Trefl': 4, '5 Trefl': 5, '6 Trefl': 6, '7 Trefl': 7, '8 Trefl': 8, '9 Trefl': 9, '10 Trefl': 10, 'Walet Trefl': 10, 'Dama Trefl': 10, 'Król Trefl': 10,
    'As Kier': 11, '2 Kier': 2, '3 Kier': 3, '4 Kier': 4, '5 Kier': 5, '6 Kier': 6, '7 Kier': 7, '8 Kier': 8, '9 Kier': 9, '10 Kier': 10, 'Walet Kier': 10, 'Dama Kier': 10, 'Król Kier': 10
}

wylosowana_karta = random.choice(list(talia.items()))
karta, wartosc = wylosowana_karta
wartoscKart = 0
wartoscKrupiera = 0
while(wartoscKart < 22):
    czyGra = input("Czy chcesz grać dalej? Wpisz tak/nie: ")
    if(wartoscKrupiera <= 17):
        wylosowana_krupiera = random.choice(list(talia.items()))
        kartaKrupiera, wartoscK = wylosowana_krupiera
        wartoscKrupiera += wartoscK
    if(wartoscKart < 22 and wartoscKrupiera < 22):
        if(czyGra.lower() == "tak"):
            wylosowana_karta = random.choice(list(talia.items()))
            karta, wartosc = wylosowana_karta
            wartoscKart += wartosc
            del talia[karta]
            print(f"Twoja karta to: {karta}, a jej wartość to {wartosc}. Wszystkie twoje wylosowane kart karty mają wartość {wartoscKart}")
            print(f"Krupier wylosował kartę: {kartaKrupiera}, jej wartość to {wartoscK}, a jego całkowity wynik to {wartoscKrupiera}")
        elif(czyGra.lower() == "nie"):
            CzyWygrales(wartoscKart, wartoscKrupiera)
            print(f"Wartość twoich kart to {wartoscKart}, a karty krupiera to: {wartoscKrupiera}")
            if(wartoscKrupiera < wartoscKart):
                wylosowana_krupiera = random.choice(list(talia.items()))
                kartaKrupiera, wartoscK = wylosowana_krupiera
                wartoscKrupiera += wartoscK
            break
    else:
        CzyWygrales(wartoscKart, wartoscKrupiera)
        print(f"Wartość twoich kart to {wartoscKart}, a karty krupiera to: {wartoscKrupiera}")
        break



