__author__ = 'Gaël Guibon'




######
## MODULE IMPORTS
######

## import the 'json' module
import json
## import the pprint function from the pprint module
## pprint means PrettyPrint
from pprint import pprint




######
## LOAD THE JSON FILE
######

## Open the file in a with environnement (so that it closes automatically)
with open('TMDB.json', 'r') as f:
    movies = json.load(f) # put the parsed content of JSON file into the variable 'movies'

## Check the type of the movies variable
print(  'The data from the JSON file is of type:', type( movies )  )

## Check the type of the first element from the movies list
firstMovieFromList = movies[0] # a list starts from zero

firstMovieType = type( firstMovieFromList )

print( 'The first element in the JSON data is of type:', firstMovieType )

## Check the first-level keys from a movie in order to see the shallow organisation of dictionaries representing movie information (uses the first movie as an example)
print( 'The keys to access information from a movie dictionary are', list( firstMovieFromList.keys() ) )


######
## UTITLITARY (CONVENIENT) FUNCTIONS
######

def getMovieWithMaxValueOfTargetedField(fieldname):
    """
    5. get the title of the movie with the maximum number of votes (**vote_count**)
    6. get the maximum number of votes (**vote_count**)

    This function returns the whole movie so we can later extract the 'title' and 'vote_count' from it in order to answer items 5 and 6.
    This is why this function used in the 2 following functions below.

    Returns:
        dict: the whole movie dict with the maximum vote_count
    """

    result = {'vote_count':0} # initialized with a vote_count field associated with zero so we can erase the whole variable by a new movie dict (which also contains a vote_count field)
    
    for movie in movies:
        currentMovieVoteCount = movie['vote_count']
        if currentMovieVoteCount > result['vote_count']:
            result = movie
    
    return result



######
## DEFINE THE FUNCTIONS
######

def getNumberOfMovies():
    """
    1. get the number of movies by using the length of the movies list

    Args:
        param1: This is the first param.
        param2: This is a second param.

    Returns:
        int: The number of movies
    """
    return len(movies)


def getMovieByTitle(title):
    """
    2. get a movie by its title (**title**)

    Args:
        title (str): the title of the movie

    Returns:
        dict: the dictionary representing the movie's information
    """

    movieFound = None
    
    for movie in movies:
        currentMovieTitle = movie['title']
        if currentMovieTitle == title: # double == for comparison
            movieFound = movie # one = for value assignement
            break # stop (break) the for loop
    
    # print something if no movie with this title has been found
    if movieFound == None: 
        print("Movie not found :'(")
    
    return movieFound


def getMoviesByStatus(status):
    """
    3. get titles of all rumored movies (**status**)

    This function can adapt to any status, not only 'Rumored' depending on the value of the argument

    Args:
        status (str): a status such as 'Rumored'
    
    Returns:
        list: movies dictionaries in a list
    """

    results = []
    
    for movie in movies:
        currentMovieStatus = movie['status']
        if currentMovieStatus == status:
            results.append( movie )
    
    return results


def getDifferentMovieStatuses():
    """
    4. get all the different statuses possible (**status**)

    Returns:
        list: list of all different statuses encountered without redundancy
    """
    
    statuses = []
    
    for movie in movies:
        currentMovieStatus = movie['status']
        if currentMovieStatus not in statuses:
            statuses.append( currentMovieStatus )
    
    ## ADVANCED other way to do it in one line: using set() (a collection without any duplicate nor order) and list comprehension (compressed list creation from a loop)
    # statuses = set( [movie['status'] for movie in movies] )
    
    return statuses


def getMovieWithMaxVotes():
    """
    5. get the title of the movie with the maximum number of votes (**vote_count**)
    6. get the maximum number of votes (**vote_count**)

    This function returns the whole movie so we can later extract the 'title' and 'vote_count' from it in order to answer items 5 and 6.
    This is why this function used in the 2 following functions below.

    This function shows how to get the maximum without using the max() function

    Returns:
        dict: the whole movie dict with the maximum vote_count
    """
    
    result = {'vote_count':0} # initialized with a vote_count field associated with zero so we can erase the whole variable by a new movie dict (which also contains a vote_count field)
    
    for movie in movies:
        currentMovieVoteCount = movie['vote_count']
        if currentMovieVoteCount > result['vote_count']:
            result = movie
    
    return result


