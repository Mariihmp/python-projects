
import random

#higher or lower 
logo = """
  _    _ _       _                 _                           
 | |  | (_)     | |               | |                          
 | |__| |_  __ _| |__   ___ _ __  | |     _____      _____ _ __
 |  __  | |/ _` | '_ \ / _ \ '__| | |    / _ \ \ /\ / / _ \ '__|
 | |  | | | (_| | | | |  __/ |    | |___| (_) \ V  V /  __/ |  
 |_|  |_|_|\__, |_| |_|\___|_|    |______\___/ \_/\_/ \___|_|  
            __/ |                                              
           |___/                                               
"""
 
 
vs = """
 _    __   
| |  / /____
| | / / ___/
| |/ (__  )
|___/____(_)
"""
#for a better maintanace we could put thiis in diffrent file 
# countries_data = {
#     { "country":'United States', 
#         'population': 331883986,
#         'continent': 'North America',
#         'description': 'The United States of America is a country located in North America.'}
       
#     ,
#         {'country':'China',
#         'population': 1444216107,
#         'continent': 'Asia',
#         'description': 'China is a populous country in East Asia known for its rich history and culture.'}
#     ,
#        {'country': 'India', 
#         'population': 1393409038,
#         'continent': 'Asia',
#         'description': 'India is a diverse country in South Asia, known for its vibrant traditions and history.'} 
#     ,
#        {'country': 'Brazil',
#         'population': 213993437,
#         'continent': 'South America',
#         'description': 'Brazil is a vast country in South America, famous for its Amazon rainforest and lively carnivals.'} 
#     ,
#         {'country' :'Russia', 
#         'population': 145912025,
#         'continent': 'Europe/Asia',
#         'description': 'Russia is the largest country in the world, spanning both Europe and Asia with diverse landscapes.'}
#     ,
#       { 'country' :'Indonesia', 
#         'population': 273523615,
#         'continent': 'Asia',
#         'description': 'Indonesia is an island country in Southeast Asia with a rich blend of cultures and traditions.'} 
#     ,
#        { 'country' :'Pakistan',
#         'population': 225199937,
#         'continent': 'Asia',
#         'description': 'Pakistan is a country in South Asia known for its diverse landscapes and cultural heritage.}'
#     ,
#        { 'country' :'Nigeria',
#         'population': 211400708,
#         'continent': 'Africa',
#         'description': 'Nigeria is a West African country known for its cultural diversity and natural resources.'}
#     ,
#         'country' :'Bangladesh', 
#         'population': 166303498,
#         'continent': 'Asia',
#         'description': 'Bangladesh is a South Asian country with a rich history and a densely populated delta region.'
#     ,
#         'country' :'Mexico',
#         'population': 130262216,
#         'continent': 'North America',
#         'description': 'Mexico is a North American country known for its ancient ruins and vibrant culture.'
#     ,
#         'country' :'Japan', 
#         'population': 125837183,
#         'continent': 'Asia',
#         'description': 'Japan is an island nation in East Asia known for its advanced technology and unique culture.',
#         'country' :'Ethiopia', 
#         'population': 120048923,
#         'continent': 'Africa',
#         'description': 'Ethiopia is an East African country with a history dating back to antiquity and diverse wildlife.'
#     ,
#        {
#            'country' :'Philippines', 
#         'population': 112867743,
#         'continent': 'Asia',
#         'description': 'The Philippines is an archipelago country in Southeast Asia, known for its stunning beaches and warm hospitality.'}
#     ,
#         'country' :'Egypt', 
#         'population': 104258327,
#         'continent': 'Africa',
#         'description': 'Egypt is a country in North Africa known for its ancient pyramids and rich cultural heritage.'
#     ,
#         'country' :'Vietnam', 
#         'population': 97490013,
#         'continent': 'Asia',
#         'description': 'Vietnam is a Southeast Asian country known for its beautiful landscapes and rich history.'
#     ,
#         'country' :'DR Congo',
#         'population': 89979814,
#         'continent': 'Africa',
#         'description': 'The Democratic Republic of the Congo is a country in Central Africa with vast rainforests and wildlife.'
#     ,
#         'country' :'Turkey', 
#         'population': 85042782,
#         'continent': 'Asia/Europe',
#         'description': 'Turkey is a transcontinental country located mainly on the Anatolian Peninsula in Western Asia.'
#     ,
#         'country' :'Iran', 
#         'population': 84959240,
#         'continent': 'Asia',
#         'description': 'Iran is a country in Western Asia known for its ancient history and rich cultural heritage.'
#     ,
#         'country' :'Germany',
#         'population': 83132799,
#         'continent': 'Europe',
#         'description': 'Germany is a country in Central Europe known for its engineering achievements and cultural contributions.'
#     ,
#         'country' :'Thailand', 
#         'population': 69428524,
#         'continent': 'Asia',
#         'description': 'Thailand is a Southeast Asian country known for its stunning temples and delicious cuisine.'
    
# }
# a compare line first comparison
#vs line
#against line 


'''
1-generate a random account from the game data
2-format the account data into printable format
3- ask user for a guess

4- check if user is correct
##get follower count of each account 
# ## use if statement

give me a feedback on their games 
make them repeatable 
making the account at position b to a 


# '''
print(logo)
#generate a randome account 

def format_data(account):
    dict_country = countries_data['country']
    dict_population = countries_data['population']
    dict_continet = countries_data['continent']
    print(f"the country i s{dict_country} and the population is  {dict_population} and it's in {dict_continet}")

account_a = random.choice(list(countries_data['country']))
print(f"-----------------{account_a}")
# account_b = random.choice(countries_data)

# if account_a == account_b:
#     account_b = random.choice(countries_data)

# print(f"compare A: {format_data(account_a)}")
# print(vs)
# print(f"compare B: {format_data(account_b)}")

# guess = input('who has more followrs  Type  a or type B').lower()


# a_population  = account_a['population']
# b_population = account_b['population']

# def check_awnser(guess,a_population,b_population):
  