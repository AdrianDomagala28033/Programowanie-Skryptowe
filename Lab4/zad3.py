text = input("Podaj tekst do dopisania: ")
with open("tekst.txt", "a") as p1:
    p1.write(text)