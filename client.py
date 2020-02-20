# from stackpull import StackPull
# from scraper import Scraper
from getch import _Getch

if __name__ == "__main__":
    stack_pull = StackPull()
    scraper = Scraper()
    query = input('Enter your search: ')
    question_ids = scraper.scrape(query)
    stack_pull.load(question_ids[0])
    index = 0
    print("the lenght is: {}".format(len(stack_pull.answers)))
    print(stack_pull.return_answer(index)[2])
    while True:
        getch = _Getch()
        key_code = ord(getch())
        if key_code == 106 and index < len(stack_pull.answers) - 1: #j
            index += 1
            print(stack_pull.return_answer(index)[2])
        elif key_code == 107 and index > 0: #k
            index -= 1
            print(stack_pull.return_answer(index)[2])
        elif key_code == 104: #h
        
        elif key_code == 108: #l
        
        elif key_code == 113: #q
            break
        if command == 'j' :
            
            
    
