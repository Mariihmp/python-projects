"""a logic game where you must guess a number based on clues
"""
import random

NUM_DIGITS = 2
MAX_GUESSES = 10

def main():
    print(f'''I'm thinking of  a {NUM_DIGITS}-digit number with no repeated digits.
          try to guess what it is here are some clues :
          when I say ------------ that means 
          #          one digit is correct but in the right position
          @          one digit is correct but in the wrong position
          *          no digit is correct
          for ex: if the secret number is 248 and your guess is 843,
          the clue would be FERMI PICO
          ''')
    while True:
        secret_num = get_secret_number()
        print('I have thought up a number .')
        print(f'you have {MAX_GUESSES} guesses to get it ')
        num_guesses = 1
        while num_guesses <= MAX_GUESSES:
            guess = ''
            while len(guess) !=NUM_DIGITS or not guess.isdecimal():
                print(f'guess {num_guesses}')
                guess = input('>>>')
                
                
            clues = get_clues(guess,secret_num)
            print(clues)
            num_guesses +=1
            if guess == secret_num:
                break
            if num_guesses > MAX_GUESSES:
                print('you ran out of guesses')
                print(f'the awnser was{secret_num}')
        
        #ask if they want to play again 
        print('do you want to play agin >> yes or no')
        if not input('>>>').lower().startswith('y'):
            break
    print('thanks for playing see you next time ')            
        

def get_secret_number():
    numbers = list('0123456789')
    random.shuffle(numbers)
    secret_num = ''
    
    for i in range(NUM_DIGITS):
        secret_num += str(numbers[i])
    return secret_num


def get_clues(guess,secret_num):
    if guess == secret_num:
        return 'you got this congrates'
    
    clues = []
    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append('#')
        elif guess[i] in secret_num:
            clues.append('@')
    if len(clues) == 0:
        return '*'
    else:
        clues.sort()
        return ' '.join(clues)

main()