def getTitleOfMovieWithMaxVotes():
    """
    5. get the title of the movie with the maximum number of votes (**vote_count**)

    Uses the previous utilitary function

    Returns:
        str: movie title
    """

    movieWithMaxVotes = getMovieWithMaxVotes()
    
    titleOfMovieWithMaxVotes = movieWithMaxVotes['title']
    
    return titleOfMovieWithMaxVotes


def getMaxNumberOfVotes():
    """
    6. get the maximum number of votes (**vote_count**)

    Uses the previous utilitary function

    Returns:
        int: max number of vote_count
    """
    
    movieWithMaxVotes = getMovieWithMaxVotes()
    
    maxNumberOfVotes = movieWithMaxVotes['vote_count']
    
    return maxNumberOfVotes


def getMovieWithMaxRevenue():
    """
    7. get the movie with the highest revenue (**revenue**)

    Using the max() function and the index() function from a list

    Returns:
        dict: movie information as dict 
    """

    revenueList = []
    
    for movie in movies:
        currentMovieRevenue = movie['revenue']
        revenueList.append(  currentMovieRevenue  )
    
    maxValue = max(revenueList)
    
    indexOfTheMaxValue = revenueList.index(  maxValue  ) # retrieves at which index (place) is a value in a list 
    
    movieWithMaxRevenue = movies[ indexOfTheMaxValue ] # from the list of movies get the movie by using the index (exemple: movies[5] , 5 is an index)
    
    return movieWithMaxRevenue


def getMovieWithMaxBudget():
    """
    8. get the movie with the highest budget (**budget**)

    Using the max() function and the index() function from a list

    Returns:
        dict: movie information as dict 
    """
    
    budgetList = []
    
    for movie in movies:
        currentMovieBudget = movie['budget']
        budgetList.append(  currentMovieBudget  )
    
    maxValue = max( budgetList )
    
    indexOfTheMaxValue = budgetList.index(  maxValue  )
    
    movieWithMaxBudget = movies[ indexOfTheMaxValue ]
    
    return movieWithMaxBudget


def getMovieWithMostDifferenceRevenueBudget():
    """
    9. get the movie with highest difference between revenue and budget (**revenue**, **budget**)

    Using the max() function
    Using the abs() function: returns the absolute value of a numerical value (hence -1 will become 1)

    """

    differencesList = []
    
    for movie in movies:
        currentMovieDifference = movie['budget'] - movie['revenue']
        currentMovieDifferenceAbsoluteValue = abs( currentMovieDifference )
        differencesList.append(  currentMovieDifferenceAbsoluteValue  )
    
    maxDifference = max( differencesList )
    
    return maxDifference


def getNumberOfMoviesPerOriginalLanguage():
    """
    10. get the number of movies per original language (**original_language**)


    Returns:
        dict: key = original_language and value = integer count of movies for this original_language
    """
    
    langsDict = {}
    
    for movie in movies:
        currentMovieOriginalLanguage = movie['original_language']
        # check if the language exists as a key in the dict. Could also use langsDict.setdefault(value, 1)  
        if currentMovieOriginalLanguage not in langsDict:
            langsDict[ currentMovieOriginalLanguage ] = 1
        else:
            langsDict[ currentMovieOriginalLanguage ] += 1 # increment its value with one
    
    return langsDict



def getMovieFrequenciesPerGenre():
    """
    11. get the number of movies per genre (**genres**)

    Same logic as previous function.

    Returns:
        dict: { genre1 : count1, .... , genreN : countN }
    """
    
    genresCounts = {}
    
    for movie in movies:
        
        for genre in movie['genres']: # iterates over the list of genres
            genreName = genre['name']
            if genreName not in genresCounts:
                genresCounts[ genreName ] = 1
            else:
                genresCounts[ genreName ] += 1

    return genresCounts



