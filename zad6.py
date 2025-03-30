fileName = input("Podaj nazwę pliku: ")
try:
    with open(fileName, "r+") as p1:
        print(f"Udało się otworzyć plik {fileName}")
except FileNotFoundError as ef:
    print(ef)
finally:
    print("To sie wykona zawsze")