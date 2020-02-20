from stackpull import StackPull
from scraper import Scraper

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
        command = input("Command: ")
        if command == 'j' and index < len(stack_pull.answers)-1:
            index += 1
            print(stack_pull.return_answer(index)[2])
        elif command == 'k' and index > 0:
            index -= 1
            print(stack_pull.return_answer(index)[2])
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
    
