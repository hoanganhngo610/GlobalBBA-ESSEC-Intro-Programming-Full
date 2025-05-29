# modify this variable
__author__ = "PUT YOUR NAME HERE BEFORE SENDING IT"


import json
from pprint import pprint


def displayStudentName(studentName):
    '''
    A function that serves to display the author name (the student).
    Don't forget to change the __author__ variable and put your name in it!
    '''
    print("="*10)
    print("This game is made by", studentName)
    print("="*10)

displayStudentName(__author__)

##############################################
# BELOW IS A STARTER PACK FOR THE EXAM
# this should help you but you can override it
# if you desire to do so
##############################################

# player informations placeholder
player = {}

# create an events variable here (or through another file)
events = {}

# pastChoices variable to keep pastChoices
pastChoices = []

## define functions (indicated by their names to help you start)


# put a function to retrieve events from the json file

# put different functions for each action
    
# You should adapt this function (from course materials) to your game
def askAction(event, choices):
    '''
    Ask an action from the user. Stay alive while the action is not recognized.
    '''
    choice = ''
    while choice not in choices:
        print('player status', player)
        choice = input()
        try:
            print(event[choice]['message'])
            if 'hploss' in event[choice]: 
                alive = removeHealth(event[choice]['hploss']) # use you action(s) if needed
                if not alive : break
            pastChoices.append(choice)
            if('paths' in event[choice]):
                askAction(event[choice]['paths'], list(event[choice]['paths'].keys()) )
        except:
            print('WRONG : Possible choices', choices )
    return True
