# # start your code here

import json, random
from pprint import pprint
pokemon_filepath = 'pokemon.json'
pokemonList = json.load( open(pokemon_filepath, 'r') )

export_filepath = 'lastresult'

########################################################
################# Utilitary functions ##################
########################################################

def exportData(data, toJson=True):
    ''' Util function : export the result into a json file or txt '''
    if toJson:
        f = open(export_filepath+'.json', 'w')
        json.dump(data, f)
        f.close()
    else:
        f = open(export_filepath+'.txt', 'w')
        f.write(str(data))
        f.close()

def mapPokemonsByGeneration():
    ''' Util function : remap the pokemons by generation '''
    generations = dict()
    for pokemon in pokemonList:
        if pokemon['Generation'] not in generations:
            generations[ pokemon['Generation'] ] = list()
        generations[ pokemon['Generation'] ].append(pokemon)
    return generations

def mapPokemonsByName():
    ''' 
    Util function : remap the pokemons by using their name as the key 
    this function and the alternative ones (byindex, etc) could be factorized
    '''
    pokeByName = dict()
    for pokemon in pokemonList:
        pokeByName[ pokemon['Name'] ] = pokemon
    return pokeByName

def mapPokemonsByIndex():
    ''' Util function : remap the pokemons by their index '''
    pokeByIndex = dict()
    for pokemon in pokemonList:
        pokeByIndex[ pokemon['Number'] ] = pokemon
    return pokeByIndex

def mapPokemonsByType1(giveNames=False):
    ''' Util function : remap the pokemons by their primary types '''
    pokeByType1 = dict()
    if giveNames:
        for pokemon in pokemonList:
            if pokemon['Type_1'] not in pokeByType1:
                pokeByType1[ pokemon['Type_1'] ] = list()
            pokeByType1[ pokemon['Type_1'] ].append(pokemon['Name'])
    else:
        for pokemon in pokemonList:
            if pokemon['Type_1'] not in pokeByType1:
                pokeByType1[ pokemon['Type_1'] ] = list()
            pokeByType1[ pokemon['Type_1'] ].append(pokemon)
    return pokeByType1

def mapPokemonsByTypeCombination():
    ''' Util function : remap the pokemons by type combination '''
    pokeByTypeCombination = dict()
    for pokemon in pokemonList:
        if pokemon['Type_2'] != None:
            combinationName = pokemon['Type_1'] + pokemon['Type_2']
            if combinationName not in pokeByTypeCombination:
                pokeByTypeCombination[combinationName] = list()
            pokeByTypeCombination[combinationName].append(pokemon)
    return pokeByTypeCombination

    

def maxListOfNumbers(elements):
    ''' 
    Util function to obtain the maximum value in a list of numbers (int float)
    Would be better to use the basic python operation for a list :
    max(myList)
    '''
    res = 0
    for element in elements:
        if element > res:
            res = element
    return res

def getPokemonsNamesRankedByValue(limit, field, lookForMax=True, pokemons=pokemonList):
    ''' 
    util function that allows you to factorize your code 
    (avoid repeating logic and code) 
    It is used for multiple todolist items. Its fleibility comes from the arguments.
    '''
    pokemonsByField = dict()
    for pokemon in pokemons:
        if pokemon[field] not in pokemonsByField:
            pokemonsByField[ pokemon[field] ] = list()
        pokemonsByField[ pokemon[field] ].append( pokemon['Name'] )
    namesAndField = dict()
    fields = list(pokemonsByField.keys())
    for i in range(limit):
        if lookForMax:
            selected = max(fields)
        else:
            selected = min(fields)
        namesAndField[selected] = pokemonsByField[selected]
        fields.remove(selected)
    return namesAndField

########################################################
################# TodoList functions ###################
########################################################

def getTotalNumberPokemons(export=True):
    ''' 1. get the total number of pokémons '''
    result = len(pokemonList)
    if export:
        exportData(result, toJson=False)
    return result

def getNumberOfPokemonsPerGeneration(export=True):
    ''' 2. get the total numbers of pokémons for each generation ''' 
    generationsCounts = dict()
    for generation, pokeList in mapPokemonsByGeneration().items():
        generationsCounts[generation] = len(pokeList)
    if export:
        exportData(generationsCounts)
    return generationsCounts

def getPokemonNameByPokedexNumber(number, export=True):
    ''' 3. get the name of a pokémon based on its pokedex number (**Number**) '''
    result = mapPokemonsByIndex()[int(number)]
    if export:
        exportData(result)
    return result
        
