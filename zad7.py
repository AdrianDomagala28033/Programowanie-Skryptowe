with open("oceny.txt", "a") as p1:
    tab = []
    for i in range(5):
        ocena = input("Podaj oceny: ")
        if(int(ocena) > 0 and int(ocena) < 7):
            tab.append(int(ocena))
    dict = {
        "imie": input("Podaj imie: "),
        "nazwisko": input("Podaj nazwisko: "),
        "oceny": tab
    }
    for i in dict:
        p1.write(str(dict[i]) + "\n")