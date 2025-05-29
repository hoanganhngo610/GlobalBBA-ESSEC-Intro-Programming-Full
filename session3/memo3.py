##### This script is a quick memo of the different notions through examples

## Variable Types
iAmAnInteger = 10
print(iAmAnInteger, 'is of type', type(iAmAnInteger))

iAmAFloat = 10.0
print(iAmAFloat, 'is of type', type(iAmAFloat))

iAmAString = 'I am a String (str())'
print(iAmAString, 'is of type', type(iAmAString))

iAmABoolean = True # only True or False.
print(iAmABoolean, 'is of type', type(iAmABoolean))

iAmAList = ['hello', 20, False] # multipe values of multiple types
print(iAmAList, 'is of type', type(iAmAList), 'and the first element', iAmAList[0],'over', len(iAmAList), 'elements is of type', type(iAmAList[0]))

iAmADictionary = {'name':'pikachu', 'element': 'electricity', 'cute': False} # key:value  separated by a comma ,
print(iAmADictionary, 'is of type', type(iAmADictionary), 'and possesses the following keys:', list(iAmADictionary.keys()) )

## Assign a value to a variable with "="
pikachu = iAmADictionary # pikachu is now the same dict as iAmADictionary

## Compare equality "==" of non equality "!="
resultIsABoolean = pikachu == iAmADictionary # will be True
resultIsABoolean = pikachu != iAmADictionary # will be False

## Statements if while for def require colons and indentation
if pikachu == iAmADictionary : # here the value of the condition after "if" can only be boolean (True or False)
    print('They are the same')

## Iterate over a list
for element in iAmAList:
    print( element )

## A reminder template for indentations and nested indentations (here there are 3 hierarchical levels)
if True :
    dummyVariable = 'dummy'
    if dummyVariable == 'dummy':
        print('indeed')
    elif dummyVariable == 'hello':
        print('hellow')
    else:
        print('it is not a dummy variable')
    
## Function reminder
def myFunction(mandatoryArgument1, mandatoryArgument2, optionalArgument1WithDefaultValue=20):
    print('myFunction is called ! ')
    return (mandatoryArgument1 + mandatoryArgument2) * 20 # returns a value

value = myFunction(2, 5) # will do the instructions inside the function and returns the value that I assign to the variable 'value'

## A reminder template for function possible usages
state = {} # empty dictionary where I will put global changes
def wakeUp():
    ''' Use this function if you want to wake up '''
    state['awake'] = True

def takeSomeMoney():
    ''' take some pocket money with you '''
    if state['awake'] == True:
        state['money'] += 147
    else:
        print('You are still sleeping...')

def goShopping(location): # a function with one mandatory argument
    ''' use this function to go shopping BUT be sure to have some money with you'''
    if state['awake'] and state['money'] >= 1:
        state['shoppingLocation'] = location
        print('happy shopping at', location)
    else:
        print('you cannot buy anything without money!')

# now I can call all the functions in the right order (other order will change the effects)
wakeUp()
takeSomeMoney()
goShopping('Rue de Rivoli, Paris')

