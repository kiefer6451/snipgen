from stackpull import StackPull
from scraper import Scraper
from getch import _Getch
import os
import colorama
from colorama import Fore, Style

from selenium import webdriver
#browser = webdriver.Firefox() #caused bug where multple selenium windows were opening. Was this for Windows or something... idk why this was here... no Windows machine to test it

def printSpacer(qIndex, title, aIndex):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("------------------------------------------------------------------------------------------")
    print(Fore.CYAN + Style.BRIGHT + "Question #{} \nQuestion Title: {} \nAnswer #{}".format(qIndex, title, aIndex))
    print(Style.RESET_ALL)

if __name__ == "__main__":
    stack_pull = StackPull()
    scraper = Scraper()
    scraper.setup() #opens selenium
   
    begin = True #auto run 'n' if we are just starting up
    while True: #mainprogram
        if begin == False:
            getch = _Getch() #key next keystroke
            key_code = ord(getch())
        else: key_code = 0
        
        if ((key_code == 110) or (begin == True)): #n, next query
            if begin == True: begin = False
            
            aIndex = 0
            qIndex = 0
            query = input('Enter your search: ')
            question_ids = scraper.scrape(query)
            ret = stack_pull.load(question_ids)

            if ret == False:
                print(Fore.RED + Style.BRIGHT + "No answers found.")
                print(Style.RESET_ALL)
                begin = True
            else: #ret is true, we successfully loaded some answers
                resp = stack_pull.return_answer(qIndex, aIndex)
                printSpacer(qIndex, resp[0], aIndex)
                print(resp[1])

        elif key_code == 106:  #j, next answer within question
            if aIndex < len(stack_pull.answers[qIndex]) - 1:
                aIndex += 1
                response = stack_pull.return_answer(qIndex, aIndex)
                printSpacer(qIndex, response[0], aIndex)
                print(response[1])
            else:
                print("Already at last answer for this question.")
        elif key_code == 107: #k, previous answer within question
            if aIndex > 0: 
                aIndex -= 1
                response = stack_pull.return_answer(qIndex, aIndex)
                printSpacer(qIndex, response[0], aIndex)
                print(response[1])
            else:
                print("Already at first answer for this question.")
        elif key_code == 104: #h, previous question
            if qIndex > 0: 
                qIndex -= 1
                aIndex = 0
                response = stack_pull.return_answer(qIndex, aIndex)
                printSpacer(qIndex, response[0], aIndex)
                print(response[1])
            else:
                print("Already at first question.")
        elif key_code == 108: #l, next question
            if (qIndex < len(stack_pull.answers)-1): 
                qIndex += 1
                aIndex = 0
                response = stack_pull.return_answer(qIndex, aIndex)
                printSpacer(qIndex, response[0], aIndex)
                print(response[1])
            else:
                print("Already at last question.")
        elif key_code == 119: #if w, scroll through code snippet
            pass
        elif key_code == 113: #q
            scraper.die()
            break
    #except Exception as e:
    #    print('Max requests exceeded')
    #    print(e)