def getMostCommonGenreAssociatedTo(name):
    """
    12. get the frequencies of genres associated with the comedy genre (**genres**)

    This function can adapt to any genre given the genreName argument.

    Using the setdefault(value, defaultvalue) function from dictionaries.

    Args:
        genreName (str): the name of the targeted genre

    Returns:

    """
    
    # Retrieve the first target dictionary found for later comparisons
    targetGenre = None
    
    for movie in movies:
        if targetGenre is not None:
            break
        for genre in movie['genres']:
            if genre['name'] == name:
                targetGenre = genre
                break
    
    # Now we can check if the targetGenre is in the genres of each movie (in the loop)
    associations = {}
    
    for movie in movies:
        if targetGenre in movie['genres']:
            # remove the targetGenre to be able to only take into account the other ones associated to it
            movie['genres'].remove(targetGenre)
            for genre in movie['genres']:
                associations.setdefault(genre['name'], 0) # this line only does something if the key did not existed
                associations[genre['name']] += 1

    return associations


def getTitlesOfMoviesWithModifiedTitleAndTotalNumber():
    """
    13. get titles of the movies with a modified title (**original_title**, **title**)
    14. get the total number of movies with a modified title (**original_title**, **title**)

    As the result is a list. For the item 14 we can use this function and just take the length of the resulting list ( len() function )

    Returns:
        list: list of dictionaries with only the original title and the new one.
    """

    foundMovies = []
    
    for movie in movies:
        newTitle = movie['title']
        originalTitle = movie['original_title']
        if newTitle != originalTitle:
            titlesDict = {'original': originalTitle, 'new': newTitle }
            foundMovies.append( titlesDict )
    
    return foundMovies



def getMovieTitlesFromCountry(country):
    '''
    15. get the titles of all movies from a specific country (`'United Kingdom'` for instance)

    Args:
        country (str): a String value for the country name

    Returns:
        list: list of string titles
    '''
    
    titles = []
    
    for movie in movies:
        for productionCountry in movie['production_countries']:
            if productionCountry['name'] == country:
                titles.append(  movie['title']  )
                break # with this indentation, breaks only the nearest for (so only the loop over production countries)
    
    return titles



def getMoviesTitlesWithKeyword(kwd):
    """
    Useful for 16th item if kwd == 'violence'
    Also useful for the 17th item

    Args:
        kwd (str): keyword's name to search for

    Returns:
        list: the movie titles in a list
    """

    result = []

    for movie in movies:
        for keyword in movie['keywords']:
            if kwd == keyword['name']: 
                result.append( movie['title'] )
    
    return result


def getNumberOfViolentMovies():
    """
    16. get the total number of violent movies

    Reuse the previous function

    Returns:
        int: the length of the list of violent movie titles
    """

    violentMovieTitles = getMoviesTitlesWithKeyword( 'violence' )

    return len( violentMovieTitles )


def getPercentageOfViolentMovies():
    """
    17. get the percentage of violent movies

    Returns:
        float: the raw percentage
    """

    violentMoviesTitles = getMoviesTitlesWithKeyword('violence')
    
    percentageOfViolentMovies = len( violentMoviesTitles ) / len( movies ) * 100

    return percentageOfViolentMovies


def getAverageMovieDuration():
    """
    18. get the average movie duration (**runtime**)

    Using the sum() function.
    Ignoring empty values (None)

    Returns:
        float: average movie duration in minutes
    """

    # first get all movie duration in a list
    runtimes = []
    
    for movie in movies:
        # the trap here is that there is some movies without any duration (None). You have to ignore them.
        if movie['runtime'] is not None:
            runtimes.append( movie['runtime'] )

    # then we compute the average
    averageRuntimes = sum(runtimes) / len(runtimes) 
    
    return averageRuntimes







######
## ADDITIONAL FUNCTION (not required)
######


def getAllTitlesByLanguageCode(language):
    """
    get the all the titles of movies available in a certain language (spoken_languages)

    Args:
        language (str): the iso_639_1 language code as a string. Such as 'en' for English for instance.

    Returns:
        list: list of titles
    """

    titles = list()
    
    for movie in movies:
        for lang in movie['spoken_languages']:
            if lang['iso_639_1'] == language:
                titles.append( movie['title'] )
    
    return titles



######
## TERMINAL INTERACTIONS
######


