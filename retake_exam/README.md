## Introduction to Python & Programming
## Retake Exam

Gaël Guibon

Essec - GBBA - A1



### Subject: Enhance your Role Playing Game

![textualgame](https://technabob.com/blog/wp-content/uploads/2012/11/text-based-multiplayer-shooter-game-by-eigen-lenk.jpg)



### Objectives
- Create an enhanced Role Playing Game using notions learned during the course.
    - The story and choices can be very basic (*the code is more important than the text content*), but need to be your original game
    - You can either start from your existing game or start a new one

### Todo List
0. **Preliminary**: Create a directory and put the starter file 'my_game.py' in it. Then, open the directory with Visual Studio Code
1. **Events**: Create the whole events script and related actions/text in an external JSON file by using a dedicated function
```python
def createEvents():
    # create the dictionary events and store it into a json file
```
2. **User actions**: Re-use the askAction() function and modify it to your needs according to the JSON file
3. **Functions**: Create a dedicated function for each action (̀`AddHealth()`, `DeleteItem()`, etc. )
3. **Dict**: Create a dictionary representing and gathering player informations
```python
aDictionary = {}
anotherEmptyDictionary = dict()
```
4. **For**: Ensure you implement an inventory like mecanism where you can use the **for** loop
```python
for el in myList: # be careful of the syntax    for in :
    # do something
```
5. **User status**: After each interaction, the user should be able to see its current information and items (inventory)
6. **Log user choices**: At the end of the game the user should be prompted its game stats (number of actions done and number of choices undiscovered)
7. **System Commands**: Add a `help` command that prompts basic usage guidelines, a `status` command displaying the user's status and inventory, and a `quit` command to close and exit the game.
```python
# to close and exit a python script programmatically, use this
exit()
``` 



### Required Actions: textual interface and export
- Each todolist item should be able to print result or export them into a file
- Implement a <span class="code">`quit`</span> command which writes down the results obtained into a text file.



### Format
- **Individual**: the work should be original and individual 
- **Home project**: due to COVID limitations, the work is an individual work project
- **Questions**: you can me ask any questions about the exam by email



### Evaluation

**Project delivery by email** using the following guidelines:
- put your name in the __author__ variable at the begining of the python file
- send the file(s) by email 

Project will serve to mainly evaluate your Python basic notions understanding: variables types, loops, file reading, functions, syntax, etc. 

Creative additions will be evaluated as a bonus. Hence, you can also go further in creating this role playing game.



### Advises
- Use local [python install](https://www.python.org/downloads/) + [visual studio code](https://code.visualstudio.com/Download)
- Use `pprint.pprint()` to better print a dictionary
``` python 
from pprint import pprint
myDict = {'greeting': 'hello A1'}
pprint(myDict)
```
----
- A problem with your machine set up? Ask for help!
    - ...but for the code you are on your own.



## Good luck!