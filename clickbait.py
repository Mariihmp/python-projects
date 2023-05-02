import random,sys
OBJECT__PRONUNS = ['Her', 'Him','Them']

POSSESSIVE_PRONUNS = ['Her','His','Their']
PERSONAL_PRONUNS = ['She','He','They']
STATES = ['california','texas','florida','newyork','pennsylvania','illinois','ohio','georgia','north carolina', 'michigan']

NOUNS = ['Athlete', 'Clown', 'Shovel', 'Paleo Diet', 'Doctor', 'Parent',
'Cat', 'Dog', 'Chicken', 'Robot', 'Video Game', 'Avocado','Plastic Straw','Serial Killer', 'Telephone Psychic']
PLACES = [
    'House', 'Attic', 'Bank Deposit Box', 'School', 'Basement','Workplace', 'Donut Shop', 'Apocalypse Bunker'
]
WHEN =['soon','this year','later today','right now','next week']

def main():
    print("""
          clickbait headline genaroter
          trying to catch users to click to the headline 
          our website needs to trick people into looking into ads 
          """) 
    while True:
        print('enter the number of clickbaits to generate')
        response = input('---')
        if not response.isdecimal():
            print('please enter a number')
        else:
            numberOfHeadlines = int(response)
            break
        
        for i in range(numberOfHeadlines):
            clickbait_type = random.randint(1,8)#we have 8 type of clickbaits to choose from basically 
            if clickbait_type ==1:
                headline = dinousors()
            elif clickbait_type ==2:
                headline = globalwarming()
            elif clickbait_type ==3:
                headline = AItakingoverhuman()
            elif clickbait_type ==4:
                headline = apoclypticEarthquick()
            elif clickbait_type ==5:
                headline = listOfJobsAutomatedByAI
                ()
            elif clickbait_type ==6:
                headline = massShootingintexas()
            elif clickbait_type == 7:
                headline = freewebsitetolearn()
            elif clickbait_type ==8:
                headline = theEndOfWorld()
            print(headline)
        print()
        
website = random.choice(['tweeter','blag','google','facebook','instagram'])
when = random.choice(WHEN).lower()
def theEndOfWorld():
    noun = random.choice(NOUNS)
    return f"the end of the world is here {noun} says" 
def freewebsitetolearn():
    pronoune = random.choice(PERSONAL_PRONUNS)
    noun1 = random.choice(NOUNS) 
    noun2 =random.choice(NOUNS)
    return f"check this {noun1} , a free website to {noun2} all of this are availabel for {pronoune}"
def massShootingintexas():
    number1 = random.randint(3, 19)
    pluralNoun = random.choice(NOUNS) + 's'
    # number2 should be no larger than number1:
    number2 = random.randint(1, number1)
    return '{} Reasons Why {} Are More Interesting Than You Think (Number {} Will Surprise You!)'.format(number1, pluralNoun, number2)           
def listOfJobsAutomatedByAI():
    state = random.choice(STATES)
    pronoun = random.choice(OBJECT__PRONUNS)
    return f"scientist bealive that in {state} jobs being automated by {pronoun}"
    pass 
def apoclypticEarthquick():
    pass 
def AItakingoverhuman():
    pass 
def globalwarming():
    pass 
def dinousors():
    pass 
        

if __name__ == '__main__':
    main()