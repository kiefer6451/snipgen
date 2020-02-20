from stackpull import StackPull
from scraper import Scraper
from getch import _Getch
import os
import colorama
from colorama import Fore, Style

def printSpacer(qIndex, title, aIndex):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("------------------------------------------------------------------------------------------")
    print(Fore.CYAN + Style.BRIGHT + "Question #{} \nQuestion Title: {} \nAnswer #{}".format(qIndex, title, aIndex))
    print(Style.RESET_ALL)

if __name__ == "__main__":
    stack_pull = StackPull()
    scraper = Scraper()
    query = input('Enter your search: ')
    question_ids = scraper.scrape(query)
    stack_pull.load(question_ids)
    qIndex = 0
    aIndex = 0
    printSpacer(qIndex, "Food", aIndex)
    print(stack_pull.return_answer(qIndex, aIndex)[2])
    while True:
        getch = _Getch()
        key_code = ord(getch())
        if key_code == 106: 
            if aIndex < len(stack_pull.answers[qIndex]) - 1: #j
                aIndex += 1
                printSpacer(qIndex, "foo", aIndex)
                print(stack_pull.return_answer(qIndex, aIndex)[2])
            else:
                print("Already at last answer for this question.")
        elif key_code == 107:
            if aIndex > 0: #k
                aIndex -= 1
                printSpacer(qIndex, "foo", aIndex)
                print(stack_pull.return_answer(qIndex, aIndex)[2])
            else:
                print("Already at first answer for this question.")
        elif key_code == 104:
            if qIndex > 0: #h
                qIndex -= 1
                aIndex = 0
                printSpacer(qIndex, "foo", aIndex)
                print(stack_pull.return_answer(qIndex, aIndex)[2])
            else:
                print("Already at first question.")
        elif key_code == 108:
            if (qIndex < len(stack_pull.answers)-1): #l
                qIndex += 1
                aIndex = 0
                printSpacer(qIndex, "foo", aIndex)
                print(stack_pull.return_answer(qIndex, aIndex)[2])
            else:
                print("Already at last question.")
        elif key_code == 113: #q
            break
