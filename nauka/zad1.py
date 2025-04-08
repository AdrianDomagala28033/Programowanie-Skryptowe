def middleOfTheText(text):
    wordList = []
    signList = []
    text += ' '
    for i in text:
        if (i == ' '):
            if (len(wordList) % 2 == 0 and len(text) > 2):
                signList.append(wordList[int(len(wordList) / 2 - 1)])
            elif(len(wordList) % 2 != 0 and len(text) > 2):
                signList.append(wordList[int(len(wordList) / 2)])
            else:
                print("Tekst ma mniej niz 2 litery")
            wordList = []
        else:
            wordList.append(i)
    print(signList)


text = input("Podaj tekst: ")
middleOfTheText(text)