def getPokemonValuesByName(name, export=True):
    ''' 4. get a pokémon's values based on its name '''
    selectedPokemon = mapPokemonsByName()[name]
    result = list(selectedPokemon.values())
    if export:
        exportData(result)
    return result

def getLegendaryPokemonsInfos(export=True):
    '''  5. get the number of legendary pokémons and their names '''
    infos = {'count': 0, 'names':[]}
    for pokemon in pokemonList:
        if pokemon['isLegendary']:
            infos['count'] += 1
            infos['names'].append(pokemon['Name'])
    result = infos
    if export:
        exportData(result)
    return result

def getPokemonNameByPrimaryType(pokeType, export=True):
    ''' 6. get pokémons names by primary type (**Type_1**) '''
    result = mapPokemonsByType1(giveNames=True)[pokeType]
    if export:
        exportData(result)
    return result

def getPokemonBodyStylesInfos(export=True):
    ''' 7. view all the body styles and the number of pokémons per body style '''
    bodyStyles = dict()
    for pokemon in pokemonList:
        if pokemon['Body_Style'] not in bodyStyles:
            bodyStyles[ pokemon['Body_Style'] ] = 1
        else:
            bodyStyles[ pokemon['Body_Style'] ] += 1
    result = { 'countPerBodyStyle': bodyStyles, 'allBodyStyles': list(bodyStyles.keys()) }
    if export:
        exportData(result)
    return result

def getNameBiggestPokemons(export=True):
    ''' 8. get the name of the biggest pokémons '''
    pokemonsHeights = dict()
    for pokemon in pokemonList:
        if pokemon['Height_m'] not in pokemonsHeights:
            pokemonsHeights[ pokemon['Height_m'] ] = list()
        pokemonsHeights[ pokemon['Height_m'] ].append( pokemon['Name'] )
    # now we get the 3 highest sizes keys
    limit = 3
    namesAndSizes = dict()
    sizes = list(pokemonsHeights.keys())
    for i in range(limit):
        # highest = maxListOfNumbers(sizes) # to obtain the max manually
        highest = max(sizes)
        namesAndSizes[highest] = pokemonsHeights[highest]
        sizes.remove(highest)
    result = namesAndSizes
    if export:
        exportData(result)
    return result

def getNameRarestPokemons(export=True):
    ''' 9. get the names of the rarest pokémons '''
    pokemonsCatchRate = dict()
    for pokemon in pokemonList:
        if pokemon['Catch_Rate'] not in pokemonsCatchRate:
            pokemonsCatchRate[ pokemon['Catch_Rate'] ] = list()
        pokemonsCatchRate[ pokemon['Catch_Rate'] ].append( pokemon['Name'] )
    limit = 3
    namesAndRates = dict()
    rates = list(pokemonsCatchRate.keys())
    for i in range(limit):
        rarest = min(rates)
        namesAndRates[rarest] = pokemonsCatchRate[rarest]
        rates.remove(rarest)
    result = namesAndRates
    if export:
        exportData(result)
    return result
    
def getHeaviestPokemons(export=True):
    ''' 11. get the heaviest pokémons and the fastest ones among them '''
    heaviestPokemonsNames = getPokemonsNamesRankedByValue(5,'Weight_kg', lookForMax=True)
    pokemonsByName = mapPokemonsByName()
    heaviestPokemons = list() 
    heaviestPokemonsNamesFlatten = list()
    for names in heaviestPokemonsNames.values():
        for name in names:
            heaviestPokemonsNamesFlatten.append(name)
            heaviestPokemons.append(pokemonsByName[name])
    fastestHeaviestPokemons = getPokemonsNamesRankedByValue(3, 'Speed', pokemons=heaviestPokemons)
    result = {'fastestHeaviestPokemons':fastestHeaviestPokemons, 'heaviestPokemons': heaviestPokemonsNamesFlatten}
    if export:
        exportData(result)
    return result

def getMostPowerfulByType1(type1, export=True):
    ''' 12. get the most powerful pokémon by primary type (**Type_1**) ''' 
    pokeByType1 = mapPokemonsByType1()
    targetedPokemons = pokeByType1[type1]
    result = getPokemonsNamesRankedByValue(5, 'Total', pokemons=targetedPokemons)
    if export:
        exportData(result)
    return result
    
def getSlimestPokemons(export=True):
    ''' 13. get the slimest pokémons by using its height and weight '''
    pokemonListWithSlimField = list()
    for pokemon in pokemonList:
        pokemon['Slim'] = pokemon['Height_m']/pokemon['Weight_kg']
        pokemonListWithSlimField.append(pokemon)
    result = getPokemonsNamesRankedByValue(5, 'Slim', lookForMax=False, pokemons=pokemonListWithSlimField)
    if export:
        exportData(result)
    return result
        
