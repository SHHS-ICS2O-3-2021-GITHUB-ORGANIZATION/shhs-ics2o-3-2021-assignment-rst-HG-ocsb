# NAME OF AUTHOR:Heleana Gordon
# NAME OF THE PROGRAM: Math Quiz
# DATE OF CREATION: 2/1/22
# PURPOSE OF PROGRAM: A math game involving addition, subtraction, multiplication and division questions with a range of numbers on three different levels

# VARIABLE DEFINITION
startNum = [1, 51, 151]
endNum = [50, 150, 300]
level = 0
num1 = random.randint(startNum[level], endNum[level])
num2 = random.randint(startNum[level], endNum[level])
num3 = random.randint(startNum[level], endNum[level])
num4 = random.randint(startNum[level], endNum[level])
num5 = random.randint(startNum[level], endNum[level])
num6 = random.randint(startNum[level], endNum[level])
num7 = random.randint(startNum[level], endNum[level])
num8 = random.randint(startNum[level], endNum[level])
loop = 'true'
loop = 'false'
truth = num7 / num8
level = level + 1
level = level + 1
level = 3

# INPUT
userin = (input())
ans1 = int(input())
ans2 = int(input())
ans3 = int(input())
ans4 = float(input())

# PROCESSING
#ask user if ready
import random
import math

#array to seed randint depending on level


if userin == 'go':
    while (level <= 2):
        

        loop = 'true'
        while (loop == 'true'):
            #print first question
           

            if ans1 != (num1 + num2):

            else:
                loop = 'false'

        loop = 'true'
        while (loop == 'true'):


            if ans2 != (num3 - num4):

            else:
                loop = 'false'

        loop = 'true'
        while (loop == 'true'):

            if ans3 != (num5 * num6):
               
            else:
                loop = 'false'

        loop = 'true'
        while (loop == 'true'):
            

            if math.isclose(ans4, truth, abs_tol=0.04):
                loop = 'false'
            else:
                

        level = level + 1

        if level < 2:
            
            answer = input()
            if (answer == 'yes'):
                level = level + 1
                
            else:
                
                #set level to greater than 2 to exit game

    #end if level <= 2
else:
    
# OUTPUT
print('Type go when ready or enter any letter to leave')
print('Level ' + str(level + 1))
print(str(num1) + ' ' '+' ' ' + str(num2))
print('Please try again')
print('Correct')
print(str(num3) + ' ' '-' ' ' + str(num4))
print('Please try again')
print('Correct')
print(str(num5) + ' ' '*' ' ' + str(num6))
print('Please try again')
print('Correct')
print(str(num7) + ' ' '/' ' ' + str(num8))
print('Correct')
print('Please try again')
print('Ready for next level? Type yes to continue or anything else to quit')
print('Leveling up...')
print('Goodbye')
print('Exiting game')

