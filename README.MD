# SnipGen: Automatic Stack Overflow search for code snippets

We built this app to enhance programming workflow by increasing coder bandwidth. Every programmer we know switches from editor/IDE to browser and searches for answer to technical questions 100's of times a day. This is a bottleneck in our workflow. We created this app to make that task seamlessly integrate into your coding workflow.  

## How It Works  

The app provides a portal to quickly search Stack Overflow for natural language queries. Ask a technical question and get the answers deposited right in your terminal. The program searches google for your query and grabs the top three Stack Overflow questions. Then the answers to the top questions are presented to you in the app. You can then use keyboard shortcuts to move between the answers and questions. Importantly, whenever you move to a new answer, the code snippet from that answer is automatically in your clipboard. Just search for something and immediatly paste the result in your coding environment. If it doesn't work, move through the questions, with code snippets automatically being added to your clipboard as you do so.

## How To Use  

Start by running
```
python3 client.py  
```  

SnipGen uses vim/vi keybinding to make things easy to use during your search.  

```
j - go to next anwer (down)
k - go to previous answer (up)
l - got to next question (right)
h - go to previous question (left)
n - next query
q - quit
```
That's it.  

## Install  

-install Python3 and pip3
-Tested in GNU/Linux and Windows 10.
-install Firefox selenium gecko driver
    -for Ubuntu 18.04 - https://askubuntu.com/questions/870530/how-to-install-geckodriver-in-ubuntu
-install dependencies
```
pip3 install -r requirements.txt
```

### Todo

-make webdriver open in the background (PhantomJs, chrome on background mode)