def getStrongestAndWeakestMegaevolvingPokemons(export=True):
    ''' 14. get the strongest and the weakest pokémons that can mega evolve'''
    megaEvolvingPokemons = list()
    for pokemon in pokemonList:
        if pokemon['hasMegaEvolution']:
            megaEvolvingPokemons.append(pokemon)
    weakest = getPokemonsNamesRankedByValue(5, 'Total', lookForMax=False, pokemons=megaEvolvingPokemons)
    strongest = getPokemonsNamesRankedByValue(5, 'Total', pokemons=megaEvolvingPokemons)
    result = {'strongest': strongest, 'weakest': weakest}
    if export:
        exportData(result)
    return result

def getThoughestAndDamageDealersPokemons(export=True):
    ''' 15. get the thoughest pokémons and the ones that deal the biggest damages '''
    pokemonListWithTotalDefAndAtk = list()
    for pokemon in pokemonList:
        pokemon['TotalDef'] = pokemon['Defense'] + pokemon['Sp_Def'] + pokemon['HP']
        pokemon['TotalAtk'] = pokemon['Attack'] + pokemon['Sp_Atk']
        pokemonListWithTotalDefAndAtk.append(pokemon)
    damageDealersPokemons = getPokemonsNamesRankedByValue(5, 'TotalAtk', pokemons=pokemonListWithTotalDefAndAtk)
    tankersPokemons = getPokemonsNamesRankedByValue(5, 'TotalDef', pokemons=pokemonListWithTotalDefAndAtk)
    result = {'thoughest': tankersPokemons, 'damageDealers': damageDealersPokemons}
    if export:
        exportData(result)
    return result

def getMostCommonTypeCombinations(export=True):
    ''' 16. get the most common type combinations '''
    # possible to use Counter and String format for this one. But we did not tackled it during courses
    
    # first retrieve frequencies by combination
    combinationsFrequencies = dict()
    for pokemon in pokemonList:
        if pokemon['Type_2'] != None:
            combinationName = pokemon['Type_1'] + pokemon['Type_2']
            if combinationName not in combinationsFrequencies:
                combinationsFrequencies[ combinationName ] = 0
            combinationsFrequencies[ combinationName ] += 1

    # inverse map the dict by frequencies
    frequenciesCombinations = dict()
    for combination, freq in combinationsFrequencies.items():
        if freq not in frequenciesCombinations.keys():
            frequenciesCombinations[freq] = list()
        frequenciesCombinations[freq].append(combination)
    
    # no need for this dict anymore, delete it
    del combinationsFrequencies

    limit = 3
    mostCommonCombinations = list()
    for i in range(limit):
        mostFrequent = max(list(frequenciesCombinations.keys()))
        mostCommonCombinations.append({mostFrequent: frequenciesCombinations[mostFrequent]})
        del frequenciesCombinations[mostFrequent]

    if export:
        exportData(mostCommonCombinations)
    return mostCommonCombinations

def getColorFrequenciesForEachTypeCombination(export=True):
    ''' 17. get the color frequencies for each type combination '''
    pokeByTypeCombination = mapPokemonsByTypeCombination()
    colorFreqByTypeCombo = dict()
    for typeCombo, pokeList in pokeByTypeCombination.items():
        # could use Counter (from collections import Counter) here
        colorCounts = dict()
        for pokemon in pokeList:
            if pokemon['Color'] not in colorCounts:
                colorCounts[ pokemon['Color'] ] = 1
            else:
                colorCounts[ pokemon['Color'] ] += 1
        colorFreqByTypeCombo[ typeCombo ] = colorCounts
    if export:
        exportData(colorFreqByTypeCombo)
    return colorFreqByTypeCombo

def getMaleFemaleProba(export=True):
    ''' 18. get the global probability for pokémons to be male of female (**Pr_Male**) '''
    maleProbas = list()
    for pokemon in pokemonList:
        if pokemon['Pr_Male'] != None:
            maleProbas.append(pokemon['Pr_Male'])
    globalProbaMale = sum(maleProbas) / len(maleProbas) # simple percentage
    globalProbaFemale = 1 - globalProbaMale
    result = {'probaMale': globalProbaMale, 'probaFemale': globalProbaFemale}
    if export:
        exportData(result)
    return result

