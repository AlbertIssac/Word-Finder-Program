# Word-Finder-Program
A python based web-app that finds the word by filtering a list of 10000+ words according to user input letters.
It is basically a program that helps to find a 5 letter word from the scratch by adding and eleminating letters, can be used to win every "Guess The Word" games.
## To Run it
Download all the files and place it in a folder(i.e games) and follow next steps.
Place 'webBG.jpg' and 'style.css' in a folder named 'static'.
Place 'index.html' in a folder named templates.
Open the folder where addleAPP.py is located in any IDE such as VS Code and write the code given below in the terminal.
```
python addleAPP.py
```
Well now the App will be running on local 5000 port in your browser and the link will be there in your teminal to visit the web-app.
Use this if you did not find any.
```
http://127.0.0.1:5000
```
## How to play
- There are 5 boxes which defines the exact position of a letter in a word. For instance, if you are looking for a word starts with 'w'. So place 'w' in the first box. Here, I'm revealing that we are looking for a word 'WATER'.
- Now we know there is a letter 'r' in the word but for some reason we don't know the position. So, write 'r' in the box "Letters to present" : r.
- And now click "Search". It will show some words starting with 'W' and have 'R' at random positions.
- Now, let say you get to know  that 't' is in the middle. So, place 't' in the 3rd box and again click on search.
- You will find that it has correctly guess the word WATER.
