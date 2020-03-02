# SnipGen: automated code snippet generation and automatic clipboarding in the terminal

We built this app to enhance programming workflow by increasing coder bandwidth. Every programmer we know switches from editor/IDE to browser and searches for answer to technical questions 100's of times a day. This is a bottleneck in our workflow. We created this app to make that task seamlessly integrate into your coding workflow.  

## How It Works  

The app provides a portal to quickly search Stack Overflow for natural language queries. Ask a technical question and get the answers deposited right in your terminal. The program searches google for your query and grabs the top three Stack Overflow questions. Then the answers to the top questions are presented to you in the app. You can then use keyboard shortcuts to move between the answers and questions. Importantly, whenever you move to a new answer, the code snippet from that answer is automatically in your clipboard. Just search for something and immediatly paste the result in your coding environment. If it doesn't work, move through the questions, with code snippets automatically being added to your clipboard as you do so.

## How To Use  

Start by running
```
python3 main.py  
```  

SnipGen uses vim/vi keybinding to make things easy to use during your search.  

```
j - go to next anwer (down)
k - go to previous answer (up)
l - got to next question (right)
h - go to previous question (left)
n - next query
w - toggle ***
q - quit
```  
That's it.  

*** toggling slides the clipboard through the code options, so you clipboard the code snippet you want

## Install  

### Tested in GNU/Linux (Ubuntu 18.04 LTS) and Windows 10.  

-install Python3 and pip3  
-install Firefox selenium gecko driver  
    -for Ubuntu 18.04 - https://askubuntu.com/questions/870530/how-to-install-geckodriver-in-ubuntu  
-install dependencies:  
```
pip3 install -r requirements.txt
```  

## Creators / Authours

Created by Cayden Pierce and Eric Kiefer

## License 

SnipGen, automated code snippet generation and automatic clipboarding in the terminal  
Copyright (C) 2020 Cayden Pierce   
Copyright (C) 2020 Eric Kiefer    

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
