import random , datetime



birthdays = []
number_of_birthdays = 40 
def get_birthdays(number_of_birthdays):
    for i in range(number_of_birthdays):
        start_of_theyear = datetime.date(2001,1,1)
        randomNumberOfDays = datetime.timedelta(random.randint(0,364))
        birthday = start_of_theyear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

def get_match(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None #all the birthdays are unique
    
    #compare each birthday to every other birthday
    for i , birthday in enumerate(birthdays):
        for j , birthday2 in enumerate(birthdays[i+1:]):
            if birthday == birthday2:
                print(birthday)

print("""
      the birthday simulation shows us in a group of n people the odds
      that two of them have matching birthdays 
      which the chance is surprisingly large """)

MONTH = ('Jan', 'Feb', 'Mar', 'Apr', 'May',
         'Jun','Jul', 'Aug', 'Sep',
         'Oct', 'Nov', 'Dec')

while True:
    print('how many birthdays you want to be generated (max 100)')
    response = input('>>>')
    if response.isdecimal() and (0<int(response)<=100):
        numberOD = int(response)
        break
print()

#display the birthdays 
print(f'here are {numberOD}  birthdays')
birthdays = get_birthdays(numberOD)
for i , birthday in enumerate(birthdays):
    if i != 0:
        print(',', end='')
    monthName = MONTH[birthday.month -1]
    dateText = f'{monthName}{birthday.day}'
    print(dateText , end='  ')
print()
print()

#see if two birthdays match 
match = get_match(birthdays)

