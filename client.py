import requests
from bs4 import BeautifulSoup as bs
import clipboard
from pynput import keyboard

class StackPull:
    def __init__(self):
        pass

    def load(self, question_id):
        response = requests.get('https://api.stackexchange.com/2.2/questions/' + str(question_id) + '/answers?order=desc&sort=votes&site=stackoverflow&filter=withbody')
        if response.status_code == 200:
            self.answers = response.json()['items']
        elif response.status_code == 404:   
            print('Not found')
        else:
            print('Failure')
    
    def return_answer(self, index):
        answer = self.answers[index]
        answer_id = answer['answer_id']
        votes = answer['score']
        answer_body = answer['body']

        soup = bs(answer_body, features="html.parser")
        code = list()
        for i in soup.find_all('pre'):
            code = i.get_text()
            clipboard.copy(code)
        return answer_id, votes, answer_body, code

if __name__ == "__main__":
    s = StackPull()
    s.load(40636607)
    print(s.return_answer(0))
