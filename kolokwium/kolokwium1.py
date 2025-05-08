ksiazka1 = {"ID" : 0, "autorzy" : ["Adrian Domagala"], "gatunki" : ["fantazy"], "strony" : 435}
ksiazka2 = {"ID" : 1, "autorzy" : ["Jan Nowak", "Piotr Kowalczyk"], "gatunki" : ["fantazy, akcji"], "strony" : 697}
ksiazka3 = {"ID" : 2, "autorzy" : ["Szymon Karaś", "Władysław Szpak"], "gatunki" : ["dramat, komedia, romans"], "strony" : 1024}
ksiazki = [ksiazka1, ksiazka2, ksiazka3]
def najwiecejAutorow(ksiazki):
    maxAutorow = 0
    autorzy = []
    lKsiazek = []
    for i in ksiazki:
        if(maxAutorow <= len(i.get("autorzy"))):
            maxAutorow = len(i.get("autorzy"))
            autorzy = i.get("autorzy")
    for i in ksiazki:
        if(len(i.get("autorzy")) == maxAutorow):
            lKsiazek.append(i)
    print(f"Oto lista książek z największą ilością autorów:")
    for i in lKsiazek:
        print(i)
najwiecejAutorow(ksiazki)

def znajdzGatunki(gatunek):
    listaKsiazek = []
    for i in ksiazki:
        for j in i.get("gatunki"):
            index = j.find(gatunek)
            if(index != -1):
                listaKsiazek.append(i)
    print(f"Oto książki należące do gatunku {gatunek}")
    for i in listaKsiazek:
        print(i)
znajdzGatunki("fantazy")