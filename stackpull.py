import requests
from bs4 import BeautifulSoup as bs
import colorama
from colorama import Fore, Style

class StackPull:
    def __init__(self):
        pass

    def load(self, question_ids):
        self.answers = list()
        for question_id in question_ids[:(min(3, len(question_ids)))]:
            #print("STACK DEBUG: {}".format(question_id))
            #print('https://api.stackexchange.com/2.2/questions/' + str(question_id) + '/answers?order=desc&sort=votes&site=stackoverflow&filter=!-*jbN.OXKfDP')
            response = requests.get('https://api.stackexchange.com/2.2/questions/' + str(question_id) + '/answers?order=desc&sort=votes&site=stackoverflow&filter=!-*jbN.OXKfDP')
            if response.status_code == 200:
                self.answers.append(response.json()['items'])
            elif response.status_code == 404:   
                print('Not found')
            else:
                print('Failure')
        if len(self.answers) == 0:
            return False
        else:
            return True
    
    def return_answer(self, qIndex, aIndex):
        answer = self.answers[qIndex][aIndex]
        answer_id = answer['answer_id']
        votes = answer['score']
        answer_body = answer['body']
        title = answer['title']
        #print(answer_body)
        soup = bs(answer_body, features="html.parser")
        allCode = ''
        codeList = list()
        ans = list()

        for line in soup.find_all(True): 
            if line.name == 'pre': #pre code, don't want this, just want the code
                pass
            elif line.name == 'code':
                allCode += "\n"
                allCode += line.get_text()
                codeList.append(line.get_text())
                ans.append(["code", line.get_text()])
                check = True
            elif line.name == 'p' or line.name == 'li': #actual writing/text that we want
                ans.append(["text", line.get_text()])
        
        return title, allCode, codeList, ans

if __name__ == "__main__":
    s = StackPull()
    res = s.load([40636607, 40636607])
    print(s.return_answer(1, 1))