def fight(pokemon1, pokemon2):
    ''' 
    19. simulate a (1vs1) "fight" between arbitrary pokémons 
    We could use defense, types, attack as additional parameter to weight the damage receive or dealt. But here is a basic "combat".
    '''
    # could use String format ''.format() but we did not tackle it
    # could also use a list of Str then join it using ''.join('\n') but we did not tackle it
    fightLog = 'Starting a Fight : '+pokemon1['Name']+ ' ('+str(pokemon1['HP'])+' HP) VS '+pokemon2['Name'] + ' ('+str(pokemon2['HP'])+' HP)' + '\n'
    turnPokemon1 = True
    turnNumber = 0

    while pokemon1['HP'] > 0 and pokemon2['HP'] > 0:
        # pokemon1 attacks first
        if turnPokemon1:
            damage = pokemon1['Attack'] - (pokemon2['Defense']/2)
            fightLog += pokemon1['Name'] + ' attacks! '+ pokemon2['Name'] + ' lose '+str(damage)+ ' HP!' + '\n'
            pokemon2['HP'] -= damage
        else: 
            damage = pokemon2['Attack'] - (pokemon1['Defense']/2)
            fightLog += pokemon2['Name'] + ' attacks! '+ pokemon1['Name'] + ' lose '+str(damage)+ ' HP!' + '\n'
            pokemon1['HP'] -= damage
        turnPokemon1 = not turnPokemon1
        turnNumber += 1

    if pokemon1['HP'] <= 0:
        fightLog += pokemon2['Name'] + ' won in '+ str(turnNumber) + ' turns'
    else: 
        fightLog += pokemon1['Name'] + ' won in '+ str(turnNumber) + ' turns'
    return fightLog

########################################################
################# Run functions ###################
########################################################

def runItems():
    ''' Arbitrary Access to queries (for you to try without typing anything) '''
    pprint( getTotalNumberPokemons())
    pprint( getNumberOfPokemonsPerGeneration())
    pprint( getPokemonNameByPokedexNumber( '3' ))
    pprint( getPokemonValuesByName('Bulbasaur'))
    pprint( getLegendaryPokemonsInfos())
    pprint( getPokemonNameByPrimaryType('Grass'))
    pprint( getPokemonBodyStylesInfos())
    pprint( getNameBiggestPokemons())
    pprint( getNameRarestPokemons())
    pprint( getHeaviestPokemons())
    pprint( getMostPowerfulByType1('Grass'))
    pprint( getSlimestPokemons())
    pprint( getStrongestAndWeakestMegaevolvingPokemons())
    pprint( getThoughestAndDamageDealersPokemons())
    pprint( getMostCommonTypeCombinations())
    pprint( getColorFrequenciesForEachTypeCombination() )
    pprint( getMaleFemaleProba() )
    pprint( fight(random.choice(pokemonList), random.choice(pokemonList)))


# mapping actions into a dictionary to prevent numerous if, elif else
# two possibilities : access a value without argument ('exec') or ask for an argument and trigger the function (with the input argument)
queries = { 
    'quit': 'quit the app',
    'count': {'exec':  getTotalNumberPokemons()}, 
    'generation counts': {'exec': getNumberOfPokemonsPerGeneration()}, 
    'name by id': {'func': getPokemonNameByPokedexNumber, 'ask': 'Type a pokedex number'},
    'pokemon by name': {'func': getPokemonValuesByName, 'ask': 'Type a pokemon name'},
    'legendary': {'exec': getLegendaryPokemonsInfos()},
    'pokemon by type': {'func': getPokemonNameByPrimaryType, 'ask': 'Type the pokemon primary type'},
    'body styles': {'exec': getPokemonBodyStylesInfos()},
    'biggest': {'exec': getNameBiggestPokemons()},
    'rarest': {'exec': getNameRarestPokemons()},
    'heaviest': {'exec': getHeaviestPokemons()},
    'powerful by type': {'func': getMostPowerfulByType1, 'ask': 'Type the pokemon primary type'},
    'slimest': {'exec': getSlimestPokemons()},
    'mega evolutions': {'exec': getStrongestAndWeakestMegaevolvingPokemons()},
    'thoughest damage': {'exec': getThoughestAndDamageDealersPokemons()},
    'common type combo': {'exec': getMostCommonTypeCombinations()},
    'colors per type': {'exec': getColorFrequenciesForEachTypeCombination()},
    'male female proba': {'exec': getMaleFemaleProba()},
    'random fight': {'exec': fight(random.choice(pokemonList), random.choice(pokemonList))}
}

def terminalInterface():
    ''' function to ask for a query and handle wrong queries '''
    req = ''
    while req != 'quit':
        print('Possible queries:', list(queries.keys()) )
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



## Here you can run the temrinal interface or every items with arbitrary values for test

terminalInterface()
# runItems() # TRY IT

# # good luck !