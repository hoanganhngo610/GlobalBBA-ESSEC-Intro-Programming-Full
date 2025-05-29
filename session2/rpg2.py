# pet store data
dogs = ['Bobby', 'Puppy', 'Barker']
cats = ['Catlicious', 'Catospheric', 'Meower']
profits = 0
playerInventory = list()
loverMeter = 0

background = """You have a crush you want to impress with gifts but do not have anything in your inventory. Maybe a flower or a pet could do the trick. A pet store is nearby and you ask for a job.
The owner of the pet store agreed and left asking you to replace him during his leave. You don't know what to do and have to handle multiple cats and dogs. Each animal has a price and you are asked to make some profit.

You have to obtain at least 250 bucks during 2 days."""

# day one

day1Scenario = """This is the first day. A customer comes with a little child that dreams to adopt a cute fluffy puppy. Which animal will you choose to sell to her? """

print(background)
print('='*5)
print(day1Scenario)
print('='*5, '\n\n')

choices = dogs + cats
print('Pet store animals:', choices)
choice = ""
while choice not in choices:
    choice = input('Type an animal name:')
    if choice == 'Puppy':
        dogs.remove(choice)
        print(""" You show the puppy to the child making her very happy. This is exactly what she wanted: a cute fluffy puppy! The customer gives you an extra  consider how you gave the perfect fit for her child. """)
        profits += 200
        print('You gained', 200, 'bucks!  Congrats!' )
    elif choice in dogs:
        dogs.remove(choice)
        print(""" You show a dog to the child. This is not exactly the dog the child wanted and she look upset. """)
        print('''Child says: "I don't want it! This is not the perfect puppy fluffy and cute that I wanted!! I want a PUPPYYYYYY !!!! ''')
        print('''Customer says: "Well you will have this dog. Thanks for your... mediocre work..." ''')
        print('You gained', 50, "bucks. You could have done better don't you think so?")
        profits += 50
    elif choice in cats:
        cats.remove(choice)
        print(""" Child says: "Are you blind?!!! I ASKED FOR A DOOOGGGG! A DOG! I hate cats! """)
        print('You totally screwed. You gained nothing. Please use our brain!')
    else:
        print('Nothing in the store goes with by name. Please choose one of these choices:', choices)

print('='*5, '\n\n')
if profits > 50:
    print('You are handling the situation very well for the moment. Keep up the good work!')
elif profits != 0:
    print('You managed to make some profits but could do better.')
else:
    print('You made no profits.... You have only one day to achieve the objective.')
print('='*5, '\n\n')

# day 2
print('='*5)
print("Day 2")
print('='*5, '\n\n')

day2Scenario = """A customer comes. He is an old man wanting to have some company by adding a new pet to his collection.
Old man says: "I do not seem to be able to merge both my desire for delicious cakes and my attraction to those cute feline animals. Can you do something about it please?"
Which animal will sell to the old man? """

print(day2Scenario)
choices = dogs + cats
print('You still possess those animals:', choices)
print('Your current profits are', profits, 'bucks')
choice = ""

while choice not in choices:
    choice = input('Type an animal name:')
    if choice == 'Catlicious':
        cats.remove(choice)
        print("""Old man says: "Oh marvelous! This cat is as delicious as a sugary cake! Thank you very much! Please accept this."
        You obtained 200 bucks!  """)
        profits += 200
        print('You current profits are', profits)
    elif choice in cats:
        cats.remove(choice)
        print("""Old man says: "It's a cat alright. Not a special one I would say. Well, here I thought you could become the beacon of my very sad day. "
        You obtained 50 bucks. """ )
        profits += 50
        print("Your current profits are", profits)
    elif choice in dogs:
        dogs.remove(choice)
        print("""Old man says: "Are you serious right now?! What is... this... very agressive... animal?! Does it even meow?"  """)
        print('You obtained 5 bucks from the customer...')
        profits += 5
        print('Your current profits are', profits)
    else:
        print('Nothing in the store goes by that name. Please choose one of these choices:', choices)


# final event: the pet store owner returns
print('='*5,'\nThe pet store owner returns and checks everything \n','='*5)
if profits == 400:
    print("""Owner says: "What a perfect employee you make!! To thank you, take this blue flower and can select an animal you wish to take with you.""")
    playerInventory.append('Blue flower')
    print('A beautiful blue flower was added to your inventory.')
    print('Current inventory = ', playerInventory)

    choice = ""
    choices = dogs + cats
    print("Select an animal to adopt between those left in the pet store:", choices)
    
    while choice not in choices:
        choice = input('Type an animal name:')
        if choice in dogs:
            playerInventory.append(choice)
            dogs.remove(choice)
            print('The dog', choice, 'was added to your inventory.')
            print('Current inventory:', playerInventory)
        elif choice in cats:
            playerInventory.append(choice)
            cats.remove(choice)
            print('The cat', choice, 'was added to your inventory.')
            print('Current inventory:', playerInventory)
        else:
            print('Wrong input, choose one of the animals left in the store:', choices)
elif profits >= 250:
    print("""Owner says: "Nice handling. I see the shop is still running. Here have this blue flower as a thank you. """)
    playerInventory.append('Blue flower')
    print('A beautiful blue flower was added to your inventory.')
    print('Current inventory = ', playerInventory)
else:
    print("""Owner says: "What a disaster! You only made""", profits, """bucks?!! My pet store will have to go bankrupt because of you. But anyway... at least have this cookie.   """)
    playerInventory.append("Overcooked cookie")
    print('An overcooked cookie was added to your inventory.')
    print('Current inventory = ', playerInventory)

# epilogue
print('='*5)
epilogue = """You go see your lover and present your gifts one at a time:"""
print(epilogue, playerInventory)
for item in playerInventory:
    if item == 'Overcooked cookie':
        print("A cookie?!! Your lover is upset and decides to leave you rot alone for the rest of your miserable life!!")
        print('='*5)
        print('GAME OVER!! YOU LOSE!! SHAME on you')
        break
    elif item == 'Blue flower':
        print('"A blue flower?!! Awwwww why thank you!!"')
        loverMeter+=1
        print('You can feel the appreciation going up!')
    elif item == 'Meower':
        print('"OOhhh I love this cute meowing tiny animal!! Is it for me?! Thank you very much!"')
        loverMeter += 5
        print('Love in the air!! :)')
    elif item in cats:
        print('"Oh a cat. For me? thanks!"')
        loverMeter += 1
        print('You can feel the appreciation going up!')
    elif item in dogs:
        print('"Meh! I hate dogs...')
        loverMeter -= 1
        print('You can feel the appreciation going down!')

print('='*5, '\n')

if loverMeter >= 2:
    print("PERFECT run ! Congratz.")
elif loverMeter == 1:
    print('You managed to obtain appreciation from your crush but this is not enough. Game over!')
else:
    print('You lost every chances you had on seducing your crush. the pet owner hates you. Now you have nothing! Game over!!')