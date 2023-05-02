import random, sys 

print('''dice roller simulation enter what kind of dice you want to roll by this format 
---number of dice /d/the number of sides that dice have + or - adjusment ---

EX-- 3d6    --> rolls 3 times and 6-sided 
EX-- 1d10+2 --> rolls one time 10-sided dice and add 2 points
EX-- 2d38-1 --> rolls two times 38-sided dice and minus 1 point 
      
      
      ''')
while True:
    
        dice_str = input('---')
        if dice_str.upper() == 'QUIT':
            print('thanks for playing')
            sys.exit()
            
        dice_str = dice_str.lower().replace(' ','')
        d_index = dice_str.find('d')
        if d_index == -1:
            raise Exception('missing the -d- char')
        
        number_of_dice = dice_str[:d_index]
        if not number_of_dice.isdecimal():
            raise Exception("missing number of dice")
        number_of_dice = int(number_of_dice)
        
        #find if ther is a plus or minus sign 
        modIndex = dice_str.find('+')
        if modIndex == -1:
            modIndex = dice_str.find('-')
        
        #find the number of sides  the 5 in 3d5+1
        if modIndex == -1:
            number_of_sides = dice_str[d_index+1:]
        else:
            number_of_sides = dice_str[d_index+1 : modIndex]
        if not number_of_sides.isdecimal():
            raise Exception('missing the number of sides ')
        numberOfSides = int(number_of_sides)
        
        #find the modifire amount 
        if modIndex ==-1:
            modAmount =0
        else:
            modAmount = int(dice_str[modIndex+1:])
            if dice_str[modIndex] =='-':
                modAmount = -modAmount
    
    
        #SIMULATE THE DICE ROLL 
        rolls = []
        for i in range(number_of_dice):
            roll_result = random.randint(1 ,number_of_sides)
            rolls.append(str(roll_result))
            
        print("total: " + sum(rolls)+ modAmount,'(each die: ',end='')
        
        for i,roll in enumerate(rolls):
            rolls[i] = str(roll)
        print(','.join(rolls),end='')
        
        if modAmount !=0:
            modsign = dice_str[modIndex]
            print(f', {modsign} , {abs(modAmount)}',end='')
    
        