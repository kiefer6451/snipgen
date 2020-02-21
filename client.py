from stackpull import StackPull
from scraper import Scraper
from getch import _Getch
import os
import colorama
from colorama import Fore, Style

from selenium import webdriver
browser = webdriver.Firefox()

def printSpacer(qIndex, title, aIndex):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("------------------------------------------------------------------------------------------")
    print(Fore.CYAN + Style.BRIGHT + "Question #{} \nQuestion Title: {} \nAnswer #{}".format(qIndex, title, aIndex))
    print(Style.RESET_ALL)

if __name__ == "__main__":
    stack_pull = StackPull()
    scraper = Scraper()
    query = input('Enter your search: ')
    try:
        question_ids = scraper.scrape(query)
        stack_pull.load(question_ids)
        qIndex = 0
        aIndex = 0
        resp = stack_pull.return_answer(qIndex, aIndex)
        printSpacer(qIndex, resp[0], aIndex)
        print(resp[1])
        while True:
            getch = _Getch()
            key_code = ord(getch())
            if key_code == 106: 
                if aIndex < len(stack_pull.answers[qIndex]) - 1: #j
                    response = stack_pull.return_answer(qIndex, aIndex)
                    aIndex += 1
                    printSpacer(qIndex, response[0], aIndex)
                    print(response[1])
                else:
                    print("Already at last answer for this question.")
            elif key_code == 107: #k
                if aIndex > 0: 
                    response = stack_pull.return_answer(qIndex, aIndex)
                    aIndex -= 1
                    printSpacer(qIndex, response[0], aIndex)
                    print(response[1])
                else:
                    print("Already at first answer for this question.")
            elif key_code == 104: #h
                if qIndex > 0: 
                    response = stack_pull.return_answer(qIndex, aIndex)
                    qIndex -= 1
                    aIndex = 0
                    printSpacer(qIndex, response[0], aIndex)
                    print(response[1])
                else:
                    print("Already at first question.")
            elif key_code == 108: #l
                if (qIndex < len(stack_pull.answers)-1): 
                    response = stack_pull.return_answer(qIndex, aIndex)
                    qIndex += 1
                    aIndex = 0
                    printSpacer(qIndex, response[0], aIndex)
                    print(response[1])
                else:
                    print("Already at last question.")
            elif key_code == 119: #w
                query = input('Enter your search: ')
                question_ids = scraper.scrape(query)
                stack_pull.load(question_ids)
                printSpacer(qIndex, "Food", aIndex)
                print(stack_pull.return_answer(qIndex, aIndex))
            elif key_code == 113: #q
                break
    except:
        print('Max requests exceeded')