def createQueriesDict():
    """
    Creates the whole queries dict with different architectures:
    'exec' -> value is the result execution of a function
    'func' -> is a function (not a call, the function directly as is)
    'ask' -> message to ask an input() that will serve as the argument for the function in 'func'

    Returns:
        dict: queries as a dict (such as events from Role Playing Games)
    """

    queries = {
        'quit': 'quit the app',

        'count': {'exec': getNumberOfMovies() },
        
        'movie by title': {'func': getMovieByTitle, 'ask': 'Enter a movie title'},
        
        'movie by status': {'func': getMoviesByStatus, 'ask': 'Enter a status\' name'},
        
        'different statuses': {'exec': getDifferentMovieStatuses()},
        
        'movie title with max votes': {'exec': getTitleOfMovieWithMaxVotes()},
        
        'max votes': {'exec': getMaxNumberOfVotes()},
        
        'movie with max revenue': {'exec': getMovieWithMaxRevenue()},
        
        'movie with max budget': {'exec': getMovieWithMaxBudget()},
        
        'movie with max diff': {'exec': getMovieWithMostDifferenceRevenueBudget()},
        
        'original lang counts': {'exec': getNumberOfMoviesPerOriginalLanguage()},
        
        'genre counts': {'exec': getMovieFrequenciesPerGenre()},
        
        'common genres with comedy': {'exec':  getMostCommonGenreAssociatedTo('Comedy')},
        
        'movies with modified titles': {'exec': getTitlesOfMoviesWithModifiedTitleAndTotalNumber()},
        
        'count movies with modified titles': {'exec': len(getTitlesOfMoviesWithModifiedTitleAndTotalNumber()) },

        'movies from UK': {'exec': getMovieTitlesFromCountry('United Kingdom') },

        'violent movies count': { 'exec': getNumberOfViolentMovies()},

        'violent movies percentage': { 'exec': getPercentageOfViolentMovies()},

        'avg movie duration': {'exec': getAverageMovieDuration()}

    }

    return queries


