import requests
from bs4 import BeautifulSoup as bs
import clipboard

import colorama
from colorama import Fore, Style

class StackPull:
    def __init__(self):
        pass

    def load(self, question_ids):
        self.answers = list()
        for question_id in question_ids[:3]:
            response = requests.get('https://api.stackexchange.com/2.2/questions/' + str(question_id) + '/answers?order=desc&sort=votes&site=stackoverflow&filter=!-*jbN.OXKfDP')
            if response.status_code == 200:
                self.answers.append(response.json()['items'])
            elif response.status_code == 404:   
                print('Not found')
            else:
                print('Failure')
    
    def return_answer(self, qIndex, aIndex):
        answer = self.answers[qIndex][aIndex]
        answer_id = answer['answer_id']
        votes = answer['score']
        answer_body = answer['body']
        title = answer['title']
        print(answer_body)
        soup = bs(answer_body, features="html.parser")
        output = ''
        code = ''

        for line in soup.find_all(True): 
            print("TEST: {}".format(line))
            if line.name == 'pre':
                pass
            elif line.name == 'code':
                print("pre: {}".format(line))
                output += "\n"
                code += "\n"
                code += line.get_text()
                output += Fore.YELLOW + Style.BRIGHT + line.get_text() + Style.RESET_ALL
                output += "\n"
                check = True
            elif line.name == 'p' or line.name == 'li':
                output += Fore.WHITE + Style.BRIGHT + line.get_text() + Style.RESET_ALL
        
        clipboard.copy(code)
        return [title, output]        

if __name__ == "__main__":
    s = StackPull()
    res = s.load([40636607, 40636607])
    print(s.return_answer(1, 1))
