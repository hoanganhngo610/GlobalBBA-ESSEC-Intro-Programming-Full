## Introduction to Python & Programming
## Hacker Night 1

Gaël Guibon

Essec - BBA - B2

13/11/2019  16:30 - 22:45



### Subject
Organizing and Querying Courses Data



### Objectives
- Create a program that will organize data and allow queries
- Implement **required actions**
- Be creative and create **creative actions**



### Required Actions
User should be able to:
- view all courses
- tag/untag a course as 'important'
- view all 'important' courses
- export all courses content into a single text file
- query courses by category -> text file
- query courses by subject -> text file
- query courses by date (or date range)
- change subject and category metadata for a course



### Creative Actions
Creative actions example ideas:
- add your own BBA courses to the project
- add custom metadata and queries
- stats queries : show all kinds of information from basic stats (counts, average, etc.) based on metadata or content
----
#### You decide
You have a superb novel idea? **Just do it** 



### Data
- 1 descriptive file : metadata.json
- 71 courses materials in "materials/data"
    - all `.txt` files
----
#### Data logic
- Structural information in a single file
- Content information in multiple files
- Can easily plug new content



### Format
- Small random groups (max 3 students)
- Internet allowed (no chatting between groups!)



### Evaluation
- Project presentation (last hour)
- Diversity of notions used
- Clarity of explanation and presentation
- Code clarity and good practices
-----
**Project delivery by email**



### Advises
- Use local [python install](https://www.python.org/downloads/) + [visual studio code](https://code.visualstudio.com/Download)
- Use `pprint.pprint()` to better print a dictionary
``` python 
import pprint
myDict = {'greeting': 'hello B2'}
pprint.pprint(myDict)
```
----
- A problem with your machine set up? Ask for help!
    - ...but for the code you are on your own.



# Good luck!