def terminalInterface(queries):
    ''' 
    function to ask for a query and handle wrong queries 
    It will execute functions (exec) or ask for more choices if needed (ask) and then execute the function (func)

    Args:
        queries (dict): dictionary of possibles choices (such as the events dict from RPGame but with functions calls inside)
    '''

    print('Welcome')

    print('''
    
     
                                      ,...,,,,....
                              ,.╥╦╦╦╦╫╫╫╫╫╫╫╫╫╫╫╫╫╫╦╦╦╦╥╥.
                          .╥╦]╫╫╫╫░╨╨╨╙╨"""```""╨╙╨╨╨╨╩╫╫╫Ñ╦╦.
                       ╥╦╫╫╫╫╩╨╨"`                    ``"╨╨╫╫╫╫N╥.
                    ╥╦╫╫╫╩╨╨``                             `╙╨╨╫╫╫N╥
                 ,╥╬╫╫╫░░`                                    ``╨╩╫╫Ñ╦.
                ╦╫╫╫╫░░`                                         `╨╩╫╫╫╦.
              ╔╬╫╫╫░░`»»       ,╥╗µ»                »╔╗µ»      » »»»░╩╫╫Ñ╦
             ╦╫╫╫░░»»»»»»»»»»»╔╬▓██▓N»            »j▓▓█▓▓N»»»»»»»»»»»░░╫╫╫N.
           :╬╫╫╫░░»»»»»»»»»»»╔╫▓▓▓▓█▓U»»»»»»»»»»»»]╣▓▓▓▓█▓U»»»»»»»»»»»»░╫╫╫Ñm
          :╫╫╫╫░░░░»»░»»»»»»»╟▓▓▓▓▓▓▓Ñ»»»»»»»»»»»»╟▓▓▓▓▓▓▓Ñ»»»»»»»»░░n░░░╫╫╫ÑH
         :]╫╫╫░░░░░░░░░░░░░»µ╫▓▓▓▓▓▓█▌░»»»»»»»»»»░╫▓▓▓▓▓▓▓▓░»░»░░░░░░░░░░░╫╫╫╫H
         ]╫╫╫░░░░░░░░░░░░░░░░╫▓▓▓▓▓▓█▌Ü»░░░░»»░»»░╫▓▓▓▓▓▓▓▌░░░░░░░░░░░░░░░░╫╫╫Ñ
        ╔╫╫╫╫░░░░░░░░░░░░░░░░╫▓▓▓▓▓▓▓▌░░░░░░░░░░░░╫▓▓▓▓▓▓▓▌░░░░░░░░░░░░░░░░╫╫╫╫H
        j╫╫╫╫░░░░░░░░░░░░░░░░╫▓▓▓▓▓▓▓Ñ░░░░░░░░░░░░╫▓▓▓▓▓▓▓╫░░░░░░░░░░░░░░░░╫╫╫╫Ñ
       :╫╫╫╫╫╫╫░░░░░░░░░░░░░░░╫▓▓▓▓▓╫░░░░░░░░░░░░░░╫▓▓▓▓▓▌░░░░░░░░░░░░░░░░╫╫╫╫╫╫H
       ╔╫╫╫╫╫╫╫░░░░░░░░░░░░░░░░╬▓▓▓Ñ░░░░░░░░░░░░░░░░╬▓▓▓Ñ░░░░░░░░░░░░░░░╫╫╫╫╫╫╫╫H
       ╚╫╫╫╫╫╫╫░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░╫╫╫╫╫╫╫╫H
       ╚╫╫╫╫╫╫╫╫░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░╫╫╫╫╫╫╫╫H
       `╟▓╫╫╫╫╫╫╫░╫╫▓▓╬╬╬╦╦░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░╦╦╦╬╬╫▓▓╫░░╫╫╫╫╫╫╫╫Ñ`
        ╚╫╫╫╫╫╫╫╫░╫╣█▓▀█▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬╦▄╦╦╦╦╦╦▄▄╬▄▄╬╬╬╬▓▓▓▓▓▓▓██▓▓▓▌░╫╫╫╫╫╫╫╫╫Ñ
        `╫╫╫╫╫╫╫╫╫╫╫▓╫░░╨╨╨╨╨▀▀▀▀▓███████▓▓▓▓▓█████████▀▀▀▀╨╨╨╨░░░╣▓╫╫╫╫╫╫╫╫╫╫╫░
         ╚╫╫╫╫╫╫╫╫╫╫▓▓Ñ░»»»»»»  ` ```````````````````````  »»»░░░╫▓▓╫╫╫╫╫╫╫╫╫╫H
          ╨╫▓╫╫╫╫╫╫╫╫▓▓▓╬╗▄µµ,,,.                     .,,,╓╔▄╬╬╣▓▓▓╫╫╫╫╫╫╫╫╫╫Ñ`
           ╨╫▓╫╫╫╫╫╫╫╫╫▓▓▓▓▓▓▓▓▓▓▓╣╬╗╗╗╗╗╗╗╗╗╗╗╗╗╗Φ╣▓▓▓▓▓▓▓▓▓▓▓▓▓╫╫╫╫╫╫╫╫╫╫▓Ñ`
            ╙╣▓╫╫╫╫╫╫╫╫╫▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓Ñ╫╫╫╫╫╫╫╫▓╫Ñ
             `╬╫╫╫╫╫╫╫╫╫╫╫▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╫╫╫╫╫╫╫╫╫╫▓Ñ╨
               ╨╣▓▓╫╫╫╫╫╫╫╫╫╫▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╫╫╫╫╫╫╫╫╫╫╫▓╫╨`
                `╨╬▓▓╫╫╫╫╫╫╫╫╫╫╣▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╫╫╫╫╫╫╫╫╫╫╫╫▓╫Ñ`
                  `╙╣╫▓╫╫╫╫╫╫╫╫╫╫╫╫╫╣╫▓▓▓▓▓▓▓▓▓▓▓▓╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫▓╬╨`
                     `╨╬╫▓╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫▓▓╫╨"
                        `╙╩╬╫▓▓╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫▓╫Ñ╨"
                            `╙╨╬╬╣▓╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫▓╫╣╬╨╨"`
                                 ``"╙╨╨╨╨╩╬╬╬╬╩╩╨╨╨╨""`
     
    
---
^[ [^ascii ^art ^generator](http://asciiart.club) ^] 

    ''')

    req = ''
    
    while req != 'quit':
        
        print('Possible queries:')
        
        pprint( list(queries.keys()) )
        
        req = input('Type your selection:\n')
        
        try:
            if 'exec' in queries[req]:
                print( '\n##### RESULT #####\n\n')
                pprint( queries[req]['exec'])
                print('\n\n' )
            else:
                arg = input(queries[req]['ask']+':\n')
                print('\n##### RESULT #####\n\n')
                pprint( queries[req]['func'](arg))
                print( '\n\n' )
        except:
            pprint('WRONG query' )



# now we can create the queries and start the interface input() loop

queries = createQueriesDict()
terminalInterface( queries )


