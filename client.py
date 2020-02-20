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
question_id = 1720421 # from cayden
 
response = requests.get('https://api.stackexchange.com/2.2/questions/' + str(question_id) + '/answers?order=desc&sort=votes&site=stackoverflow&filter=withbody')

answers = None
index = 0

def display_answer(answer):
    answer_id = answer['answer_id']
    votes = answer['score']
    answer_body = answer['body']

    print('Answer ID: ' + str(answer_id))
    print('Votes: ' + str(votes))

    soup = bs(answer_body)

    print('Code:')
    print('-----------------------------------------------------------------------')
    for i in soup.find_all('pre'):
        code = i.get_text()
        clipboard.copy(code)
        print(code)
    print('-----------------------------------------------------------------------')

if response.status_code == 200:
    answers = response.json()['items']
    display_answer(answers[0])        
elif response.status_code == 404:   
    print('Not found')
else:
    print('Failure')

while True:
    command = input("Command: ")
    if command == 'j' and index < len(answers) -1:
        index += 1
        display_answer(answers[index])
    elif command == 'k' and index > 0:
        index -= 1
        display_answer(answers[index])
    elif command == 'q':
        break


# listener = keyboard.Listener(on_press=on_press)
# listener.start()  # start to listen on a separate thread
# listener.join()  # remove if main thread is polling self.keys    

# def on_press(key):
#     if key == keyboard.Key.esc:
#         return False  # stop listener
#     try:
#         k = key.char  # single-char keys
#     except:
#         k = key.name  # other keys
#     if k in ['j', 'k']:  # keys of interest
#         print('Key pressed: ' + k)
#         if k == 'j':
#             if index < len(answers):
#                 index += 1
#         elif k == 'k':
#             if index > 0:
#                 index -= 1
#         display_answer(answers[index])
    
