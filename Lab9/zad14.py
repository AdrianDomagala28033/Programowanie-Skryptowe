import os, random

def getRandomAnswers(answers):
    answer = answers[random.randint(0, len(answers))]
    return answer
def playGame(answers):
    checkLocation()
    print("Witaj w twojej własnej magicznej kuli, zadaj mi pytanie a ja postaram ci się na nie odpowiedzieć")
    pytanie = input()
    while pytanie != "":
        odpowiedz = getRandomAnswers(answers)
        print(odpowiedz)
        saveQuestionAndAnswer(pytanie, odpowiedz)
        print("Zadaj kolejne pytanie! Jeśli chcesz przerwać naciśnij ENTER")
        pytanie = input()
def checkLocation():
    if not os.path.exists(os.path.join(os.getcwd(), "QA")):
        os.mkdir("QA")
        print("Tworzę lokalizacje do zapisywania odpowiedzi")
def loadAnswers(path=None):
    answers = []
    if path != None:
        if os.path.exists(path):
            with open(path, "r") as rAnswer:
                for r in rAnswer.readlines():
                    answers.append(r)
    return answers
def saveQuestionAndAnswer(question, answer):
    with open(os.path.join("QA", "qa.txt"), "a+") as wAnswer:
        wAnswer.write(f"{question} : {answer}\n")
answers = []
answers = loadAnswers("answers.txt")
playGame(answers)