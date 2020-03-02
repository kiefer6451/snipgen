from stackpull import StackPull
from scraper import Scraper
from getch import _Getch
import os
import colorama
from colorama import Fore, Style
import clipboard
from selenium import webdriver

def printSpacer(qIndex, title, aIndex):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("------------------------------------------------------------------------------------------")
    print(Fore.CYAN + Style.BRIGHT + "Question #{} \nQuestion Title: {} \nAnswer #{}".format(qIndex, title, aIndex))
    print(Style.RESET_ALL)

def display(stack_pull, qIndex, aIndex, snippet):
    title, allCode, codeList, ans = stack_pull.return_answer(qIndex, aIndex)
    printSpacer(qIndex, title, aIndex)
    
    #print out answer, highlighting only code that is selected
    cnt = 0
    for line in ans:
        if line[0] == 'code':
            if snippet == -1 or (snippet%len(codeList) == cnt):
                print(Fore.YELLOW + Style.BRIGHT + line[1] + Style.RESET_ALL)
            else:
                print(line[1]) #non clipboarded code
            cnt += 1
        else: #it's text
            print(line[1])
    
    #set snippet in clipboard
    if len(codeList) > 0:
        if snippet == -1:
            clipboard.copy(allCode) #copy all code to clipboard
        else:
            clipboard.copy(codeList[snippet%len(codeList)])


if __name__ == "__main__":
    stack_pull = StackPull()
    scraper = Scraper()
    scraper.setup() #opens selenium
   
    begin = True #auto run 'n' if we are just starting up
    snippet = -1
    while True: #mainprogram
        if begin == False:
            getch = _Getch() #key next keystroke
            key_code = ord(getch())
        else: key_code = 0
        
        if ((key_code == 110) or (begin == True)): #n, next query
            if begin == True: begin = False
            
            aIndex = 0
            qIndex = 0
            snippet = -1
            query = input('Enter your search: ')
            question_ids = scraper.scrape(query)
            ret = stack_pull.load(question_ids)

            if ret == False:
                print(Fore.RED + Style.BRIGHT + "No answers found.")
                print(Style.RESET_ALL)
                begin = True
            else: #ret is true, we successfully loaded some answers
                display(stack_pull, qIndex, aIndex, snippet)

        elif key_code == 106:  #j, next answer within question
            if aIndex < len(stack_pull.answers[qIndex]) - 1:
                snippet = -1
                aIndex += 1
                display(stack_pull, qIndex, aIndex, snippet)
            else:
                print("Already at last answer for this question.")
        elif key_code == 107: #k, previous answer within question
            if aIndex > 0: 
                snippet = -1
                aIndex -= 1
                display(stack_pull, qIndex, aIndex, snippet)
            else:
                print("Already at first answer for this question.")
        elif key_code == 104: #h, previous question
            if qIndex > 0: 
                snippet = -1
                qIndex -= 1
                aIndex = 0
                display(stack_pull, qIndex, aIndex, snippet)
            else:
                print("Already at first question.")
        elif key_code == 108: #l, next question
            if (qIndex < len(stack_pull.answers)-1): 
                snippet = -1
                qIndex += 1
                aIndex = 0
                display(stack_pull, qIndex, aIndex, snippet)
            else:
                print("Already at last question.")
        elif key_code == 119: #if w, scroll through code snippet
            snippet += 1
            display(stack_pull, qIndex, aIndex, snippet)
        elif key_code == 113: #q, for quit
            scraper.die()
            break
