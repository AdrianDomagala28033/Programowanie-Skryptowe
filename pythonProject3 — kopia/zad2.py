znaj = 5
tydz = 1
while(znaj <= 150):
    if(znaj * 2 > 150):
        break
    else:
        znaj -= 1
        znaj *= 2
        tydz += 1
print(f"Do osiągnięcia liczby Dunbara minęło {tydz} tygodni")