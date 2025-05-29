## Introduction to Python & Programming
## Hacker Night 2

Gaël Guibon

Essec - GBBA - A1

17/11/2020  16:30 - 22:45



### Subject
![thor](https://www.superherodb.com/pictures2/portraits/10/050/140.jpg?v=1594783082)
![spiderman](https://www.superherodb.com/pictures2/portraits/10/050/133.jpg?v=1595572836)
![wonderwoman](https://www.superherodb.com/pictures2/portraits/10/050/807.jpg?v=1605427499)

Browse and Query Superheroes!



[The database website](https://www.superherodb.com/) 

(this corpus is a subset)

[Source dataset creation](https://github.com/jbesomi/texthero/tree/master/dataset/Superheroes%20NLP%20Dataset)



### Objectives
- Create a program that will handle Superhero data from two source files
1. Implement **required actions**
2. Merge them into a terminal interface (<span class="code">`input()`</span> function)
3. Be creative and create **creative actions**



### Required Actions: todo list
Todo List:
1. open the json file using the <span class="code">`json`</span> modulefd
2. display the <span class="code">type()</span> of the root data structure from the json file
3. get the total number of superheroes
4. query a superhero by using it's name: <span class="code">`'Kylo Ren', 'Yoda', ...`</span> (<span class="field">**name**</span>)


5. create a <span class="code">`summary()`</span> function which only retrieves a subdictionary from a superhero, containing only the following keys: <span class="field">**name**</span>, <span class="field">**creator**</span>, <span class="field">**gender**</span>, <span class="field">**overall_score**</span> (use it later on to easily display smaller info about heroes)
```python
summary( hero )
```
6. get summary of all <span class="code">`'Student'`</span> heros (<span class="field">**occupation**</span>)
7. get the total number of superheroes per publisher (<span class="field">**Publisher**</span>)
8. get the number of superhero per gender (<span class="field">**Gender**</span>)


9. get the names of all the villains (<span class="field">**alignment**</span>)
10. get all the different heroes collections (<span class="field">**creator**</span>)
11. get a list of heros names from given a creator: <span class="code">`'Disney'`</span> for instance (<span class="field">**creator**</span>, <span class="field">**name**</span>)
12. get the weakest superheroes' summary (<span class="field">**overall_score**</span>)
13. get the hero with the max number of superpowers (<span class="field">**superpowers**</span>)
14. get names of all heros being part of a specific team (<span class="field">**teams**</span>): <span class="code">`'Jedi Order'`</span> for instance


15. get the name and creator of the strongest heroes (be careful of the <span class="code">`'∞'`</span> value) (<span class="field">**name</span>,<span class="field">**creator**</span>,<span class="field">**overall_score**</span>)
16. get the counts of villains, heros and neutral males and females(<span class="field">**gender**</span>, <span class="field">**alignment**</span>)


17. Create a random battle between two heros using the parameters you want. for instance: (<span class="field">**strength_score**</span> x <span class="field">**power_score**</span> / opponent's <span class="field">**durability_score**</span>). Use <span class="code">`random.choice(myList)`</span> to randomly get an element from a list
```python
random.choice( myList )
```
18. add your team from json files! Create a hero for each team member (a json file each), put your team name inside the <span class="field">**teams**</span> field (list). You can start from a random existing hero to gain ome time.



### Required Actions: textual interface and export
- Each todolist item should be able to print result or export them into a file
- Implement a <span class="code">`quit`</span> command which writes down the results obtained into a text file.



### Creative (bonus) Actions
Creative actions example ideas:
- Add one of your favorite heroes / fictional main character that is missing (<span class="code">`'Son Goku'`</span>, *etc.* )
- Stats queries : show all kinds of information from basic stats (counts, average, etc.)

You have a superb novel idea? **Just do it**



### Format
- **Small groups** (max 4 students) 
- **Location** discord server
- **Work presentation** starting from 21h45 to 22h45 (online, screen sharing)
- Otherwise **stay in discord**



### Evaluation

**Presentation Explanations**

**Project delivery by email** before leaving/presenting

----

- Project presentation (last hour)
- Sparsity of notions used
- Todolist completion
- Creativity actions
- Code clarity and good practices



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