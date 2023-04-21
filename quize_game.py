
def new_game():
    guesses =[]
    correct_guesses = 0
    question_num = 1
    
    for key in questions:
        print('--------------')
        print(key)
        for i in options[question_num -1]:
            print(i)
        guesse = input('Enter (A B C)')
        guesse = guesse.upper()
        guesses.append(guesse)
        correct_guesses += check_answer(questions.get(key),guesse)#calling function to check 
        #if we are guessing correctly or not the key and guesses as a paramater
        question_num +=1    
    display_score(correct_guesses, guesses)
def check_answer(answer,guess):
    if answer == guess:
        print('Correct')
        return 1
    else:
        print('wrong')
        return 0 
    
def display_score(correct_guesses,guesses):
    print('----------------')
    print('Results')
    print('-----------------------------')
    print('answers:',end=' ')
    for i in questions:
        print(questions.get(i),end='')
    print()    
    
    print('Guesses:',end=' ')
    for i in guesses:
           print(i,end =' ')
    print()
    
    score = int((correct_guesses/len(questions))*100)   
    print('your score is : ' + str(score) + '%')  
def play_again():
    response = input('do you want to play again? (y/n)')
    response = response.upper()
    if response == 'y':
        return True
    else:
        return False

questions = {
    "who created python?":'A',
    "is the earth rounde?":'B',
    "is python a good language?":'C',
    "is AI going to kill us?":'A'
}
options = [
    ["A.guido van rossum",'B.elon f musk','C.zuckerburg'],
    ["A.yes",'B.no','C.not sure'],
    ["A.no",'B.yes','C.not sure3'],
    ["A.no",'B.yes','C.not sure']
]
new_game()